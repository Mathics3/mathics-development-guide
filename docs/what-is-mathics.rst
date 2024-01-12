The Components of Mathics3
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. contents::
   :depth: 2
   :local:


At one time, there was a single Python PyPI installable package that
made up this open-source version of the Wolfram language. It included for example a Django-based front end.

However in order to facilitate using the parts of it in other projects
or the parts you need, the original package and github repositories have has been broken up into separately
installable packages, and separate github repositories. These reposities are now under the Mathics3 github organization. (The old organization and github repositories are around, but you will find no development there.)

Splitting up into packages reduces the dependencies needed for many of the individual components: when
you only need part of Mathics3 you don't needed to the code or
dependencies for parts you don't want. For example, if you might not need the Django-based front end; perhaps you do everything from a command line interface. If that is the case, then you don't need to install Django or MySQL which Django uses in our implementation to save worksheet data.

On the other hand, if you only interested  the Django interface and will never used the command-line interface, then you don't need the the mathicsscript package and the python terminal packages that pulls in.

Natural-Language Processing (NLP) is a separate Mathics3 module; it requires OS package support and word lists that you might not have installed, and might not want to devote disk space for. Various Python interpreters cannot build the Python NLTK package.

However, if you do want everything, we have a separate package called `Mathics-omnibus <https://pypi.org/project/Mathics-omnibus/>`_ which pulls in all of the Mathics-related packages. As part of the `github project <https://github.com/Mathics3/mathics-omnibus>`_ is a docker setup.

Using this, you can use the full `Mathics3 suite via dockerhub <https://hub.docker.com/r/mathicsorg/mathics>`_ without having to build Mathics3 or have necessary OS libraries (including Python itself) outside of the docker containers.

The pieces are described next go into the individual Python-packages that make up the Mathics3 suite.


Mathics3 Core
+++++++++++++

The Mathics3 core contains a parser, and evaluator, and
some formatting routines.

Over time, formatting routines may be packaged separately

There is also a very rudimentary command-line shell called ``mathics``.


The Mathics3 core required for any work with Mathics3.

If you are developing a non-interactive application written in
Mathics3, you may no more than this.

Although we provide documentation `on-line
<https://mathics.org/docs/mathics-latest.pdf>`_, inside the `docker
image <https://hub.docker.com/r/mathicsorg/mathics>`_ , and
extractable from the that, should you want to build your own PDF,
you'll need to have various TeX packages installed.

Front ends Mathics-Django and mathicsscript use mathics core.

Mathics3 Character Tables and Tokenizer
+++++++++++++++++++++++++++++++++++++++

This is the tokeniser or scanner portion for the Wolfram Language.

As such, it also contains a full set of translation between Wolfram Language named characters, their Unicode/ASCII equivalents and code-points.

The scanner inside Mathics3 Core, but it can also be used for
tokenizing and formatting Wolfram Language code. In fact
mathics-pygments described in the next section uses this.

You can install this portion from `PyPI
<https://pypi.org/project/Mathics-Scanner/>`_. The github project is
`here <https://github.com/Mathics3/mathics-scanner>`_.

Mathics3 Syntax Highlighting
++++++++++++++++++++++++++++

There is a syntax highlighter called mathics-pygments_ which uses `Pygments <https://pygments.org>`_. It is
based on rsmenon's `pygments-mathematics
<https://pypi.org/project/pygments-mathematica/>`_.

The main difference between the two is that the character tables are
used here. Possibly over time more parts of the scanner will be used
as well.

Mathicsscript uses this package.



mathicsscript
+++++++++++++

The Mathics3 core comes with a very rudimentary command-line
shell, if you want fancier shell features such as:

* Prompt toolkit and GNU Readline terminal interaction. This includes
   - saving command history between sessions.
   - variable completion, even for symbol names like `\\[Sigma]`
   - limited ESC keyboard input; for example *esc* ``p`` *esc* is π
* Syntax highlighting using mathics-pygments_
* Automatic detection of light or dark `terminal background color <https://pypi.org/project/term-background/>`_.
* Entering and displaying Unicode symbols such as used for Pi or Rule arrows

There is a separately-installable PyPI package called `mathicsscript <https://pypi.org/project/mathicsscript/>`_.

Django-based GUI
++++++++++++++++

If you prefer, as many do, browser-based interaction with nicely
formatted graphics and MathML-formatted output, right now there is a
Django-based PyPI package `Mathics-Django
<https://pypi.org/project/Mathics-Django>`_.

Some of its features:

* Extensive online documentation and interactive documentation via Ajax
* Integrated graphics and MathML mathematics output via MathJax
* Notebook-like sessions

To use this, you will need Django 3.2.5 or later installed, and a
browser with JavaScript enabled.

Note: in the future we intend to also provide a Jupyter-like interface.

Mathics3 Python Modules
+++++++++++++++++++++++

A number of the add-ons are not automatically loaded when Mathics3 starts, instead can be loaded from within Mathics3 using the `Needs <https://reference.wolfram.com/language/ref/Needs.html>`_ function.

However the Python packages need to have been Python installed outside of Mathics3 first for this to work.

Below we describe some of these packages. A full list can be found by looking in the `Mathics3 organization <https://github.com/Mathics3>`_.

`"Hello, World" as a Mathics3 Python Module <https://github.com/Mathics3/pymathics-hello>`_
--------------------------------------------------------------------------------------------

This is a minimal Mathics3 Python Module for example or teaching purpose.

In contrast to the Mathics3 Python Modules, this one is not general useful except for showing how to write a Mathics3 Python Module.


`Natural Language Mathics3 Module <https://github.com/Mathics3/pymathics-language>`_
-------------------------------------------------------------------------------------

This Mathics3 Python Module adds Natural-Language Processing (NLP) functions.

To use this, you will need to have `nltk
<https://pypi.org/project/nltk>`_ and `spacy
<https://pypi.org/project/spacy>`_ installed.

`Network Graph Mathics3 Python Module <https://github.com/Mathics3/pymathics-graph>`_
--------------------------------------------------------------------------------------

This Mathics3 Python Modules adds Graph Theory or Networks Builtin Functions.

To use this you will need to have `networkx <https://pypi.org/project/networkx>`_ and `matplotlib <https://pypi.org/project/matplotlib>`_ installed.


`Matplotlib Python Module Backend Renderer <https://github.com/Mathics3/pymathics-matplotlib>`_
-----------------------------------------------------------------------------------------------

Currently this is a work in progress and works only in very limited way.
It provides graphics rendering using `matplotlib <https://pypi.org/project/matplotlib>`_.

`Asymptote Python Module Backend Renderer <https://github.com/Mathics3/pymathics-asy>`_
----------------------------------------------------------------------------------------

Currently this is a work in progress and works only in very limited way.
It provides graphics rendering using the `asymptote <https://asymptote.sourceforge.io/>`_ vector graphics language.

.. _mathics-pygments: https://pypi.org/project/mathics-pygments/
