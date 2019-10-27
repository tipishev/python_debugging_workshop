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

Meaning that someone had complicated the code so much that reading the source is not enough anymore.

![Tunnelbana](/images/tunnelbana.png)

But on the other hand, a complex application, can be compared to a transit system. Of course, you have your source: the transit map and schedules. But would you bet your lunch money on the exact location of any given train?

![Rube Goldberg](/images/rube_goldberg.jpg)

That is exactly the problem, we would like to see inside the black box and examine the runtime state of our code.

While preparing this workshop I have looked at a number of debugging tutorials and they all follow the same structure.

* "Don't use print!"
* A recap of PDB documentation
* A few examples of using debugger commands

I tried to make this workshop a bit differently

### Print Considered Harmful

![Boat vs Surf](/images/boat_vs_surf.jpg)

However, I am legally required to shame you for `print`-debugging and exmplain what's wrong with it.

![Printgles](/images/printgles.png)
First of all, one print is never enough, like Pringles, once you pop, you cannot stop
You put one, it doesn't work, then you put another one, and yet another one. And to see your changes you need to restart your code every time, which can be quite slow, especially in a dockerized setup, and this is not what we want. We want a short feedback loop to test our theories as fast as we can.

Another argument against `print`s is that they ofthen get into production code. If you don't believe me, just search your codebase.

![Bearded Crab](/images/crab.png)

By the way "it will get to production" applies not only to `print` statements, but to any silly code and data. I call this the "The Law of Bearded Crab". When I was working for an events aggregator, we used silly fake events on staging. And guess what, one day, a misconfigured import, put "the Concert of Bearded Crab" on the main page.

One more argument for using a debugger is that you can easily look into runtime of not only your code, but also the one of 3rd parties, like Django and celery.

Finally, print is ofthen used to see if the code runs at all. It's such a waste, Python has a 3-character built-in for that.

Behold the mighty Redneck Breakpoint

`1/0`

unlike print it does not get lost in console output, it just crashes loudly and prodly.

Ok, now that we are done with print-shaming, let's get started.

### Debugging as Text Adventure

How many of you have played MUDs?
What about Roguelikes or Interactive Fiction (IF)?

Then you will find console-debugging similar to playing such a game:

They are both...

* controlled with a few commands:
  - "north, open, examine" vs "next, step, where"
* the commands can be abbreviated:
  - "(n)orth, (o)pen, e(x)amine" vs "(n)ext, (s)tep, w(here)"
* some actions are irreversible:
  - "items can be lost forever" vs "function calls cannot be undone"
* permadeath:
  - "if you die you start from the beginning" vs "unhandled exceptions stop the debugger"

By the way, on last year's Pycon Sweden there was a great talk about Evennia, a Python-framework in which you can build your own Multi-User Dungeon.

Funnily enough, when we look at our codebases, the similarity with dungeons becomes stronger. See for yourself, our codebases are built over years by multiple programmers, and sometimes you need Git archeology to dig up history, but it's a topic from my another talk.

A typical code-dungeon looks like this:

![Dungeon](/images/dungeon.png)

* a single point of entry
* each function is a corridor
* the more lines there is in a function the longer the corridor
* calling a function within a function takes you one level deeper down the stack
* returning from a function takes you one level up, to the line where you entered
* luckily there are no GOTO statements in Python, so each function has a single point of entry,
* though it may have multiple return points, for example a condition check may return the result earlier. And even if you don't return explicitly, Python returns an implicit None.

* One thing to note about this diagram the numbers are not the actual line numbers in the files, they are relative to each function. In real code all functions may be defined in the same file and their starting line number can be anywhere, but lines are always consecutive.

### Installation

If you want to follow along please clone this repository.

Does everyone have Python 3.7+ installed?

We start by cloning the repository.

```bash
git clone git@github.com:tipishev/python_debugging_workshop.git
cd python_debugging_workshop
virtualenv -p python 3.7 venv
. venv/bin/activate
pip install -r requirements.txt
cd dungeon
```

Let's open `play.py`. Here we create a `Player` instance, with a name and empty starting inventory.

All locations in the game are functions that accept the player instance as an argument and return it back, possibly modifying its state. Or don't return it and raise an exception instead. In `play.py` we enter the main_corridor from which all the other corridors branch. The goal of the game is to get the Golden Python and save the world.

