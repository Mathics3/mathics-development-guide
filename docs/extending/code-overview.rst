=================================
Mathics Core Interpreter Overview
=================================

At its heart, the Mathics interpreter works over `S-expressions
<https://en.wikipedia.org/wiki/S-expression>`_: combinations of nested
and/or sequenced lists, pretty much the same as simple Lisp
interpreters work. See also `Everything is an Expression
<https://reference.wolfram.com/language/tutorial/Expressions.html#4715>`_.

When you enter a string to Mathics there is a 3-step process:

* the input string is parsed to ``FullForm``
* The ``FullForm`` S-expression is evaluated giving another S-expression
* The result is formatted to the kind of output desired. Formatting can cause additional evaluations to occurs

This is mentioned from the user perspective in the Figure `"Steps in
the operation of Wolfram Language"
<https://reference.wolfram.com/language/tutorial/TextualInputAndOutput.html#8971>`_

Each of the above steps can be involved, so we break these down below.

.. toctree::
   :maxdepth: 3

   code-overview/apply-eval-format
   code-overview/scanning-and-parsing
   code-overview/ast
   code-overview/evaluation
   code-overview/pattern-matching
   code-overview/boxes-forms-and-formats
   code-overview/object-classes
