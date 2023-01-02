===============
Python Modules
===============

The fundamental python modules that make up Mathics-core are described
below.

Most of these classes are defined in `mathics.builtin.base
<https://github.com/mathics/Mathics/tree/master/mathics/builtin/base.py>`_
or `mathics.core.expression <https://github.com/mathics/Mathics/tree/master/mathics/core/expression.py>`_.

``mathics.core``
================

This is the core of the ``mathics-core`` package.

Here you find the the lowest, most fundamental modules and classes.

Objects here are fundamental to the system. These include objects like
``Symbols``, ``Numbers``, ``Rational``, ``Expressions``, ``Patterns``
and ``Rules``, to name a few.

While some parts of ``mathics-core`` could conceivably be written in
Mathics, but are instead written in Python for efficiency, everything
here pretty much has to written in Python.

``mathics.core.convert``
------------------------

Routines here convert between various internal representations such as
between ``Expressions``, LLVM functions, SymPy Arguments, MPMath
datattypes and so on. However this does not include the inital
conversion a parsed string into one of the internal
representations. That is done in the parser.

``mathics.core.parser``
------------------------

This module contains routines that takes tokens from the scanner (in a
separate module and repository) and parses this into some sort of
M-Expression as its AST (Abstract Syntax Tree).

There is a separate `README
<https://github.com/Mathics3/mathics-core/blob/master/mathics/core/parser/README.md>`_
for decribing how this works.


``mathics.eval``
================

Mathics3 Evaluation Functions

Routines here are core operations or functions that implement evaluation. If there
were an instruction interpreter, these would be the instructions.

These operatations then should include the most commonly-used Builtin-functions like
``N[]`` and routines in support of performing those evaluation operations/instructions.

Performance of the operations here can be important for overall interpreter performance.

It may be even be that some of the functions here should be written in faster
language like C, Cython, or Rust.


``mathics.builtin``
====================

Mathics3 Builtin Functions and  Variables.

Mathics3 has over a thousand Built-in Functions and variables, all of
which are defined here.

Note that there are other modules to collect specific aspects a
Builtin, such as ``mathics.eval`` for evaluation specifics, or
``mathics.format`` for rendering details, or ``mathics.compile`` for
compilation details.

What remains here is then mostly the top-level definition of a Mathics
Builtin, and attributes that have not been segregated elsewhere such
as has been done for one of the other modules listed above.

A Mathics3 Builtin is implemented one of a particular kind of Python
class.  Within these classes class variables give properties of the
builtin class such as the Builtin's Attributes, it Information text,
among other things.


``mathics.compile``
===================

xoMathics3 ``Compile`` implementation.

Here we have routines for compiling Mathics3 code.

At present, we use LLVM for this.


``mathics.doc``
===============

Module for handling Mathics-style documentation.

Right now this covers common LaTeX/PDF and routines common to
Mathics3 Django. When this code is moved out, perhaps it will
include the Mathics3 Django-specific piece.
Mathics' home-grown documentation system.
