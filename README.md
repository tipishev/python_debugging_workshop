# Python Debugging Workshop

## Transcript

### Introduction

Hello everyone! My name is Tim and today I will talk about Python debugging.

![Debugging Game](/images/debugging_game.png)

First of all, how many of you use a debugger in your daily workflow?

* \<½ Awesome! It means that a lot of you will go to lunch with a new tool under the belt.
* \>½ Nice! Then you already know quite a few things that I tell, and it will be a refresher, with a few tips and tricks on top.

Some developers say they don't need a debugger in a scripting language, since they can just look at the source. On one hand it's true and there is a saying

> "If you need a debugger, the error had happened much earlier."

Meaning that someone had complicated the code so much that reading the source does not help much.

![Tunnelbana](/images/tunnelbana.png)

But on the other hand, a complex application, can be compared to a transit system. Of course, you have your source: the transit map and schedules. But would you bet your lunch money on the exact location of any given train?

![Rube Goldberg](/images/rube_goldberg.jpg)

That is exactly the problem, that the debuggers solve. They allow us to see inside the black box and examine the runtime state of the code.

While preparing this workshop I have looked at a number of debugging tutorials and they all follow the same structure.

* They warn agains using `print` statements
* They recap Pdb documentation
* And show a few examples of using debugger commands

I tried to make this workshop a bit differently: on top of the three points above we will also look at other Python debuggers and learn when it is better to use one or the other. Another thing that I will tell is useful tips and tricks.

### Print Considered Harmful

![Boat vs Surf](/images/boat_vs_surf.jpg)

I am legally required to scorn you for `print`-debugging and explain what's wrong with it.

![Printgles](/images/printgles.png)

First of all, one print is never enough, like Pringles, once you pop, you cannot stop
You put one, it doesn't work, then you put another one, and yet another one. And to see your changes you need to restart your code every time, which can be quite slow, especially in a dockerized setup, and this is not what we want. We want a short feedback loop to test our theories as fast as we can.

Another argument against `print`s is that they ofthen get into production code. If you don't believe me, just search your codebase.

![Bearded Crab](/images/crab.png)

By the way, "it will get to production" applies not only to `print` statements, but to any silly code and data. I call this phenomenon the "The Law of The Bearded Crab". When I was working for an entertainment events aggregator, we used silly fake events for testing our staging environment. And guess what, one day, a misconfigured import, uploaded "the Concert of The Bearded Crab" to the main page.

One more argument for using a debugger is that you can easily look into runtime of not only your code, but also the one of 3rd parties, like Django and celery.

Finally, `print` is very limitted in what it can do and is often used just to check whether the code runs at all. Using `print` for that is an overkill, there is a 3-character Python built-in function for that.

Behold the mighty Redneck Breakpoint

`1/0`

unlike print it does not get lost in console output, and you don't have to decorate it with `=...=` or `*...*` it just crashes your program loudly and proudly. If you have several places to check where they run, you can use `2/0`, `3/0`, etc.

Ok, now that we are done with print-shaming, let's get started.

### Debugging as Text Adventure

How many of you have played MUDs?
What about Roguelikes or Interactive Fiction (IF)?

Then you will find console-debugging similar to playing such a game:

They are both...

* controlled with a few commands:
  - "north, open, examine" in games
  - and "next, step, continue" in debugger
* the commands can be abbreviated:
  - In interactive fiction it is common to have `n` for (n)orth, `o` for (o)pen, and `x` for e(x)amine
  - Python debugger has the same: `n` for (n)ext, `s` for (s)tep, and `c` for (c)continue
* Both can be harsh:
  - if you die in a game you start from the beginning
  - unhandled exceptions stop the debugger

By the way, if you are into text adventures, at last year's Pycon Sweden there was a great talk about Evennia, a Python MUD-framework.

Funnily enough, when we look at our codebases, the similarity with dungeons becomes stronger. See for yourself, our codebases are built over years by multiple programmers, and sometimes you need Git archeology to dig up history, but it's a topic from my another talk.

A typical code-dungeon looks like this:

![Dungeon](/images/dungeon.png)

* a single point of entry
* each function is a corridor
* the more lines there is in a function the longer the corridor
* calling a function within a function takes you one level deeper down the stack
* returning from a function takes you one level up, to the line where you entered
* luckily there are no GOTO statements in Python, so each function has a single point of entry,
* though, it may have multiple return points, for example a condition check may return the result earlier. And even if you don't return explicitly, Python returns an implicit None.
* One thing to note about this diagram is that numbers are not the actual line numbers in the files, they are relative to each function. In real code all functions may be defined in the same file and their starting line number can be anywhere, but lines are always consecutive.

Because of these similarities, I prepared a small game "The Quest for Golden Python", while going through it we will work with different aspects of using a debugger.

