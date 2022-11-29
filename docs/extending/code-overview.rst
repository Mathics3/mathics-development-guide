=================================
Mathics Core Interpreter Overview
=================================

.. index:: S-expression

At its heart, the Mathics interpreter works over a generalization of
an `S-expression <https://en.wikipedia.org/wiki/S-expression>`_,
called an `M-expresssion
<https://en.wikipedia.org/wiki/M-expression>`_. An M-expression is a
nested and/or sequenced lists, pretty much the same as simple Lisp
interpreters work, except the head element can be an expression rather
than just a simple function name. See also `Everything is an
Expression
<https://reference.wolfram.com/language/tutorial/Expressions.html#4715>`_.

When you enter a string to Mathics there is a 3-step process:

* the input string is parsed to ``FullForm``
* The ``FullForm`` M-expression is evaluated giving another M-expression
* The result is formatted to the kind of output desired. Formatting can cause additional evaluations to occurs

This is mentioned from the user perspective in the Figure `"Steps in
the operation of Wolfram Language"
<https://reference.wolfram.com/language/tutorial/TextualInputAndOutput.html#8971>`_

Each of the above steps can be involved, so we break these down below.

.. toctree::
   :maxdepth: 3

   code-overview/session
   code-overview/scanning-and-parsing
   code-overview/ast
   code-overview/evaluation
   code-overview/pattern-matching
   code-overview/boxes-forms-and-formats
   code-overview/python-modules
   code-overview/object-classes
   code-overview/glossary
