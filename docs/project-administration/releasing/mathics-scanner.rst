=================================
Making a Mathics-Scanner Release
=================================

.. code::


    $ package="mathics_scanner"
    $ PACKAGE="Mathics-Scanner"
    # Edit ${package}/version.py
    $ source ${package}/version.py # to set in POSIX shell
    $ echo $__version__

Create a new branch
===================

.. code:: bash

    $ git checkout -b release-$__version__
    $ git commit -m"Get ready for release $__version__" .

Update Changes
==============

.. code:: bash

    $ make ChangeLog

Update ``CHANGES.rst`` from ``ChangeLog``

::

    $ make check
    $ git commit --amend .
    $ git push -u origin HEAD # get CI testing going early

Check Python versions
======================

.. code::

   $ ./admin-tools/check-versions.sh

Build Docs
==========

.. code::

    $ make doc

See also [[Documentation and tests]].

Merge release
=============

Go to github and merge release into master.

Then...
.. code::

    $ git checkout master
    $ git pull


Check package from github
=========================

TODO: turn this into a script in ``admin-tools``

.. code:: bash

    $ [[ ! -d /tmp/gittest ]] && mkdir /tmp/gittest; pushd /tmp/gittest
    $ pyenv local pyston-2.3.4 # Use a version that is not the most recent
    $ pip install -e git+https://github.com/Mathics3/${PACKAGE}.git#egg=${package}[full]
    $ mathics-generate-json-table --version # See new verison appear
    $ pip uninstall ${PACKAGE}
    $ popd

Make packages and check
=======================

::

    $ ./admin-tools/make-dist.sh
    $ twine check dist/Mathics_Scanner-$__version__*
    $ pip install dist/$package-$__version__*.whl

Go over what is in dist and remove unnecessary files in ``dist``.

Release on Github
=================

Go to https://github.com/Mathics3/mathics-scanner/releases/new

https://cloudconvert.com/rst-to-md can be used to change the CHANGES.rst
section to markdown.

Now check the *tagged* release. (Checking the untagged release was
previously done).

TODO: turn this into a script in ``admin-tools``

.. code::

    $ git pull # to pull down new tag
    $ pushd /tmp/gittest
    $ pip install -e git+https://github.com/Mathics3/${PACKAGE}.git@${__version__}#egg=${package}[full]
    $ mathics-generate-json-table --version # See new verison appear
    $ pip uninstall ${PACKAGE}
    $ popd

Upload the release to PyPI
==========================

Upload it to PyPI with ``twine``:

.. code::

    $ twine upload --verbose dist/Mathics_Scanner-${__version__}*{whl,gz}

Move dist files to save
========================

.. code::

    $ mv -v dist/Mathics_Scanner*{whl,gz,egg} dist/uploaded/


Post-Release
============

    Bump version in ``${package}/version.py``, and add ``dev0``.
