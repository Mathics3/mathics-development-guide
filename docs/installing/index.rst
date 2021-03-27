.. toctree::
   :maxdepth: 3
   :caption: Contents:

   what-is-mathics

Installing Mathics
==================

Here we describe the various ways to get Mathics installed.

.. toctree::
   :maxdepth: 2


Install from PyPI
~~~~~~~~~~~~~~~~~

Here is how you can install the full Mathics suites:
::

       $ pip install Mathics-omnibus


This package doesn't have any code in it. Instead it just contains dependencies to other PyPI Mathics packages.of other PyPI package.
It is more or less equivalent to:


::
       $ pip install Mathics3  # this is the core engine. It is a dependency of some of the below too
       $ pip install Mathics-Django # web front-end
       $ pip install mathicsscript  # the command-line interface
       $ pip install pymathics-natlang # the Natural-language Python module
       $ pip install pymathics-graph # the Python module for working with Graphs and Networks

Note the name is "Mathics3" for the most recent release. "Mathics" has
pre-Python 3 code.

See the previous sections for descriptions of the various pieces, what
features they add and what dependencies are needed to run them.

Install from Conda-Forge
~~~~~~~~~~~~~~~~~~~~~~~~

See https://github.com/conda-forge/mathics3-feedstock.

:emphasis:`At present, the Conda Forge Mathics release is for an older version.`

From docker (dockerhub)
~~~~~~~~~~~~~~~~~~~~~~~

As an alternative to building all the components from source or via Python
package, you can run pre-built code for *all* of the components via
`docker <https://www.docker.com>`__. To download a copy of the docker
image run:

::

    $ docker pull mathicsorg/mathics

This will pull the latest development release that has a docker
tagname ``#latest`` if you want a stable release, give the version in
the pull command. For example

    $ docker pull mathicsorg/mathics#2.0.0

From an OS-specific Repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Click on the link below from `Repology.org <https://repology.org>`__ for
details for a specific OS and distribution:

|Packaging status|

Install from git from github
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you need the most recent fixes, you can install from github.  Note
that there isn't a single github repository that contains everything.

Also, since Mathics is in constant flux, dependencies can change. The
development version from might require development version from
another.

These instructions then aren't complete and may need to be adapted for
the various Mathics3 github repositories


Requirements
++++++++++++

Mathics runs on Python 3.6 or later. We also support PyPy 3.6 or later.

Underneath, Mathics relies on
`sympy <https://www.sympy.org/en/index.html>`__ which relies on
`numpy <https://numpy.org>`__. These and the other requirements will be
installed automatically if you use the standard Python installer
`pip <https://pip.pypa.io/en/stable/>`_. They are also listed in
`setup.py <https://github.com/mathics/Mathics/blob/master/setup.py>`__.


Several additional dependencies over what is described above if you want
to:

-  build the documentation (which needs ``xetex``, etc.)
-  do full testing (which needs pytest, etc.)
-  run the command-line interface
-  run the Django 3.1 webserver (which needs SQLite, etc.) \`

Below we give command-line instructions for most of the core packages. We don't
include the numer


There is also GitHub's git
client for your operating system (`Mac <http://mac.github.com/>`__;
`Windows <http://windows.github.com/>`__). For that, clone
mathics/Mathics (there is a button at the top of
https://github.com/mathics/Mathics that says "Clone in Mac" or "Clone in
Windows" depending on your platform).

.. code:: bash

    $ git clone https://github.com/Mathics3/mathics-scanner.git
    $ cd mathics-scanner
    $ make install

    $ cd ..
    $ git clone https://github.com/mathics/Mathics.git
    $ cd Mathics
    $ make install

    $ cd ..
    $ git clone https://github.com/Mathics3/mathics-django.git
    $ cd mathics3-django
    $ make install

    $ cd ..
    $ git clone https://github.com/Mathics3/mathicsscript.git
    $ cd mathicsscript
    $ make install

The above doesn't include PyMathics modules, but each of those are installed in like fashion.


Alternatively use ``make develop`` or ``pip install -e`` to run the code
installed from where the source-code is checked out. In doing this, code
changes in the source tree are reflected immediately when you rerun.

Of course, you may not want this, but instead want to run from a copy of
the last stable code, so that's what ``make install`` does.

OS-dependent packages
~~~~~~~~~~~~~~~~~~~~~

For the installation above you may need OS-specific packages.

For Debian/Ubuntu based systems:

::

    $ apt-get install python-dev libsqlite3-devp python-setuptools

as super-user, i.e. either after having issued ``su`` or by preceding
the command with ``sudo``).

On Mac OS X:

::

    $ brew install sqlite3

On FreeBSD:

::

    $ sudo pkg install math/py-mathics

.. |Packaging status| image:: https://repology.org/badge/vertical-allrepos/mathics.svg
			    :target: https://repology.org/project/mathics/versions
