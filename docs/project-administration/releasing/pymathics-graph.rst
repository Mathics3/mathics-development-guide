=====================================
Making a Mathic3 Graph Module Release
=====================================


.. code::

    $ PACKAGE="pymathics-graph"
    $ package="pymathics/graph"
    # Edit ${package}/version.py
    $ source ${package}/version.py # to set in POSIX shell
    $ echo $__version__

Create a new branch
===================

.. code::

    $ git checkout -b release-$__version__
    $ git commit -m"Get ready for release $__version__" .

Workflows update?
=================

Check ``.github/workflows/*.yml`` to make see if we are using
github versions for testing. If so adjust.


Update Changes
==============

.. code::

    $ make ChangeLog

Update ``NEWS.md`` from ``ChangeLog``

::

    $ make check
    $ git commit --amend .
    $ git push -u origin HEAD # get CI testing going early

Check Python versions
======================

.. code::

   $ ./admin-tools/check-versions.sh

Merge release
=============

Go to github and merge release into master.

Then...
.. code::
::

    $ git checkout master
    $ git pull


Check package from github
=========================

TODO: turn this into a script in ``admin-tools``

.. code::

    $ [[ ! -d /tmp/gittest ]] && mkdir /tmp/gittest; pushd /tmp/gittest
    $ pyenv local 3.9.18 # Use a version that is not the most recent
    $ pip install -e git+https://github.com/Mathics3/${PACKAGE}.git#egg=${PACKAGE}[full]
    $ mathics -e 'LoadModule["pymathics.graph"]; g = Pymathics`Graph[{1 -> 2, 2 -> 3, 3 <-> 4}, VertexLabels->True]; Pymathics`WeaklyConnectedComponents[g]'
    $ pip uninstall ${PACKAGE}
    $ popd

Make packages and check
=======================

::

    $ bash ./admin-tools/make-dist.sh
    $ twine check dist/*-$__version__*

Go over what is in dist and remove unnecessary files in ``dist``.

Release on Github
=================

Go to https://github.com/Mathics3/pymathics-graph/releases/new

https://cloudconvert.com/rst-to-md can be used to change the CHANGES.rst
section to markdown.

Now check the *tagged* release. (Checking the untagged release was
previously done).

TODO: turn this into a script in ``admin-tools``

.. code::

    $ git pull # to pull down new tag
    $ pushd /tmp/gittest
    $ pip install -e git+https://github.com/Mathics3/${PACKAGE}.git@${__version__}#egg=${PACKAGE}[full]
    $ mathics -e 'LoadModule["pymathics.graph"]; g = Pymathics`Graph[{1 -> 2, 2 -> 3, 3 <-> 4}, VertexLabels->True]; Pymathics`WeaklyConnectedComponents[g]'
    $ pip uninstall ${PACKAGE}
    $ popd

Upload the release to PyPI
==========================

Upload it to PyPI with ``twine``:

.. code:: bash

    $ twine upload --verbose dist/*-${__version__}*{whl,gz}

Move dist files to save
========================

.. code::
    $ mv -v dist/$PACKAGE*{whl,gz} dist/uploaded/


Post-Release
============

    Bump version in ``${PACKAGE}/version.py``, and add "dev0".