### Installation

Does everyone have Python 3.7+ installed? It's not critical as long as you have Python3.

If you want to follow along, clone this repository from

* https://github.com/tipishev/python_debugging_workshop
* or here is a short link https://git.io/JeEhw

```bash
git clone git@github.com:tipishev/python_debugging_workshop.git
cd python_debugging_workshop
virtualenv -p python3.7 venv
. venv/bin/activate
pip install -r requirements.pip
cd dungeon
```

Let's open `play.py` in your favourite text editor. Here we create a `Player` instance, with a name and an empty starting inventory. As you can see, the `Player` class itself is very simple.

All locations in the game are functions that accept the player instance as an argument and hopefully return it back, possibly modifying its state, mostly the inventory. In `play.py` we enter the `main_corridor` from which all the other corridors branch. The goal of the game is to get the Golden Python, and possibly save the world.

### Quest 0: Scare the Rat

So, if everyone is ready, let's run the game.

```bash
python play.py
```

We immediately see an error, that happened in the `main_corridor`. The player was eaten by a rat. Looks like we need to have at least something in our inventory. Let's take a broomstick, big enough to scare the rat away. And run the the game again.

```bash
./play.py
```

### Walking


Having a broom helped, but now we see a different error and can finally use a debugger. There are different ways to start it. In this example we can put a hardcoded breakpoint in our code right before the player enters the main corridor.


_type `import pdb; pdb.set_trace()` right above `player = main_corridor(player)`_

You don't have to worry about `ImportError`: `pdb` is in the standard library.

Now, when we run `play.py` we are greeted by the Pdb prompt.

```bash
./play.py
```

Debugger stops the program right after the `set_trace()` line and politely asks us what to do next.

For example we can just `quit` the debugger with `q`

_do that_

or tell it to `continue` with `c`

_do that_

and happily crash at the exception.

Not very useful. The fun starts when we learn to navigate our code dungeon.

There are 2 types of movement:

* horizontal – within a single function
* vertical – up and down the call stack

Let's have a quick tutorial on moving within a single function:

![Next](/images/walking/1_next.png)

The first command is called `next`, it simply takes us to the next line. Here and in following examples, blue shows the position before the command, the orange – the position after. So, if we were on line 42 and typed next, we are taken to line 43.

![Next on call](/images/walking/2_on_fun.png)

If we are on a line that makes a function call, we have 2 choices.

![On fun next](/images/walking/3_on_fun_next.png)

We can choose `next` and it the function executes behind the scenes and we continue in the current function. Think of next: "stay local and avoid any foreign functions"

![On fun step](/images/walking/4_on_fun_step.png)

Or we can type `step` and go vertically one level down in the nested function and continue horizontal movement there.

![Until](/images/walking/5_until.png)

We can also use command `until {line_number}` instead of typing `next` or `n`.
`until` stops on return, `until` to break out of loops

![Return](/images/walking/6_return.png)

Or we can type `return` or `r` and stop just before returning to the function above.
Useful when we lose interest in the current function, got stuck in a loop, or stepped in the function by accident and would like to go back.

We can also use command `until {line_number}` instead of typing `next` or `n`.

We can press `next` and it wil


Here are a couple of immediately useful commands:

* `list` to show the source code  _type it_ the arrow shows where we are
* `step` to enter the function call _type it_ it takes us inside the corridor
* `next` to advance to the next line _type it_

These commands can also be abbreviated to `l`, `s`, and `n` respectively. We will talk more about these commands in the following exercises.

As I mentioned earlier, PDB shows just the current line, so almost always we would like to go to the next line and see the code around it.
We can do this by separting commands with double semicolon.

```python
n ;; l
```

We can also set these command as aliases:

```python
alias nl n;;l
alias sl s;;l
```

We will talk about helpful aliases as we go.

To quit the debugger just type `q`. We see a Traceback because to stop, the debugger raises a special `bdb.BdbQuit` exception.

For this exercise we will use `ipdb`, a wrapper around PDB that adds tab-completion, color, and multiline context support.

For that we can add a couple of `i`s in the earlier breakpoint.  _add those 'i's_
Now, all the goodness of iPython is available to us. Another improvement is that you can set how many lines of context you would like to see. _add context=5_

![Lighting](/images/lighting.png)

In the game, context can be compared to how much of the corridow we can see. In default Pdb it's horrible: just one line and no syntax highlight, so it's black-and-white mole-vision. Things get better if we use `n ;; l` and `s ;; l` aliases, we see 11 lines, but again, no colors. Ipdb finally solves this problem by having proper syntax highlighting and `context`-kwarg, that you can use directly:

`import ipdb; ipdb.set_trace(context=10)` or via a `breakpoint` built-in in Python 3.7: `breakpoint(context=10)`.


