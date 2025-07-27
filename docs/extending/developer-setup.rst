Setup for Developing Mathics3 Python Code
=========================================

We encourage people to work with the Python source code, modify it in ``git`` and put in Pull Requests when there is something you want to share with other Mathics3 users.

For this, you'll need to have ``git`` installed as well as a GitHub account to submit a pull request (PR) when done.

Github repositories are listed in :ref:`Install from the Mathics3 Github Organization`.

Developer Python Code-Checking Packages
---------------------------------------

There are a number of additional Python-related packages you will probably want to have to reduce inadvertent mistakes and keep the code consistent with its existing style. These are:


* `isort <https://pypi.org/project/isort/>`_: sorts Python imports
* `black <https://pypi.org/project/black/>`_: formats Python code according to standard Python-formatting conversions.

When you commit code, you can arrange to have these tools run automatically and fix up mistakes using a package called `pre-commit <https://pypi.org/project/pre-commit/>`_.

After running ``pip install pre-commit`` then run ``pre-commit install``.

Optional but Useful Developer Python Packages
---------------------------------------------

Other Python packages that are nice to have but are not strictly necessary are:

* `mypy <https://mypy.readthedocs.io/en/stable/>`_:  static type checker for Python
* `flake8 <https://pypi.org/project/flake8/>`_: code checker for Python
* `pylint <https://pypi.org/project/pylint/>`_:  code analyzer for Python

.. TODO: add section about putting in PRs
