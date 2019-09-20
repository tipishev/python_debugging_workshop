# python_debugging_workshop

Here I combine notes and slides for my Python debugging workshop


## Topics

* pdb basic usage
* pretty-print with pp
* `vars` built-in master race vs dirty `__dict__` peasants
* one-time breakpoints
* watching variables with post-run commands
* %debug iPython magic
* post-mortem
* debugging live in a closure
* pickling traceback for later debugging
* pdb config file
* pinfo, pinfo2
* break
  - filename:lineno | function
  - condition


## Dungeon game

* short commands: l - look, a - around
* args, to see who entered the function/room with us
* hide function arguments with *args and **kwargs
* increase context lines number, picture of a knight opening visor
  - use context size as a game mechanic aka light?
* up and down the floors in stack, multiple floors aka elevator
* Sphinx's ridiculous puzzle with going back in time inside a function with `jump`
* make a "look" command to check surroundings (local variables?)
* pp inventory
* cannot modify the code, only pdbrc
* debugging inside a closure == inside the dragon's belly
* enter to repeat command, keep walking
* source the enemy to see weakness?
* display/undisplay to check surroundings
* interact: a safespace to experiment
* we can use `!` only n-times
* morbid pickling
* narrate to sys/err?

### Meta

* remember the last year talk about Multi-user Dungeons (MUD)
* analogy with building a dungeon at work
* mention `l`, `u`, and `d` reminding of Interactive Fiction (IF)

## TODO

* review David Beazley's book on frames and frame hacking
* read PDB source (1729 LOC): https://github.com/python/cpython/blob/master/Lib/pdb.py
* read iPDV (345 LOC): https://github.com/gotcha/ipdb
