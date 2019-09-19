# python_debugging_workshop

Here I combine notes and slides for my Python debugging workshop

## Topics

* pdb basic usage
* increase context
* pretty-print with pp
* `vars` built-in master race vs dirty `__dict__` peasants
* one-time breakpoints
* watching variables with post-run commands
* stack-dungeon with up and down
* %debug iPython magic
* post-mortem
* debugging live in a closure
* pickling traceback for later debugging
* frame-hacking, review David Beazley's book


## TODO
* read PDB source (1729 LOC): https://github.com/python/cpython/blob/master/Lib/pdb.py
* read iPDV (345 LOC): https://github.com/gotcha/ipdb
