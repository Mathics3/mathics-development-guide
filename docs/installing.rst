.. index:: installing
.. _installing:

Installing Mathics
==================

Here we describe the various ways to get Mathics installed.

What makes up the full Mathics Suite?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mathics is broken up into a number of pieces in order to facilitate
using the parts of you desire. This can also reduce the vast number of
dependencies to those that you need and the footprint to run. The
pieces are described next with the component's OS and Python-package
dependencies.


Mathics Core
++++++++++++

The Mathics core is required for any work with Mathics.

If you are developing a non-interactive application written in
Mathics, you may no more than this.

Although we provide documentation `on-line
<https://mathics.org/docs/mathics-latest.pdf>`_, should you want to
build your own PDF, you'll need to have varous TeX packages installed.

mathicsscript
+++++++++++++

Tthe Mathics core comes with a very rudimentary command-line
shell called ``mathics``. However, if you want fancier shell features such as:

* GNU Readline terminal interaction. This includes
   - saving command history between sessions.
   - variable completion, even for symbol names like `\\[Sigma]`
   - limited ESC keyboard input; for example *esc* ``p`` *esc* is π
* Syntax highlighting using `pygments <https://pygments.org>`_.
* Automatic detection of light or dark `terminal background color <https://pypi.org/project/term-background/>`_.
* Entering and displaying Unicode symbols such as used for Pi or Rule arrows

there is a separately-installable PyPI package called `mathicsscript <https://pypi.org/project/mathicsscript/>`_

Django-based GUI
++++++++++++++++

If you prefer, as many do, browser-based interaction with nicly formatted graphics and MathML-formatted output,
right now there is a Django-based PyPI package `Mathics-Django <https://pypi.org/project/Mathics-Django>`_.

Some of its features:

* Extensive online documentation and interactive documentation via Ajax
* Integrated graphics and MathML mathematics output via MathJax
* Notebook-like sessions

To use this, you will need Django installed, and a browser with Javascript enabled.

Note: in the future we intend to also proved a Jupyter-like interface.

Natural Language Python Module add-on
+++++++++++++++++++++++++++++++++++++

If you want Natural-Language processing, there is an additional PyPI package called `pymathics-natlang <https://pypi.org/project/pymathics-natlang/>`_.

To use this, you will need to have `nltk <https://pypi.org/project/nltk>`_ and `spacy <https://pypi.org/project/spacy>`_ installed.

Graph Python Module add-on
+++++++++++++++++++++++++++

If you need to do work with Graph Theory or Networks you may want the Graph Python module called `pymathics-graph <https://pypi.org/project/pymathics-graph/>`_.

To use this you will need to have `networkx <https://pypi.org/project/networkx>`_ and `matplotlib <https://pypi.org/project/matplotlib>`_ installed.


Install from PyPI
~~~~~~~~~~~~~~~~~

Here is how you can install the full Mathics suites:
::

       $ pip install Mathics3  # this is the core engine
       $ pip install Mathics-Django # web front-end
       $ pip install mathicsscript  # the command-line interface
       $ pip install pymathics-natlang # the Natural-language Python module
       $ pip install pymathics-graph # the Python module for working with Graphs and Networks

Note the name is "Mathics3" for the most recent release. "Mathics" has
pre-Python 3 code.

See the previous sections for descriptions of the various pieces, what
features they add and what dependencies are needed to run them.

Above we explicitly install Mathics3, the core, although that isn't
strictly necessary: if you install one of the other PyPI packages, it
will pull in the Mathics3 core as a dependency.

Install from Conda-Forge
~~~~~~~~~~~~~~~~~~~~~~~~

See https://github.com/conda-forge/mathics3-feedstock.

From docker (dockerhub)
~~~~~~~~~~~~~~~~~~~~~~~

As an alternative to building all the components from source or via Python
package, you can run pre-built code for *all* of the components via
`docker <https://www.docker.com>`__. To download a copy of the docker
image run:

::

    $ docker pull mathicsorg/mathics

However you this step is also done implicitly if you just issue the
command to run the code. That invocation is given in the :ref:next section.

From an OS-specific Repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Click on the link below from `Repology.org <https://repology.org>`__ for
details for a specific OS and distribution:

|Packaging status|

Install from git from github
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

Below we give command-line instructions. There is also GitHub's git
client for your operating system (`Mac <http://mac.github.com/>`__;
`Windows <http://windows.github.com/>`__). For that, clone
mathics/Mathics (there is a button at the top of
https://github.com/mathics/Mathics that says "Clone in Mac" or "Clone in
Windows" depending on your platform).

.. code:: bash

    $ git clone https://github.com/mathics/Mathics.git
    $ cd Mathics
    $ make install

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