### Quest 0: Scare the Rat

Let's run the game.
```bash
./play.py
```

We immediately see an error. Let's look what happened in the `main_corridor`. Ok, we need to have at least something in our inventory. Let's take a broomstick, big enough to scare away a rat. By the way, here you can see how the `main_corridor` is structured, there are several levels, each focusing on some aspect of Python debugger. At the end of each we get an amulet. We need to collect them all to collect the Golden Python.

### Walking

Let's run the game again.

```bash
./play.py
```

Now we have a different error and can use a debugger.

Now we get a different error, now coming from the `walking_corridor`. Here we can finally start a debugger. Right before entering the `main_corridor`.

How many of you use Python version less that 3.7?

_raise hand, too_

Good, before 3.7, starting a debugger takes more keystrokes.

_type `import pdb; pdb.set_trace()` right before entering the main corridor_

Now, when we run `play.py` we drop into Pdb prompt. For the record, Pdb is not my favourite debugger:

* shows just one line of context
* has poor tab-completion
* does not support colors

If I can, I use any other debugger. But in spite of all its shortcomings, Pdb has one killer feature: it is part of the standard library. So, if you ssh to a server, but have no permission to install a better debugger, you can still run Pdb.

As with most games, we need to start with the controls. There are 2 types of movement in the dungeon:

* horizontal – within a single function
* vertical – up and down the call stack


Let's start with a quick tutorial on horizontal movement, since we will use the most.

![Next](/images/walking/1_next.png)

The first command is called `next`, it simply takes us to the next line. Here and in following examples, blue shows the position before the command, the orange – the position after. So, if we were on line 42 and typed next, we are taken to line 43.

![Next on call](/images/walking/2_on_fun.png)

If we are on a line that makes a function call, we have 2 choices.

![On fun next](/images/walking/3_on_fun_next.png)

We can choose `next` and it the function executes behind the scenes and we continue in the current function.

![On fun step](/images/walking/4_on_fun_step.png)

Or we can type `step` and go one level down in the nested function and continue horizontal movement there.

![Until](/images/walking/5_until.png)

We can also use command `until {line_number}` instead of typing `next` or `n`.

![Return](/images/walking/6_return.png)

Or we can type `return` or `r` and stop just before returning to the function above.

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


-----------------------------------------------------------
                Here Be Dragons
-----------------------------------------------------------

### Looking
* looking tutorial diagram, limited to 1 file, different listing ways

### Stacking

* Image: stacktrace stairs/elevator
* inspired by SCP-087
* alias for traceback size

* Pdb commands for displaying current level

* mention `a` arguments
* show how to navigate up and down the stack
* `sys.setrecursionlimit`

### Jumping

* In real world jumping helps to skip
  - network calls
  - initialization before debug-section
  - expensive computation in loops

combined e.g. `records = decode_xml(requests.get('http://example.com/huge.xml'))`

* go back if you forgot to check something

* pudb jump not working https://github.com/inducer/pudb/pull/306


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

## Topics

#### Quitting

* show q(uit)

### Aliases

* `vars` built-in master race vs dirty `__dict__` peasants
* `import pprint; pprint(self.__dict__)` vs `pp vars(self)`
* knapsack metaphor, "but in-game inventory is not the only thing we take"
* incremental introduction to aliases

### Postmortem

* Source Code 2011 movie
* "I wish I was there when it happened!"
* since it's postmortem, cannot follow the runtime, just observe the state at the moment of crash
* multiple ways to start
  - `python -m pdb|ipdb|pudb play.py` and crash
  - `import *db; *db.pm()` in interactive shell. Will use `sys.last_traceback` for examination
  - `%debug` in iPython

# Examination

* (a)rguments to see what was passed
* `p`  if you really miss that `print`
* `pp` a bag ~full of JSON~ of `dict`s, arrange lines vertically for clue
* pprint sorts keys


### Debug with access to source code

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
* CMD, CMD2

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
* breakpoint regexp?

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


## Reading notes

### https://docs.python.org/3/library/pdb.html notes

