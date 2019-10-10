# python_debugging_workshop

Here I combine notes and slides for my Python debugging workshop


## Plan

### Introduction

"if you need debugging something went wrong long before you hit the bug"


### Main part

* help commands

### Conclusion

* Now you know what to do when you encounter a bug
  - insert a breakpoint
  - if it's live use one of `run`, `runeval`, or `runcall` or `set_trace` in a closure

* Call to action
  - set up useful aliases (which?)
  - the next time you time your code breaks, put `import ipdb; ipdb.set_tace(context=10)`


## Images

* [PDB, IPDB, BDB, CMD] diagram with explanation of responsibilities
* how do we read stack overflow
* how do we read github repositories (in relation to pudb)
* dungeon map + lighting + jumping possibility
* stacktrace stairs/elevator
* walking n, s, unt, c, r
* debugger skill-chart / snake-brain meme?
  - 1/0
  - print
  - pdb
  - ipdb
  - pudb*
  - avoiding bugs with isort, flake8, autopep8, messy room analogy





## Topics

* pdb basic usage
* useful aliases, combining, passing parameters
* ;; multiple commands
* pretty-print with pp
* `vars` built-in master race vs dirty `__dict__` peasants
* one-time breakpoints
* watching variables with post-run commands
* %debug iPython magic
* breakpoint() in Py3.7
* post-mortem
* debugging live in a closure
* pickling traceback for later debugging
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

* autoreload
* %debug% instead of .pm()
* other magic commands?

## https://docs.python.org/3/library/pdb.html notes

* debugger is extensible, `Pdb` class, `bdb` and `cmd` modules
* `ipdb.run('dungeon.main()')`
* envoke as a script `python3 -m ipdb dungeon.py`
* auto-restart program, preserves breakpoints
* `breakpoint()` built-in in 3.7+, find a way to switch to `ipdb`
  - `export PYTHONBREAKPOINT=ipdb.set_trace`
  - `export PYTHONBREAKPOINT=pudb.set_trace`
  - `export PYTHONBREAKPOINT=0` to ignore breakpoints
* `run` set breakpoints, accepts globals and locals kwargs, code object
* `runeval` returns the expression result. Ok.
* `runcall` to run a callable
* `run`, `runeval`, `runcall` are boring but useful with no access to code
* `set_trace` FTW, could not test header in `ipdb`
* `alias` can take all arguments with `%*`
* `interact` what's the use?
* `p`... why would I use it instead of !command?, I guess if one misses prints
* `>>` marks current exception


* TODO `post_mortem` STUDY sys.traceback!

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
* jump over pits
* make a "look" command to check surroundings (local variables?)
* pp a bag full of JSON
* cannot modify the code, only .pdbrc
* debugging inside a closure == inside the dragon's belly
* enter to repeat command, keep walking
* source the enemy to see weakness?
* display/undisplay to check surroundings
* `display` to check coin count, try multiple
* interact: a safespace to experiment
* we can use `!` only n-times
* morbid traceback pickling, black bag with another adventurer's traceback
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

#### Looking

* shows ways to list a file - l(ist)
  - just line
  - lines range
  - line with count
* look puzzle: look at line 42, look 42 lines lower, 47 higher, etc.

#### Fooscending

* show how to navigate up and down the stack
* infinite recursion trap without base case, bottomless pit, actually 1000 calls bottom

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

* knapsack metaphor
* use really useful aliases
  - examine `dict`
  - dump to file


### Meta

* mention inspiration of nethack
* remember the last year talk about Multi-user Dungeons (MUD)
* analogy with building a dungeon at work
* mention `l` (look or light), `u`, and `d` reminding of Interactive Fiction (IF)
* mention git game
* nethack

## Reading List

* PDB help docs
* all the help tree in PDB's `h` menu
* https://realpython.com/python-debugging-pdb/
* https://www.codementor.io/stevek/advanced-python-debugging-with-pdb-g56gvmpfa
* https://blog.ironboundsoftware.com/2016/10/31/6-quick-python-debugging-tips/
* example .pdbrc https://nedbatchelder.com/blog/200704/my_pdbrc.html
* iPDB (345 LOC): https://github.com/gotcha/ipdb
* on bdb https://docs.python.org/3/library/bdb.html#module-bdb
* on https://docs.python.org/3/library/cmd.html#module-cmd
* David Beazley's cookbook, search for "frame", "debug", and "pdb"
* look at https://www.nnja.io/post/2019/djangocon-2019-goodbye-print-hello-debugger/
* https://github.com/pablogsal/gdb-emoji
* https://pbs.twimg.com/media/EFbZsS_W4AAQ5Sh?format=jpg&name=900x900
* https://www.nnja.io/post/2019/djangocon-2019-goodbye-print-hello-debugger/