Let's go through this level in ipdb.

To avoid the bearded crab problem use git pre-commit hooks to clear

* `print`
* `breakpoint` / `set_trace`


### Pdb bashing

How many of you use Python version less that 3.7?

_raise hand, too_

Good, before 3.7, starting a debugger takes more keystrokes.
For the record, Pdb is not my favourite debugger:

* shows just one line of context
* has poor tab-completion
* does not support colors

If I can, I use any other debugger. But in spite of all its shortcomings, Pdb has one killer feature: it is part of the standard library. So, if you ssh to a server, but have no permission to install a better debugger, you can still run Pdb.

-----------------------------------------------------------
                Here Be Dragons
-----------------------------------------------------------

### Miscellaneous :-/
* warn about single-letter variables, use `!` to be sure
  - `c`, `n`, etc. but serves right, don't use one-letter variables
  - `list`, `args` are more treacherous

### Looking
* looking tutorial diagram, limited to 1 file, different listing ways

### Stacking

* `where` also shows the caller id of who called the whole shebang
* Image: stacktrace stairs/elevator
* inspired by SCP-087
* alias for traceback size
* `import pdb; pdb.Pdb(skip=['django.*']).set_trace()`

* Pdb commands for displaying current level

* mention `a` arguments
* show how to navigate up and down the stack
* `sys.tracebacklimit` default 1000, `sys.setrecursionlimit`

### Jumping

* In real world jumping helps to skip
  - network calls
  - initialization before debug-section
  - expensive computation in loops

combined e.g. `records = decode_xml(requests.get('http://example.com/huge.xml'))`

* go back if you forgot to check something

* pudb jump not working https://github.com/inducer/pudb/pull/306

### Running

* `run`, `runeval`, `runcall` are boring but useful with no access to code


### Preventing Bugs

Be a condescending twat and talk how it's better to write good code instead of fixing errors.

### Conclusion

* Now you know what to do when you encounter a bug
  - configure a debugger of choice: `pdb`, `ipdb`, or `pudb`
  - insert a breakpoint
  - if it's live use one of `run`, `runeval`, or `runcall` or `set_trace` in a closure

* Call to action
  - set up useful aliases (which?)
  - the next time you time your code breaks, put `import ipdb; ipdb.set_tace(context=10)`

* https://github.com/git-game/git-game

### Aliases

* `alias` can take all arguments with `%*`
* `vars` built-in master race vs dirty `__dict__` peasants
* `import pprint; pprint(self.__dict__)` vs `pp vars(self)`
* knapsack metaphor, "but in-game inventory is not the only thing we take"
* incremental introduction to aliases
* `alias n next ;; list` -> `unalias n`

### Postmortem

* Source Code 2011 movie
* "I wish I was there when it happened!"
* since it's postmortem, cannot follow the runtime, just observe the state at the moment of crash
* multiple ways to start
  - `python -m pdb|ipdb|pudb play.py arg1 arg2` and crash
  - `import *db; *db.pm()` in interactive shell. Will use `sys.last_traceback` for examination
  - `%debug` in iPython

# Examination

* (a)rguments to see what was passed
* `p`  if you really miss that `print`
* `pp` a bag ~full of JSON~ of `dict`s, arrange lines vertically for clue
* pprint sorts keys
* `display` can list current expressions, local for frame
* `undisplay` can clear one or many expressions
* display shows old value, neat!
* display to create a "watch list"


### Debug with access to source code

* PEP553
* `breakpoint()` in 3.7+
  - defaults to `pdb.set_trace`
  - raison d'être:
    * easy to remember
    * linters complain
    * even JavaScript has it!
  - configure to the debugger of your choice
  - `breakpoint(*args, **kwargs)` useful for passing `context=10`
  - simple values `0` for none, `1` for default, `some.importable.callable`
  - `export PYTHONBREAKPOINT=ipdb.set_trace`
  - `export PYTHONBREAKPOINT=pudb.set_trace`
  - `export PYTHONBREAKPOINT=0` to ignore breakpoints
* something to hook onto, `None`

### Configuration
* mostly useful for aliases
* pdb config file .pdbrc or ~/.pdbrc, local overrides global, as in git or laws

### Debug without access to source code
* debugging live in a closure, when no better idea
* shows 3 ways to run a command:
  - run
  - runeval
  - runcall
* example with running property: `ipdb.run('obj.property')`
* mocking live code

### Anatomy of PDB
* [PDB, IPDB, BDB, CMD] diagram with explanation of responsibilities
* debugger is extensible, `Pdb` class, `bdb` and `cmd` modules
* inherits from `cmd.Cmd` and `cmd.Bdb`

#### CMD aside
* client code spectrum:
  - simple script
  - command with arguments
  - Command line environment
  - Graphical wrapper