* debugger is extensible, `Pdb` class, `bdb` and `cmd` modules
* `ipdb.run('dungeon.main()')`
* envoke as a script `python3 -m ipdb dungeon.py`
* auto-restart program, preserves breakpoints
* `run` set breakpoints, accepts globals and locals kwargs, code object
* `runeval` returns the expression result. Ok.
* `runcall` to run a callable
* `run`, `runeval`, `runcall` are boring but useful with no access to code
* `set_trace` FTW, could not test header in `ipdb`
* `alias` can take all arguments with `%*`
* `interact` what's the use?
* `p`... why would I use it instead of !command?, I guess if one misses prints
* `>>` marks current exception


### https://www.youtube.com/watch?v=mbdYATn7h6Q  Pudb tutorial from PyBay 2017

* one `print` is never enough, will definitely get in production, war story about bearded crab
* watch-statements
* code, variables, stack, breakpoints


### PDB help notes
* make fancy debugger
* warn about single-letter variables, use `!` to be sure, `list` can trip, so can one-letter vars, so can `args`
* `bt` alias for `where`
* file-specified breakpoint looks on `sys.path`, `.py` can be skipped
* enable/disable breakpoints, multiple (space separated list)

### cmd.py

#### sources

* https://docs.python.org/3/library/cmd.html
* https://github.com/python/cpython/blob/3.7/Lib/cmd.py

#### what it does

* creates a simple command-line interace (CLI) interpreter
* creates a Read Evaluate Print Loop (REPL)
* pases input as `foo *args` where `foo` is a command
* commands are are defined as methods `do_foo`
* provides help based on command-method's docstrings
* handles empty-string command, default: repeat the last command
* allows `!`-prefixed execution in a shell
* manages command context-aware tab-completion (`complete_foo`)
* allows pre- and post- command hooks
* sets a default action for unrecognized commands
* sets prompt, e.g. `(Pdb)`
* output redirection defaults are `stdin`, `stderr`, `stdout`
* formats help to terminal-friendly 80 characters
* queues multi-line commands, e.g. code blocks
* documentation page has a cute example `TurtleShell`

### bdb.py

#### sources

* https://docs.python.org/3/library/bdb.html
* https://github.com/python/cpython/blob/3.7/Lib/bdb.py

#### what it does

* defines `BdbQuit` exception to stop the debugger
* defines `Breakpoint` class `(file, line)`
* defines `Bdb` default Python debugger class, `skip` argument
* `trace_dispatch(frame, event, arg)`
  - line
  - call
  - return
  - exception
  - c_call
  - c_return
  - c_exception
* `dispatch_{line, call, return, ...}`
* stop_here/break_here/break_anywhere
* `user_{call, line, return, exception}`
* do_clear
* `set_{step, next, return, until, trace, continue, quit}`
* breakpoints manipulation:
  - set_break
  - clear_break
  - clear_bpbynumber
  - clear_all_file_breaks
  - clear_all_breaks
  - `get_{bpbynumber, break, breaks, file_breaks}`
* stack trace presentation
  - get_stack
  - format_stack_entry
* `run/runeval/runcall`
* checkfuncname, effective, set_trace


### https://github.com/python/cpython/blob/master/Lib/pdb.py

Notes on the latest PDB source.

* `find_function` uses `re`, delayed context manager
* `getsourcelines` uses `inspect.findsource`, special logic for modules
* `lasti2lineno` uses `dis.filndlinestarts`, what's `lasti`?
* `_rstr` String that doesn't quote its repr., what is it for?
* line_prefix

#### class PDB

* inherits from `cmd.Cmd` and `cmd.Bdb`
* initializes both parents with relevant `__init__` args
* prompt is initialized to `(Pdb) `
* has dicts for aliases and displaying
* `mainpytfile`/`wait_for_mainpyfile`
* tries to use `readline` with a ridiculous regexp
* successively reads global and local `.pdbrc`
* has breakpoint-number-keyed dicts for
  - commands
  - commands_doprompt
  - silent
* flag and bp number for defining commands
* `sigint_handler`
* `reset` delegates to `bdb.Bdb`, calls `self.forget`
* `self.forget` resets line number, stack, current index, frame, tb_lineno
* `setup` forget(), `tb_lasti`, caches lineno, and `curframe.f_locals`
* `execRcLines` check for `self.onecmd` and not comment (`'#'`)
* overrides Bdb `.user_call`, `.user_line`, `.bp_commands`
* bp_commands
  - bdb sets self.current_bp
  - checks self.commands
  - one_cmd
  - checks silencing and prompting
* user_return

### Python sys docs

