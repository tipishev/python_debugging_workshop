# Python Debugging Workshop

Here I combine notes and slides for my Python debugging workshop

# Transcript

## Quotes
> "Debuggers don't remove bugs, they show them in slow-mo"  # TODO source
> "They are errors, not bugs" Edsger Dijkstra

## Introduction

Hello everyone! My name is Tim and in today's workshop I will talk about debugging Python.

How many of you have used a debugger before?

* <½ Awesome! It means that a lot of you will go to lunch with a new tool under your belt
* >½ Nice! Then a lot of what I tell today will be a refresher, with a few tips and tricks on top.

Let's talk about debugging in general. Some developers say they don't need a debugger in a scripting language, since they can just look at the source. On one hand it's true and there is a saying

> "If you need a debugger, the error had happened much earlier."

But on the other hand, a complex application, can be compared to a transit system. Of course, you have your source: the transit map and schedules. But would you bet your lunch money on the exact location of any given train? That is the problem, we want to see inside the black box and see the runtime state of our code.

While preparing this workshop I have looked at a number of debugging tutorials and they all follow the same structure.

* "Don't use print!"
* A recap of PDB doc help page
* A few examples of using debugger commands

I tried to make this workshop slightly different

---
There is a silly factoid that we remember

* 30% of what we hear
* 50% of what  we see
* 80% of what we do
* ~~95% of what we teach~~
---

That's why in this workshop we will hands-on solve a series of puzzles, each one focusing on some aspect of Python debugging.

How many of you have been there last year?
Then you probably remember the talk about Evennia, Python-based Multi-User Dungeon (MUD) framework.

How many of you have played MUDs?
What about Roguelikes or Interactive Fiction (IF)?

Then you will also find using the debugging is similar to playing such a game:

* controlled with a few commands: "north, open, examine" vs "next, step, where"
* the commands can be abbreviated: "(n)orth, (o)pen, e(x)amine" vs "(n)ext, (s)tep, w(here)"
* most actions are irreversible: "items can be lost forever" vs "function calls cannot be undone"
* permadeath: "if you die you start from the beginning" vs "unhandled exceptions stop the debugger"

When we look at real life long-running codebases, the similarity to dungeons becomes inevitable. See for yourself, our codebases are built over years by multiple programmers, some of whom have left the company and you need Git archeology to find what you need, but it's a topic for another talk.

A typical code-dungeon looks like this:

* a single point of entry
* each function is a corridor
* the more lines in a function the longer the corridor
* calling a function within a function takes you one level deeper
* returning from a function takes you one level up
* one function can have multiple return points
* (luckily Python has no GOTO so we don't have weird teleports)
* on the diagram the numbers are relative to function, therefore start from 1. In real code all functions could be defined in the same file and the actual start could be on any line, though lines are always consecutive.


Before we start, I am legally required to tell you why `print`-debugging is bad:

* one is never enough: like Pringles, once you pop, you cannot stop
* it will get in production, just search your codebase for those stray prints

By the way "it will get to production" applies not only to `print` statements, but also to anything you put in your code for debugging and fun. I call this the "The Law of Bearded Crab". When I was working for an entertainment event aggregator, we used silly fake events for testing. Ang one day, after an incorrect import, "the Concert of Bearded Crab" appeared on the main page.

So, without further ado let's get to tutorial.

## Main part

### Setup

Does everyone have Python 3.7 + installed?

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

All locations in the game are functions that accept the player instance as an argument and return it back, possibly modifying its state. Or don't return it and raise an exception instead. In `play.py` we enter the main_corridor from which all the other corridors branch. The goal of the game is to get the Golden Python.

### First Run

Let's run the game.
```bash
./play.py
```

We immediately see an error. Let's look what happened in the `main_corridor`. Ok, we need to have at least something in our inventory. Let's take a broomstick, big enough to scare away a rat. By the way, here you can see how the `main_corridor` is structured, there are several branching functions, each focusing on some aspect of Python debugger. At the end of each sub-corridor we get a key. We need to collect them all to unlock the final challenge.


### Walking

Let's run the game again.
```bash
./play.py
```

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

We will talk about aliases later.
To quit the debugger just type `q`. We see a Traceback because to stop, the debugger raises a special `bdb.BdbQuit` exception.

For this exercise we will use `ipdb`, a 345-line wrapper around PDB that adds tab-completion, color, and multiline context support.

For that we can add a couple of `i`s in the earlier breakpoint.  _add those 'i's_
Now, all the goodness of iPython is available to us. Another improvement is that you can set how many lines of context you would like to see. _add context=5_

Let's go through this level in ipdb.


To avoid bearded crab use git pre-commit hooks to clear

* print
* breakpoint

### Looking

### Jumping

In real world jumping helps to:

* skip heavy operations
* avoid broken code
* go back if you forgot to check something


### Stacking

* inspired by SCP-087
* alias for traceback size
  - `alias hd import traceback ;; p len(traceback.format_stack())`

* Pdb commands

* mention `a` arguments
* show how to navigate up and down the stack
* infinite recursion trap without base case, bottomless pit, actually 1000 calls bottom
* `sys.setrecursionlimit`



## Conclusion

* Now you know what to do when you encounter a bug
  - configure a debugger of choice: `pdb`, `ipdb`, or `pudb`
  - insert a breakpoint
  - if it's live use one of `run`, `runeval`, or `runcall` or `set_trace` in a closure

* Call to action
  - set up useful aliases (which?)
  - the next time you time your code breaks, put `import ipdb; ipdb.set_tace(context=10)`


## Images

* iPython iceberg dark internet
* [PDB, IPDB, BDB, CMD] diagram with explanation of responsibilities
* how do we read stack overflow
* how do we read github repositories (in relation to pudb)
* ~~dungeon map~~ + lighting + jumping possibility
* stacktrace stairs/elevator
* walking n, s, unt, c, r
* looking diagram, limited to 1 file, different listing ways
* debugger skill-chart / snake-brain meme?
  - 1/0
  - print
  - pdb
  - ipdb
  - pudb* / graphical / IDE
  - avoiding bugs with isort, flake8, autopep8, broken windows theory
* PDB vs iPDB vs PUDB vs IDE
  - Pdb: upside: available everywhere, downside: very basic, rough on the edges shows bdb.Quit
  - iPdb: upside: can start as %debug from iPython, downside: none, it's my fave
  - Pudb: downside: no jumps, show github issue
  - IDE debuggers, downside: cannot run in terminal, loss of oldschool-cred



## Topics

* useful aliases, combining, passing parameters
* ;; multiple commands
* pretty-print with pp
* `vars` built-in master race vs dirty `__dict__` peasants
* one-time breakpoints
* watching variables with post-run commands
* %debug iPython magic
* pdb has no `context=10` option

* `breakpoint()` in 3.7+
  - defaults to `pdb.set_trace`
  - raison d'être:
    * easy to remember
    * linters complain
    * even JavaScript has it!
  - configure to the debugger of your choice
  - `breakpoint(*args, **kwargs)` useful for passing context=10
  - simple values `0` for none, `1` for default, `some.importable.callable`
  - `export PYTHONBREAKPOINT=ipdb.set_trace`
  - `export PYTHONBREAKPOINT=pudb.set_trace`
  - `export PYTHONBREAKPOINT=0` to ignore breakpoints

* post-mortem
* debugging live in a closure
* ~pickling traceback for later debugging~ not possible to pickle tracebacks
* pdb config file .pdbrc or ~/.pdbrc, local overrides global, as in git or laws
* pinfo, pinfo2: real story `DictWriter.field_names`
* break
  - filename:lineno | function
  - condition
* tbreak aka tea break
* `_` variable stores the result of previous ivocation
* mocking live code
* PUDB
* web-pdb `PYTHONBREAKPOINT=web_pdb.set_trace` for multithreaded

### iPdb tricks

* %autoreload
* %debug% instead of .pm()
* other magic commands?

## https://docs.python.org/3/library/pdb.html notes

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


## https://www.youtube.com/watch?v=mbdYATn7h6Q  Pudb tutorial from PyBay 2017

* one `print` is never enough, will definitely get in production, war story about bearded crab
* watch-statements
* code, variables, stack, breakpoints


## PDB help notes
* make fancy debugger
* warn about single-letter variables, use `!` to be sure
* `bt` alias for `where`
* file-specified breakpoint looks on `sys.path`, `.py` can be skipped
* enable/disable breakpoints, multiple (space separated list)

## cmd.py

### sources

* https://docs.python.org/3/library/cmd.html
* https://github.com/python/cpython/blob/3.7/Lib/cmd.py

### what it does

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

## bdb.py

### sources

* https://docs.python.org/3/library/bdb.html
* https://github.com/python/cpython/blob/3.7/Lib/bdb.py

### what it does

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


## https://github.com/python/cpython/blob/master/Lib/pdb.py

Notes on the latest PDB source.

* `find_function` uses `re`, delayed context manager
* `getsourcelines` uses `inspect.findsource`, special logic for modules
* `lasti2lineno` uses `dis.filndlinestarts`, what's `lasti`?
* `_rstr` String that doesn't quote its repr., what is it for?
* line_prefix

### class PDB

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

## Dungeon game

### Ideas

* short commands: `l` - look, `a` - around
  - a,b,c for 3 rats doesn't work, tell about `!`
* args, to see who entered the function/room with us
* hide function arguments with *args and **kwargs
* increase context lines number, picture of a knight opening visor
  - use context size as a game mechanic aka light?
* up and down the floors in stack, multiple floors aka elevator
* Sphinx's puzzle with going back in time inside a function with `jump`
* make a "look" command to check surroundings (local variables?)
* cannot modify the code, only .pdbrc
* debugging inside a closure == inside the dragon's belly
* source the enemy to see weakness?
* display/undisplay to check surroundings
* `display` to check coin count, try multiple
* interact: a safespace to experiment?
* we can use `!` only n-times?
* ~morbid traceback pickling, black bag with another adventurer's traceback~
* narrate to sys/err?
* flat structure: 3 dungeon branches, each with key, one final room
* use ipdb.rc for provisioning
* use termcolor?
* aliases for solving puzzles
* bottomless pit of recursion missing a basecase
* use money mechanic to buy a key or get killed by a shopkeep

* all deaths are preventable with proper preparation!!!
* hm... maybe passwords to avoid redoing boring exercises
* condition can be decreasing health.

### Realized notes
* launching `./dungeon.py` seems the easiest
* `__` works quite well for a filler
* uranium coins? fix by rewriting pickup-hook
* use emojis, e.g. hearts for health status


### Description

So, without further ado we descend into the Dungeons of Doom.

### Locations

#### Quitting

* show q(uit)

#### Walking

* demonstrates
  - n(ext)
  - s(tep)
  - r(eturn)
  - unt(il)
  - c(ont(inue))

* start with pdb, show it's ugliness
* show `nl`, `sl` to show how to make it better in absence of `ipdb`
* continue with ipdb, show breakpoints(), mention production hooks

#### Looking
* not so painful with `context`: demonstrate
* not required for PUDB, demonstrate


#### Running

* shows 3 ways to run a command:
  - run
  - runeval
  - runcall
* example with running property: `ipdb.run('obj.property')`
* ! is guard, running python commands is forbidden "magic"
* something to hook onto

#### Jumping

* jumping is useful to skip
  - expensive computation in loops
  - initialization before debug-section
  - network calls
* pudb jump https://github.com/inducer/pudb/pull/306


#### Aliasing

* knapsack metaphor, "but in-game inventory is not the only thing we take"
* use really useful aliases
  - examine `dict`
  - dump to file
* incremental introduction to aliases

#### Examination

* (a)rguments to see what was passed
* `p`  if you really miss that `print`
* `pp` a bag ~full of JSON~ of `dict`s, arrange lines vertically for clue


### Meta

* analogy with building a dungeon at work
* https://github.com/git-game/git-game

## Reading List

* https://github.com/spiside/pdb-tutorial
* all the help tree in PDB's `h` menu
* https://realpython.com/python-debugging-pdb/
* https://www.codementor.io/stevek/advanced-python-debugging-with-pdb-g56gvmpfa
* https://blog.ironboundsoftware.com/2016/10/31/6-quick-python-debugging-tips/
* example .pdbrc https://nedbatchelder.com/blog/200704/my_pdbrc.html
* iPDB (345 LOC): https://github.com/gotcha/ipdb
* David Beazley's cookbook, search for "frame", "debug", and "pdb"
* look at https://www.nnja.io/post/2019/djangocon-2019-goodbye-print-hello-debugger/
* https://pbs.twimg.com/media/EFbZsS_W4AAQ5Sh?format=jpg&name=900x900
* https://github.com/pdbpp/pdbpp