* part of the standard library
* creates a simple command-line interace (CLI) interpreter
* documentation page has a cute example `TurtleShell`
* Cmd2 is actually better, common pattern with standard implementations

#### Bdb
* defines `Breakpoint` class `(file, line)`
* `trace_dispatch(frame, event, arg)`
  - line
  - call
  - return
  - exception
  - c_call
  - c_return
  - c_exception
* breakpoints manipulation:
  - set_break
  - clear_break
  - clear_bpbynumber
  - clear_all_file_breaks
  - clear_all_breaks
  - `get_{bpbynumber, break, breaks, file_breaks}`

### Breakpoints
* breapoints allow a test-journey:
  - instead of put print here, restart, put print there, restart
  - put break here, check. Put break there, check within a single run
* one-time breakpoints
* watching variables with post-run `commands`
* %debug iPython magic
* pinfo, pinfo2: real story `DictWriter.field_names`
* break
  - filename:lineno | function
  - condition
* tbreak aka tea break
* `_` variable stores the result of previous ivocation
* PUDB
* web-pdb `PYTHONBREAKPOINT=web_pdb.set_trace` for multithreaded
* condition may be useful when a bug happens only on certain conditions, like looping over a bunch of records, and only orders from France are processed incrorrectly.
* it's better to avoid modifying the code with `breakpoint`/`set_trace`, less chance of committing to production
* `python -m ipdb -c "b levels/main.py:13" -c "b levels/main.py:14" play.py`

### Debuggers comparisson

* PDB vs iPDB vs PDB++ vs PUDB vs IDE

#### Pdb
  * available everywhere
  * simple
  - very basic, rough on the edges shows bdb.Quit
  - no color

#### iPdb
  * can start as `%debug` from iPython or `debug function(args, **kwargs)`
  * tab-completion
  * colors
  - requires iPython 
  - no extended functionality as in Pdb++

#### Pudb:
  * Graphical
  * Shows the whole source
  * Shows source, vars, stack, breakpoints, console on the same screen
  - ∓ uses `Vi`-style navigation
  - works better on bigger screens 
  - no jumps https://github.com/inducer/pudb/issues/129
  * watch-statements
  * code, variables, stack, breakpoints

#### Pdbpp
  * avoids one-letter trap by preferring context variables to debugger commands, can override with `!!command`
  * Disable `pdb.set_trace()`: any subsequent call to it will be ignored
  * `@pdb.break_on_setattr(attrname, condition=always)`
  - hijacks Pdb name

#### IDE/Visual debuggers
  * no stray code
  * better display of variables
  * jump to source
  - cannot run in terminal
  - extra steps for remote or container debugging 
  - loss of oldschool-cred

* Image: debugger skill-chart
  - 1/0
  - print
  - pdb
  - ipdb / pdb++
  - pudb* / graphical / IDE
  - avoiding bugs with isort, flake8, autopep8

### Pdb++

* sticky mode: same as showing context?
* track draws a dependency graph and requires pypy
* `display` expressions should not have side effects
* can open editor
* can mark some frames as hidden using a decorator, don't display in stacktrace
* shell shell_pp python ipython pdb ipdb pdb pdb_pp, common pattern
* setattr condition can discriminate between 2 instances of the same class
* `break_on_setattr` can be attached even from within debugger. 

#### Config
* prompt
* highlight
* some colors settings
* editor `vim` by default or `editor = "subl {filename}:{lineno}"`
* hiding frames and showing their count, useful if you trust Django/celery or other 3rd party libraries
* `setup(self, pdb)`
* Pygments config, for example if you want `solarized` theme


#### Pudb

### iPdb tricks

* %autoreload
* %debug% instead of .pm()

### Dungeon Ideas

* one-letter trap, mimic!
* short commands: `l` - look, `a` - around
  - a,b,c for 3 rats doesn't work, tell about `!`
* args, to see who entered the function/room with us
* hide function arguments with *args and **kwargs
* increase context lines number, picture of a knight opening visor
  - use context size as a game mechanic aka light?
* Sphinx's puzzle with going back in time inside a function with `jump`
* make a "look" command to check surroundings (local variables?)
* debugging inside a closure == inside the dragon's belly
* source the enemy to see weakness?
* display/undisplay to check surroundings
* `display` to check coin count, try multiple, actually not necessary in 2.7, use commands to look at `Mock.call_count`
* condition can be decreasing health.

## Quotes

### Edsger Dijkstra

> They are errors, not bugs.

> If you want more effective programmers, you will discover that they should not waste their time debugging, they should not introduce the bugs to start with.

### Unknown

> Debuggers don't remove bugs. They only show them in slow motion.

## Used Materials
TODO image sources, use tineye?
