==============================
Making a MathicsScript Release
==============================


.. code:: bash

    $ PACKAGE="mathicsscript"
    # Edit ${PACKAGE}/version.py
    $ source ${PACKAGE}/version.py # to set in POSIX shell
    $ echo $__version__

Create a new Mathicsscript release branch
=========================================

.. code:: bash

    $ git checkout -b release-$__version__
    $ git commit -m"Get ready for release $__version__" .

Workflows update?
=================

Check ``.github/workflows/*.yml`` to make see if we are using
github versions for testing. If so adjust.


Update Changes
==============

.. code:: bash

    $ make ChangeLog

Update ``NEWS.md`` from ``ChangeLog``

::

    $ make check
    $ git commit --amend .
    $ git push -u origin HEAD # get CI testing going early

Check Python versions
======================

.. code:: bash

   $ ./admin-tools/check-versions.sh

Merge release
=============

Go to github and merge release into master.

Then...
.. code:: bash
::

    $ git checkout master
    $ git pull


Check package from github
=========================

TODO: turn this into a script in ``admin-tools``

.. code:: bash

    $ [[ ! -d /tmp/gittest ]] && mkdir /tmp/gittest; pushd /tmp/gittest
    $ pyenv local 3.9.18 # Use a version that is not the most recent
    $ pip install -e git+https://github.com/Mathics3/${PACKAGE}.git#egg=${PACKAGE}[full]
    $ mathicsscript --version # see that new version appears
    $ mathicsscript -e "1+2"
    $ mathicsscript  # Try it out with Sin[x, {x, 0, 2 Pi} and Graphics3D[Circle[{0,0,0}, 1]
    $ pip uninstall ${PACKAGE}
    $ popd

Make packages and check
=======================

::

    $ bash ./admin-tools/make-dist.sh
    $ twine check dist/${PACKAGE}-$__version__*

Go over what is in dist and remove unnecessary files in ``dist``.

Release on Mathicsscript on Github
==================================

Go to https://github.com/Mathics3/mathicsscript/releases/new

https://cloudconvert.com/rst-to-md can be used to change the CHANGES.rst
section to markdown.

Now check the *tagged* release. (Checking the untagged release was
previously done).

TODO: turn this into a script in ``admin-tools``

.. code:: bash

    $ git pull # to pull down new tag
    $ pushd /tmp/gittest
    $ pip install -e git+https://github.com/Mathics3/${PACKAGE}.git@${__version__}#egg=${PACKAGE}[full]
    $ mathicsscript --version # see version
    $ mathicsscript -c "1+2"
    $ mathicsscript  # Try it out with Sin[x, {x, 0, 2 Pi} and Graphics3D[Circle[{0,0,0}, 1]
    $ pip uninstall ${PACKAGE}
    $ popd

Upload the Mathicsscript release to PyPI
=========================================

Upload it to PyPI with ``twine``:

.. code:: bash

    $ twine upload --verbose dist/$PACKAGE-${__version__}*{whl,gz}

Move Mathicsscript dist files to uploaded
=========================================

.. code:: bash
    $ mv -v dist/$PACKAGE*{whl,gz} dist/uploaded/


Post Mathicsscript Release
==========================

    Bump version in ``${PACKAGE}/version.py``, and add "dev0".
