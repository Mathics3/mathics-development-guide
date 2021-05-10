.. index:: S-expression, AST
.. _ast:

AST, S-Expression, General List: same thing
============================================

The end-result of scanning and parsing is an S-expression, which is a
Python object of type ``Expression``. In compiler terminology the
S-expression is also called an *abstract syntax tree* or AST. The
first leaf of an ``Expression`` is called the "head".

When the ``Expression`` is to be evaluated, the head should a ``Symbol``.

In Mathics, there are only very few different kinds of
non-``Expression`` nodes, called "atoms" that can appear:

.. index:: Number, String, Symbol, Filename

* ``Number``
* ``String``
* ``Symbol``
* ``Filename``

With the exception of the addition of ``Filename`` these are
almost the same atoms described in `Basic Internal Architecture
<https://reference.wolfram.com/language/tutorial/TheInternalsOfTheWolframSystem.html#6608>`_
for WL.

Not listed above but found in the link is "general expressions": the
thing that glues everything together. In Mathics, I imagine this
corresponds to ``Expression``.

The class definitions for these are given in `mathics.core.parser.ast
<https://github.com/mathics/Mathics/tree/master/mathics/core/parser.ast>`_.

If you compare the above four AST types with other languages, you'll
find this is pretty sparse. For example, `Python's AST
<https://docs.python.org/3/library/ast.html>`_ has well over 30
different types.

So what's the difference? Python specializes AST types for different
kinds of programming language constructs, such as for loops,
conditional statements, exception blocks, different kinds of
expressions, and so on. In WL and Mathics, these are all simply
built-in functions.
