=================================
Mathics Core Interpreter Overview
=================================

At its heart, the Mathics interpreter works over `S-expressions
<https://en.wikipedia.org/wiki/S-expression>`_: combinations of nested
and/or sequenced lists, pretty much the same as simple Lisp
interpreters work. See also `Everything is an Expression
<https://reference.wolfram.com/language/tutorial/Expressions.html#4715>`_.

When you enter a string to Mathics there is a 3-step process:

* the string is parsed to FullForm
* The full form S-expression is interpreted
* The result, also an S-expression, is formatted to the kind of
  output desired

However each of the above steps can be involved, so we break these
down below

Scanning and Parsing
====================

All parsing routines are located in `mathics-core-parser <https://github.com/mathics/Mathics/tree/master/mathics/core/parser>`_.

See the ``README.md`` that appears in that directory for detailed information on how scanning and parsing works.

You won't find much on the scanner there. There are two passes made in
the scanner, a "pre-scan" in found in
`mathics-core-parser-prescanner
<https://github.com/mathics/Mathics/blob/master/mathics/core/parser/prescanner.py>`_
which converts some WL-specific character codes to character or long
names and the tokenizer after that which breaks up a string into
*tokens*, classifications of a sequence of characters, which is then
as the atoms on which the parser pattern matches on.

There is a bit written in ``README.md`` on parsing so we won't
describe that, but the main points are:

* The parser is recursive descent
* Because WL has a lot of operators an `Operator-precedence parser <https://en.wikipedia.org/wiki/Operator-precedence_parser#Precedence_climbing_method>`_ is used
* The result is an Full-form S-Expression, which is a translation of the input string. See `Expressions as Trees <https://reference.wolfram.com/language/tutorial/Expressions.html#14609>`_.

To see a translation of the Full-Form *input* the flag ``--full-form`` can be given to the command-line utilities ``mathics`` or ``mathicsscript``.

Here is an example:

::

   $ mathics --full-form

   Mathics 2.0.0dev
   ...
   Quit by pressing CONTROL-D

   In[1]:= 1 + 2 / 3
   System`Plus[1, System`Times[2, System`Power[3, -1]]]
   Out[1]= 5 / 3

Note that this is different from formatting the *output*:

::

   In[2]:= (x + 1) / 3
   System`Times[System`Plus[Global`x, 1], System`Power[3, -1]]
   Out[2]= (x + 1) / 3
   In[3]:= (x + 1) / 3 // FullForm
   System`FullForm[System`Times[System`Plus[Global`x, 1], System`Power[3, -1]]]
   Out[3]= Times[Rational[1, 3], Plus[1, x]]

Some things to notice:

* Parsing fully-qualifies names. So we have ``System`Times`` instead of
  ``Times``, even the FullForm output shows the simple name.
* Parsing removes parenthesis used for grouping capturing this
  instead by the function nesting order

Python Code for Parsing an String
---------------------------------

Inside Python, here is how you parse a string:

.. code-block:: python

   from mathics.core.parser import parse, SingleLineFeeder
   from mathics.core.definitions import Definitions

   definitions = Definitions(add_builtin=True)
   str_expression = "1 + 2 / 3"
   expr = parse(definitions, SingleLineFeeder(str_expression))
   print("type", type(expr))
   print("expr: ", expr)

Running the above produces:

::

   type <class 'mathics.core.expression.Expression'>
   expr:  System`Plus[1, System`Times[2, System`Power[3, -1]]]

The function ``SingleLineFeeder`` should be supplied by the front-end.
It reads input a line and a time and returns that back to the parser.


Evaluation of an Expression
===========================

Evaluation of the S-expression created by the parser is a bit more
complicated than some programming languages because method lookup uses
the function's signature using pattern matching. Also, there can be
rule-based term-rewriting which goes on in conjunction with method
lookup.

If you have programmed in WL, aside from the the Python-syntax and
conventions used here, a lot of this should seem familiar,

