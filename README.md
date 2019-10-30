# Python Debugging Workshop

## Transcript

### Introduction

Hello everyone! My name is Tim and today I will talk about Python debugging.

<img src="/images/debugging_game.png" width="400" title="Debugging Game">

First of all, how many of you use a debugger in your daily workflow?

* \<½ Awesome! It means that a lot of you will go to lunch with a new tool under the belt.
* \>½ Nice! Then you already know quite a few things that I tell, and it will be a refresher, with a few tips and tricks on top.

Some developers say they don't need a debugger in a scripting language, since they can just look at the source. On one hand it's true and there is a saying

> "If you need a debugger, the error had happened much earlier."

Meaning that someone had complicated the logic so much that reading the source code does not help.

<img src="/images/tunnelbana.png" width="400" title="Tunnelbana">

But on the other hand, a complex application, can be compared to a transit system. Certainly, you have your "source code": the transit map and schedules. But would you bet your lunch money on even approximate location of any given train?

<img src="/images/rube_goldberg.jpg" width="400" title="Rube Goldberg">

That is exactly the problem, that the debuggers address. They allow us to look inside the black box and examine the runtime state of the code.

While preparing this workshop I have looked at a number of debugging tutorials and they all follow the same structure.

They

* warn agains using `print` statements
* recap Pdb documentation
* show examples of using debugger commands

I tried to make this workshop a bit differently: on top of the three points above we will look at different Python debuggers and ways to invoke them depending on the context: whether you develop locally, or run code in a remote shell. I will also share pragmatic tips from my day-to-day.

### Print Considered Harmful

![Boat vs Surf](/images/boat_vs_surf.jpg)

Before we start, I am legally required to talk about `print`-debugging and what's wrong with it.

First of all, `print` is limitted in what it can do and is often used simply to check whether the code runs at all. Using `print` for that is an overkill, there is a better way. Python has a 3-character Python built-in for that.

`1/0`

Also known as the Redneck Breakpoint

unlike the timid `print` it does not get lost in the console output, it crashes your program loudly and proudly. If you need more than one, use `2/0`, `3/0`, etc.

<img src="/images/printgles.png" width="400" title="Printgles">

Secondly, one print is never enough, like Pringles, once you pop, you cannot stop.
You put one, it doesn't work, then you put another one, and yet another one. And in order to see the changes you need to restart the application every time, which may be quite slow, for example in Docker. We want a short feedback loop to test our bug-origin theories as fast as we can without breaking the flow of thought.

The third argument against `print`s is that they ofthen get into production code. If you don't believe me, just search your codebase git history.

<img src="/images/crab.png" width="400" title="Bearded Crab">

By the way, "it will get to production" applies not only to `print` statements, but to anything that touches your code but should not go to production . I call this extension of the Murphy's law the "The Curse of The Bearded Crab". I used to work for an entertainment events aggregator, and we put silly fake events in our staging environment. And guess what, one day, a misconfigured import, uploaded "the Concert of The Bearded Crab" to the main page. So, think of the Bearded Crab as an evil deity who preys on you losing focus.

Finally, a debugger allows to explore not only your application code, but to also step inside 3rd party modules that your code uses.

So, next time your fingers type `print`, please stop and put a debugger breakpoint instead.

### Debugging as Text Adventure

Ok, enough with `print`-shaming.

![Text Adventures](/images/text_adventures.jpeg)

How many people in this room have played text adventure games such as MUDs, Roguelikes, or Interactive Fiction?

Then you will find console-debugging similar to playing such a game:

They are both...

* controlled with just a few commands:
  - "north, south, open, examine" in games
  - and "next, step, break, continue" in debugger
* the commands can be abbreviated to single letters:
  - In interactive fiction it is common to have `n` for (n)orth, `o` for (o)pen, and `x` for e(x)amine
  - Python debugger has the same: `n` for (n)ext, `s` for (s)tep, `b` for (b)reak, and `c` for (c)continue
* Both can be harsh:
  - In Nethack, the most known roguelike, when you die you lose all progress, but can identify your possessions at the moment of death.
  - When an unhandled exception hits you in a debugger, you cannot continue, but enter a post-mortem mode to look at the program state at the moment of exception.

