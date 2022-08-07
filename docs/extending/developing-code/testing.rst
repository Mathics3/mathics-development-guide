Running Tests
=============

Tests come in the following kinds:

* unit tests via ``pytest``
* integration tests
* tests inside examples
* integration tests
* benchmark tests

Benchmark testing is a topic in of itself and we don't have things fully automated here.

To run the other tests though run:

::

    $ make test  # add option -j3 if you want to run in parallel


Unit tests
----------

To run unit tests:

::

   $ make pytest

This runs ``pytest``. If you want to run pytest directly and customize options you should do this by running ``pytest`` as a module:

::

   $ python -m pytest test # pytest options

Note if you are using ``pyston`` run this way or set the ``PYTHON`` environment variable to ``pyston`` before running ``make``.


Doctests
--------

Currently we have a homegrown version of `Sphinx autodoc <https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html>`__.
We hope to replace this someday with Sphinx autodoc. Until then, what we have is a little fragile and alas follows its own conventions.

During a test run, the results of tests can be stored for the documentation, both in MathML and LaTeX form, by executing

::

    $ python mathics/docpipeline.py -o

or

::

    make doc

You can then create the PDF using LaTeX. All required steps can be
executed by

::

    $ make latex

in the ``doc/tex`` directory, which uses ``latexmk`` to build the LaTeX
document. You just have to adjust the ``Makefile`` and ``latexmkrc`` to
your environment. You need the Asymptote to
generate the graphics in the documentation.


The version of the documentation, that is used by Django is run similarly from the Mathics Django repository.
interface, is updated immediately. To produce the LaTeX documentation
file, run:

You can also run the tests for individual built-in sections using

::

    $ python mathics/docpipeline.py -s [name]

The same thing can be done for chapters.

This will not re-create the corresponding documentation results,
however. You have to run a complete test to do that.

Dependencies
++++++++++++

The following packages are required to build the PDF documentation:

- ``texlive-font-utils``
- ``latexmk``
- ``texlive-xetex``
- ``lmodern``
- ``inkscape``
- ``texlive-latex-extra``
- ``texlive-latex``
- ``texlive-fonts-recommended``
- ``asymptote``

Those can be installed in Debian-based system with

::

    $ apt-get install texlive-font-utils latexmk texlive-xetex lmodern inkscape texlive-latex-extra texlive-latex texlive-fonts-recommended asymptote