If however you are not familiar with WL, but very familiar with Python
or similar languages, a lot of this can seem very mysterious at first
because functions don't get called using a traditional way where you
create an object like ``Number()`` and then instantiate a method on
that, like ``+``, ``__plus__()``, or even ``Times()``.

Of course, since the underlying interpreter language *is* Python, this
does happen, but in a much more roundabout way.

The first thing to understand is that finding which Python method in
an Mathics ``System`List`` requires a bit of work, much like in Python when you write
``a.b()``: there is a method lookup in the ``a`` object for method
``b`` and that might come from a super class of ``a``.

Mathics and WL are not Object Oriented so there is no such class-hierarchy lookup.
However as mentioned above there is pattern matching going on.

The entire function invocation in Mathics comes from a ``System`List``. The first leaf
(or ``Head[]``) is the name of a function to call. The remaining
leaves are the parameters to give to that first leaf.  The combination
of function name and remaining leaves is pattern matched.

Inside a Mathics builtin function, represented as a Python object the
appropriate class, there are a number of conventions used. Python
objects are instrospected for properties that they have. In particular a function's
docstring, and methods, and class variables all influence invocation.

In particular the object instance method to that is called when the
Mathics function such as ``System.Times`` is a method name that starts
out with ``apply``.

The docstring of that method gives the function signature (or
"pattern" in WL terminology) that has to match in the list leaves for
it to be called.

Here is an example for the `Environment <https://reference.wolfram.com/language/ref/Environment.html>`_ primitive taken from the code

.. code-block:: python

   class Environment(Builtin):

   def apply(self, var, evaluation):
       "Environment[var_?StringQ]"
   ...

The ``apply()`` function above will get called when a ``System`List`` expression where its "head" value is "Environment" and
it has one parameter ``var`` which is a ``String`` object.

For more information functions with patterns see `Functions and
Programs
<https://reference.wolfram.com/language/tutorial/FunctionsAndPrograms.html>`_
and `Patterns <https://reference.wolfram.com/language/tutorial/Patterns.html>`_.

Online and printed documentation for builtin Environment comes from the docstring for ``class Environment`` if that exists.
In the example above, it was omitted. Here is what it looks like in the actual code.

.. code-block:: python

    class Environment(Builtin):
        """
        <dl>
          <dt>'Environment[$var$]'
          <dd>gives the value of an operating system environment variable.
        </dl>
        X> Environment["HOME"]
         = ...
        """

        def apply(self, var, evaluation):
        <dl>
          <dt>'Environment[$var$]'
          <dd>gives the value of an operating system environment variable.
        </dl>
        X> Environment["HOME"]
         = ...
	""""

The XML/HTML markup is used to format help nicely. "Documentation markup" elsewhere describes this markup.


Python Code for Evaluating an Expression
----------------------------------------

Building on the code shown above for parsing an expression,
here is code to evaluate an expression from a string:

.. code-block:: python

   # The below is a repeat of the parsing code...

   from mathics.core.parser import parse, SingleLineFeeder
   from mathics.core.definitions import Definitions

   definitions = Definitions(add_builtin=True)
   str_expression = "1 + 2 / 3"
   expr = parse(self.definitions, SingleLineFeeder(str_expression))

   # This code is new...

   evaluation = Evaluation(definitions=definitions, catch_interrupt=False)
   last_result = expr.evaluate(evaluation)

   print("type", type(last_result))
   print("expr: ", last_result)

All of the above is wrapped nicely in the module ``mathics.session`` which
performs the above. So here is an equivalent program:

.. code-block:: python

    from mathics.session import session
    result = session.evaluate(str_expression)


Object Classes
==============

To be continued...

Atom Class Attributes
---------------------

To be continued...

SympyFunction and _MPMathFunction
---------------------------------

Builtin and Predefined
----------------------

PrefixOperator and PostFixOperator
----------------------------------

BinaryOperator and UnaryOperator
--------------------------------

Operator
--------