Funnily enough, when we look at our codebases, the similarity with dungeons becomes only stronger. See for yourself, we build them over years, layer upon layer, with parts of them getting abandoned, here and there you see scarce outdated comments from people who are no longer with you. The process of recovering the lost knowledge is akin to archeology, but instead of a pickaxe you (dig up history)[https://github.com/tipishev/git_workshop] with Git commands.

A typical code-dungeon looks like this:

![Dungeon](/images/dungeon.png)

* a single point of entry
* each function is a corridor
* the more lines in a function the longer the corridor
* calling a function within a function takes you one level deeper down the call stack
* returning from a function returns you one level up, to the line where you entered
* luckily there are no GOTO statements in Python, so each function has a single point of entry,
* though, it may have multiple return points, for example a condition check may return the result earlier. And even if you don't return explicitly, Python returns an implicit None.
* On this diagram the numbers are relative to each function. In real code all functions may be defined in the same file and their starting line number can be anywhere, but lines in a function are always consecutive.

For your entertainment I prepared a small game "The Quest for Golden Python", while going through it we will work with different aspects of using a debugger.

### Installation

Does everyone have Python 3.7+ installed? It's not critical as long as you have Python3.

If you want to follow along, please clone this repository from

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

_give 3-5 minutes to setup_

Before we start, let's edit `play.py`. Here we create an instance of `Player` with a name and an empty starting inventory. As you can see, the `Player` class itself is very simple.

All locations in the game are functions to which we pass the player instance and hopefully they return player back. The game starts with enterng `main_corridor` from which all the other corridors branch. The goal of the game is to obtain the Golden Python, and possibly save the world, I don't know.

### Quest 0: Scare the Rat

So, if everyone is ready, let's run the game.

```bash
python play.py
```

We immediately see an error, that happened in the `main_corridor`. The player was eaten by a rat. Judging by the error message we need to have at least something in our inventory. Let's take a big broomstick, to scare the rat away. And run the the game again.

```bash
./play.py
```

### Walking

Having a broom helped, but now we hit a different error and can use a debugger. There are a few ways to start a debugger, depending on how much control you have over the source code. Here we are in full control, so let's put a hadcoded breakpoint, right before entering the main corridor.

_type `import pdb; pdb.set_trace()` right above `player = main_corridor(player)`_

You don't have to worry about `ImportError`: `pdb` is part of the standard library.

```bash
./play.py
```

> Debuggers don't remove bugs. They only show them in slow motion.
– Unknown

Now, when we run `play.py` we are greeted by the Pdb prompt.
Pdb becomes our Dungeon Master, stops the program on the line after the breakpoint and politely asks us what to do next.

First of all, we can just `quit` the debugger with `q`

_do that_

or tell it to `continue` running towards the error with `c`

_do that_

Or we can look around us, with `l`, which stands not for `look` as in text adventures but for `list`.

The real fun begins when we start navigating our code dungeon.

There are 2 types of movement:

* horizontal – within a single function or frame
* vertical – up and down the call stack

Let's look at moving within a single function:

![Next](/images/walking/1_next.png)

The first command is called `next`, it simply takes us to the next line. Here and in following examples, blue shows the position before the command, the orange – the position after. So, typing `next` on line 42 takes us to line 43.

![Next on call](/images/walking/2_on_fun.png)

If we are on a line with a function call, we have 2 choices.

![On fun next](/images/walking/3_on_fun_next.png)

We can choose `next` and the nested function executes behind the scenes and we continue to line 45. Think of `next` as "stay local and avoid any foreign functions".

![On fun step](/images/walking/4_on_fun_step.png)

Or we can type `step` and go vertically one level down to line 17, inside the nested function and continue horizontal movement there.

![Until](/images/walking/5_until.png)

We can also fast travel with `until {line_number}` instead of typing `next` or `n`.
This command is useful for skipping loops. If lines 18 to 20 contained a loop, both `next` or `step` would make us go through each iteration.

If a return happens before the `{line_number}`, debugger stops there. For example, if I accidentally typed `until 210`, the debugger would stop on line 23 and wait for further commands.

![Return](/images/walking/6_return.png)

If we specifically want to stop before returning to the calling function , we can type `return` or `r`.

It gets useful when we

* lose interest in the function and just want to see what it returns
* get stuck in a loop
* or `step` in the nested function by accident, instead of typing `next`

Let's try these commands in the debugger.

But before we do that, let's get a lantern. By default Pdb shows just the current line, so we may have to use `l` a lot. Instead, we can use an iPdb, an iPython-wrapper around Pdb. For that we just add a couple of `i`s to our hardcoded breakpoint.

Notice the improvements:

* we now have color vision with syntax highlight
* we see 3 lines of context instead of just one

Now let's step in the `walking_corridor` and get our first amulet.

_go through walking corridor: warn about `!`, `c`, `n`, etc. serves right, don't use one-letter variables, `list`, `args` are more treacherous_

Now we can add the 'amulet of walking' to our inventory.

### Stacking

Since you see how the game is structured we can move `set_trace()` directly in the main corridor. And while we are at it, let's give us even more light with `context=5`

Let's go to the next level and see how to navigate vertically in the call stack.

_go through stacking corridor; mention (a)rgs and how they are local to each frame where shows who started the whole circus_

Now, let's add the "amulet of stacking" to our evergrowing collection and and see what fails next.

How many of you use Python version less that 3.7?

_raise hand, too_

But when we switch to Python 3.7, we can start using a builtin keyword `breakpoint()`.

It was introduced in PEP553 because..

* The linter complains about multiple statements on one line
* It's short and easy to remember
* Even JavaScript has a `debugger` builtin

Let's put it by the entrance to the corridor of looking.

It defaults to `pdb.set_trace`  _demonstrate_
To configure it use `export PYTHONBREAKPOINT=`...

* "" (unset) for default Pdb
* 0 for ignoring breakpoints, can be the last line of defence in Production environment.
* dotted path to a debugger callable
  - `ipdb.set_trace` for iPdb
  - `pudb.set_trace` for Pudb (we'll look at it later)

`breakpoint` passes args and kwargs to the handler, so we can put `breakpoint(context=7)` will make iPdb show 10 lines of context.

_demonstrate with context=7_

Since we talk about showing context, here is an illustration of context showing in Pdb and iPdb.

<img src="/images/lighting.png" width="640" title="Lighting">

If we use the dungeon metaphor, context is how much of surroundings you can see.

By defaul, PDB shows just the current line, so often we would type `l` after `n` or `s`.
We can turn this into a one liner with double-semicolon:

```python
n;;l
s;;l
```

We can also set aliases:

```python
alias nl n;;l
alias sl s;;l
```

Finally, for maximum slack, save the aliases to `.pdbrc` to load them at debugger start.

I don't use Pdb unless nothing better is installed, however, Pdb has one killer feature: it is in the standard library. So, if you ssh to a server, have no install permissions, you can still run Pdb.

iPdb gives us both color vision and more context.


### Looking

So, let's go through looking level.

_do the looking level_

So far, we've been dropping the hardcoded breakpoints. This is fine most of the time, but still gives the Bearded Crab a chance to sneak your breakpoints in the release. The ninja-way is to use the debugger without changing the source code. Here is one way to do it.

```bash
python -m ipdb play.py
```

This way we start from the very first line and keep going. We can avoid this journey by passing a breakpoint.

```bash
python -m ipdb -c "b levels/examination.py:71" play.py
```

### Examination

_do the examination level_

You may also want to use a debugger inside an interactive shell, like django shell or iPython. When I just started using a debugger I write a wrapper function around the code I wanted to debug like this:

```python
def run():
    import ipdb; ipdb.set_trace()
    jumping_corridor(player)
```

### Running in Shell / Jumping

But later I found that Pdb has 3 functions for exactly that:

* run
* runeval
* runcall

The last one I find the most usefull. Pass into it a callable, and it's arguments and the the call will happen under debugger's control. Let's try that.

```python
from play import main_corridor, player
ipdb.runcall(main_corridor, player)
```

* In real world jumping helps to skip
  - network calls
  - expensive computation before debug-section

combined e.g. `records = decode_xml(requests.get('http://example.com/huge.xml'))`

* go back if you forgot to check something

### Postmortem

While we talk about running code inside a shell, there's a super-useful debugger feature "postmortem" abbreviated to `pm()`. It finds the last exception that happened iin the shell and allows to explore the state right before it happened.

* Source Code 2011 movie
* "I wish I was there when it happened!"
* since it's postmortem, cannot follow the control, just observe the state at the moment of crash.
* multiple ways to start
  - `python -m pdb|ipdb|pudb play.py arg1 arg2` and crash
  - `import *db; *db.pm()` in interactive shell. Will use `sys.last_traceback` for examination
  - `%debug` in iPython
* when a long-running script crashes in your shell, type `%debug` and walk up the stack and see what happened. It may give insights on what was the error about. Not so long ago, I was fetching events from our partner and ran postmortem on a failed script, it showed me the exact URL on which the connection was reset, so I could continue from that exact spot.


-----------------------------------------------------------
                Here Be Dragons
-----------------------------------------------------------


### Breakpoints
* it was a celery task, so I put a breakpoint to avoid the celery dispact resolving shim sham shimmy, advice: with much wrapping put a breakpoint where you are sure it will reach.
* `b 108,statistic_type=='spam'`
* breapoints allow a test-journey:
  - instead of put print here, restart, put print there, restart
  - put break here, check. Put break there, check within a single run
* one-time breakpoints
* watching variables with post-run `commands`
* %debug iPython magic
* break
  - filename:lineno | function
  - condition
* tbreak aka tea break
* `_` variable stores the result of previous ivocation
* condition may be useful when a bug happens only on certain conditions, like looping over a bunch of records, and only orders from France are processed incrorrectly.
* it's better to avoid modifying the code with `breakpoint`/`set_trace`, less chance of committing to production
* `python -m ipdb -c "b levels/main.py:13" -c "b levels/main.py:14" play.py`

### Preventing Bugs

> If you want more effective programmers, you will discover that they should not waste their time debugging, they should not introduce the bugs to start with.
  – Edsger W. Dijkstra

Talk how it's better to write good code instead of fixing errors.

* flake8
* autopep8
* isort

### .pdbrc and aliases
* pdb config file .pdbrc or ~/.pdbrc, local overrides global, as in git or laws
* mostly useful for aliases
* `alias` can take all arguments with `%*`
* `import pprint; pprint(self.__dict__)` vs `pp vars(self)`
* even if you cannot write to `.pdbrc`, keep your local config up-to-date and paste the aliases file in remote Pdb-shells, after all it's just a list of legal debugger commands.

### Anatomy of PDB
* [PDB, IPDB, BDB, CMD] diagram with explanation of responsibilities
* inherits from `cmd.Cmd` and `cmd.Bdb`
* debugger is extensible, `Pdb` class, `bdb` and `cmd` modules

#### Bdb
* the core of all python debuggers
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

### Debuggers comparisson

* Talk in spectrum Availability -> Features
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
  * sticky mode: same as showing context?
  * track draws a dependency graph and requires pypy
  * `display` expressions should not have side effects
  * can open editor
  * can mark some frames as hidden using a decorator, don't display in stacktrace
  * shell shell_pp python ipython pdb ipdb pdb pdb_pp, common pattern
  * setattr condition can discriminate between 2 instances of the same class
  * `break_on_setattr` can be attached even from within debugger.

#### Config
  * max pimping
  * prompt
  * highlight
  * some colors settings
  * editor `vim` by default or `editor = "subl {filename}:{lineno}"`
  * hiding frames and showing their count, useful if you trust Django/celery or other 3rd party libraries
  * `setup(self, pdb)`
  * Pygments config, for example if you want `solarized` theme

#### Pdb++ aka Pdbpp
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
  - they cost money?

* Image: debugger skill-chart
  - 1/0
  - print
  - pdb
  - ipdb / pdb++
  - pudb* / graphical / IDE
  - avoiding bugs with isort, flake8, autopep8


### Strace ?
```bash
sudo strace -s 65535 -v -p {PID}
```

### Conclusion

* Now you know what to do when you encounter a bug
  - configure a debugger of choice: `pdb`, `ipdb`, or `pudb`
  - insert a breakpoint
  - if it's live use one of `run`, `runeval`, or `runcall` or `set_trace` in a closure

* Call to action
  - install `ipdb`, `pudb`, and `pdbpp` in all environments where you are allowed to run a Python shell
  - add useful aliases to a .pdbrc file, to not type `pp vars(self)` all the time
  - the next time you time your code breaks, put `import ipdb; ipdb.set_tace(context=10)`