* `call_tracing` call from debugger checkpoint
* `_current_frames`
* `breakpointhook`
* `displayhook` populates `_` variable
* `excepthook(exc_type, exc_instance, traceback)`
  - interactive: returns control to the shell
  - program: exits
* original non-overriden values are stored in
  - `sys.__breakpointhook__`
  - `sys.__displayhook__`
  - `sys.__excepthook__`
  - `sys.__unraisablehook__`
* `exc_info` finds unhandled exception on stack.
* `sys._getframe([depth])`
* `sys.gettrace()`
* ` sys.__interactivehook__`
* these exist for `pdb.pm()` and `%debug`'s sake
  - `last_type`
  - `last_value`
  - `last_traceback`
* `ps1`, `ps2` can be dynamic in `interact` mode
* `sys.settrace(tracefunc)`
  - 'call'
  - 'line'
  - 'return'
  - 'exception'
  - 'opcode', `f_trace_opcodes=True'`
* `tracebacklimit` default 1000


### Python traceback docs
* `print_tb(tb, limit=None, file=None)` file to object, alias?
* `print_exception`
* `print_exc` helper for `sys.exc_info()`
* `print_stack`
* `format_list/exception/exc/tb/stack`, as above, but just formats
* `walk_stack/tb`
* `TracebackException` lightweight exception wrapper
* Syntax errors are treated slightly differently
* StackSummary for nicely printing
* FrameSummary


### https://www.nnja.io/post/2019/djangocon-2019-goodbye-print-hello-debugger/

```
# Install IPython: python3 -m pip install ipython

import IPython
from traitlets.config import get_config

cfg = get_config()
cfg.InteractiveShellEmbed.colors = "Linux"  # syntax highlighting
cfg.InteractiveShellEmbed.confirm_exit = False

alias interacti IPython.embed(config=cfg)
```

### https://github.com/spiside/pdb-tutorial

* shorter feedback loop -> better debugger person
* Pdb-precedence gotcha
* listing 3rd party packages code
* one-letter trap, mimic!
* `b` to list breakpoints
* `cl(ear)` one or all breakpoints
* `r` when you lose interest and just want it to be over, loop it

### https://realpython.com/python-debugging-pdb/ (amazingly useful)

* debugger stops the program and asks what to do next
* `breakpoint` is PEP553
* `python -m pdb play.py arg1 arg2`
* test an alternative implementation directly in the application
* `next` to stay local and avoid any foreign functions
* `alias n next ;; list` -> `unalias n`
* breakpoint condition, not line but function
* (c)ontinue to the next breakpoint, nothing can stop it except bp or exception
* put new breakpoint when a current stop brought no result
* condition, enable, disable, clear
* condition may be useful when a bug happens only on certain conditions, like looping over a bunch of records, and only orders from France are processed incrorrectly.
* break function_name:lineno to have enough vars for a condition check
* `tbreak` self-destructs after entering
* `until` stops on return
* `until` to break out of loops
* `display` can list current expressions, local for frame
* `undisplay` can clear one or many expressions
* display shows old value, neat!
* display to create a "watch list"
* stack, frame, where-output can be confusing, illustrate with image
* frame is a data structure that python creates when calling a function and deletes when it returns
* stack is a LIFO list of frames
* stack overflow happens when there are more frames on the stack than it is allowed
* `bt` is yet another silly alias for `where`
* check `help` or `help n`
* `where` also shows the caller id of who called the whole shebang
* print cheat sheet


### https://www.codementor.io/stevek/advanced-python-debugging-with-pdb-g56gvmpfa

* `python3 -mpdb play.py` for postmortem
* it's better to avoid modifying the code with `breakpoint`/`set_trace`, less chance of committing to production
* `l 1,999` to list the entire file
* `b mymodule.function`
* `r` to quickly get out if stepped in by mistake
* `until` to get out of loops
* `python -m ipdb -c "b levels/main.py:13" -c "b levels/main.py:14" play.py`
* restart behavior is unclear, cannot recover after an exception
* watch throuh commands, `silent` seems useless in my setup
* `-m pdb` will drop in debugger on unhandled exceptions

### https://blog.ironboundsoftware.com/2016/10/31/6-quick-python-debugging-tips/ 

* in iPython: `debug fun(args)` drops into that function, super neat! What the hell will happen when you call it? No modifications
* pdb++ may work better with Py2

## Used Materials
TODO image sources, use tineye?
