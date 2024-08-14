==============================
Making a Mathics3 Core Release
==============================

*Note: This package depends on ``mathics-scanner``, so if that needs a release too, do that before this.*

.. code::

    $ PACKAGE="Mathics3"
    $ github_top_dir="mathics-core"
    # Edit mathics/version.py
    $ source mathics/version.py # to set in POSIX shell
    $ echo $__version__

Workflows update?
=================

Check ``.github/workflows/*.yml`` to make see if we are using
github versions (of scanner) for testing. If so adjust.


Create a new branch
===================

.. code::

    $ git checkout -b release-$__version__
    $ git commit -m"Get ready for release $__version__" .

Update Changes
==============

.. code::

    $ make ChangeLog

Update ``CHANGES.rst`` from ``ChangeLog``

::

    $ make check
    $ git commit --amend .
    $ git push -u origin HEAD # get CI testing going early

Make Mathics3 PDF
=================

.. code::

   $ pyenv local 3.11 # or whatever latest Python you want to build doc with
   $ make clean # make sure mathics-title.pdf has not been removed
   $ make doc


Look at resulting PDF and colophon

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
    $ pyenv local pyston-2.3.5 # Use a version that is not the most recent
    $ pip install -e git+https://github.com/Mathics3/${github_top_dir}.git#egg=${PACKAGE}
    $ mathics --version # see that new version appears
    $ mathics -e "1+2"
    $ pip uninstall ${PACKAGE}
    $ popd

Make packages and check
=======================

::

    $ bash ./admin-tools/make-dist.sh
    $ twine check dist/Mathics3-$__version__*

Go over what is in dist and remove unnecessary files in ``dist``.

Release on Github
=================

Go to https://github.com/Mathics3/mathics-core/releases/new

https://cloudconvert.com/rst-to-md can be used to change the CHANGES.rst
section to markdown.

Now check the *tagged* release. (Checking the untagged release was
previously done).

TODO: turn this into a script in ``admin-tools``

.. code::

    $ git pull # to pull down new tag
    $ pushd /tmp/gittest
    $ pip install -e git+https://github.com/Mathics3/${github_top_dir}.git@${__version__}#egg=${PACKAGE}
    $ python -c 'import mathics_pygments; print(mathics_pygments.__version__)'
    $ pip uninstall ${PACKAGE}
    $ popd

Upload the release to PyPI
==========================

Upload it to PyPI with ``twine``:

.. code::

    $ twine upload --verbose dist/$PACKAGE-${__version__}*{whl,gz}

Move dist files to ``uploaded``
===============================

.. code::

    $ [[ ! -d dist/uploaded ]] || mkdir dist/uploaded
    $ mv -v dist/$PACKAGE*{whl,gz} dist/uploaded/


Post-Release
============

    Add 1 to release number of version in ``mathics/version.py``; also append "dev0".
