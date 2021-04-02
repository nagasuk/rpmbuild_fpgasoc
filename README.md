RPM Build Environment for fpgasoc suite
=======================================

Overview
--------
Environment to build rpm package of fpgasoc suite.
The target software managed in this repository is as follows:
* `drvfpgasoc`
* `libfpgasoc`
* `util_fpgasoc`

How to build
------------
```sh
$ rpmbuild -ba --clean <path to this repository top>/SPECS/<target to build>.spec
```

Requirement
-----------
* rpmbuild

License
-------
Please see `LICENSE.md` file for details.

