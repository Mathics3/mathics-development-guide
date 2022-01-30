.. index:: evaluation

.. contents::

===========================
Evaluation of an Expression
===========================

Overview
========

In contrast to the simplicity and regularity for representing the data
for ``Expression``, *evaluation* of this data or expression is more involved
than conventional programming languages. I suppose this is to be expected.

Part of the complexity in evaluating an expression involves:

* how Python methods and values are bound to symbol literals
* how the expression is pattern matched and rewritten based on symbol
  values and rules that can be dynamically changing; term rewriting
  can take into account the current types of variables or bound
  symbols
* how to select the method to dispatch for a Mathics function call and how
  parameter values are assigned after term rewriting and symbol binding is done
* how we determine when the evaluation of an expression is complete

If you have programmed in WL and have an understanding of the
complexities involved in WL evaluation, aside from the Python-syntax
and conventions used here, the evaluation process of this may seem
familiar. The conventions that this program uses will be new.
This part is custom to this program.

If however you are instead not familiar with WL, but very familiar
with Python or similar languages, a lot of this may seem
mysterious. Functions don't get called using a traditional way where
you create an object like ``Number()`` and then instantiate a method
on that, like ``+``, ``__plus__()``, or even ``Times()``.

Instead all Function calls are triggered through an evaluation method
which involves the concept of `rewriting
<https://en.wikipedia.org/wiki/Rewriting>`_. This alone can obscure
what gets called. There Mathics function ``TraceEvaluation[]`` can
help in understanding the subexpressions that are computed in evaluation.

And as mentioned above, aside from this, the behavior is encoded in
Mathics' Python code using conventions uniquely defined in this
system. Built-in Functions are special methods in classes derived from
a Bulltin class.  Furthermore they must have names that start out
``apply`` and must have docstrings that contain WL patterns that
indicate when the method matches. More on this is described later.


Evaluation can leave an S-Expression Unchanged
==============================================

If you've used Mathics and misspelled a builtin function name or
called a function with the wrong number of parameters, you might find
it odd that sometimes you won't get an error message but just the same
thing back. Or what you might type might be coorect and and complete
expression ```myvariable`` or ``Pi`` can get the same thing back.

This isn't a bug, but a feature of the design of the language.

In the case of ``myvariable`` the language detects this as a symbol
and symbols do not need to be declared in advance of their use.

When you type ``Pi`` all by itself, unless a numeric approximation of
that was requested, ``Pi`` refers to its symbol value. The
S-expression entered is exactly the same. A later step may decide to
materialize a value or convert the representation of ``Pi`` into a
unicode string.

And when an S-expression doesn't match a particlar form for a function
call, the S-expression *needs* to be left unchanged: the act of not
matching a particular function in of itself isn't an error because
there may be some other rule around, maybe even at a different level
of the Expression Tree which will match.



Apply/Evaluate Process
======================

Expression evaluation is an iterative and recursive tranformation process where we apply transformation rules and function application
until the resulting expression that comes back doesn't change, or we are told to stop, e.g. an error or limit was encountered.

Here we give in broad outline a single apply/evaluate step of this
process. See also `The Standard Evaluation Sequence
<https://reference.wolfram.com/language/tutorial/Evaluation.html>`_.


Gather information from ``Head`` and gather its leaves
------------------------------------------------------

This is done using these attributes in ``Head``:

* ``HoldFirst``,
* ``HoldAll``,
* ``HoldRest``

and using the following subexpressions may appear in the expression:

* ``Evaluate[]``
* ``Unevaluated[]``

At the end of this, variables ``head``, ``attributes`` (of head), and ``leaves`` (of the expression) are set.

Build a new Expression
-----------------------

Build a new expression with using variables ``head`` and ``leaves`` based
the attribute settings in variable ``attributes`` from previous step,

This substeps here are:

* Try to flatten sequences in the expression unless the ``SequenceHold`` or ``HoldAllComplete`` attributes are set in ``Head``
* Change ``Unevaluated[expr]`` to ``expr`` but mark the expression as being unevaluated
* Flatten extpressions involving nested functions if the ``Flat`` attribute was found in ``Head``
* Sort leaves if the ``Orderless`` attribute was found in ``Head``

Compute evaluation timestamp
----------------------------

Compute timestamp in a expression cache. This may lead to invalidation and rebuild the expression cache elsewhere.

Search for a Rule in ``Head`` to apply
--------------------------------------

Search for a rule in ``Head`` that matches the expression

Apply Rule or restore Expression
--------------------------------

If a rule was found, apply it getting back an evaluated expression.
If the expression is unchanged, restore it to its state before building a new expression,
and reset the evaluation cache to its value before updating.



Mathics Function Application
============================

.. index:: Symbol, Predefined, Builtin, Expression

The first leaf, called the "head" (or ``Head[]``) of an
``Expression`` is a ``Symbol``.

When there are other leaves, the head is assumed to be a Mathics
function call, where  the function name comes from the head. If this is a
built-in function, like ``Plus``, the Mathics function name is the name
of a Python class derived ultimately from ``Builtin``. These
Mathics function-like classes are described in later sections.

As described in the previous section, before invoking that Mathics
function, we need to check for a rewrite rule that applies to
the Mathics function call. If a rule is found, it will have attached to
a bound method name starts with ``apply``.

These rules get created on loading the module containing a subclass of
``Builtin`` implementing some Mathcs Primative Funtion.  The rules
come from the docstrings of a methods that start with ``apply``.

The docsting includes not only a pattern to match on but how the
parameters should get bound when applying the function.
instance of an ``Evaluation`` is also supplied as a parameter in the call.

There is a degenerate situation though where there is no rule
rewriting, or apply methods involved. Here the instance method's
*evaluate()* method is called. This is used when a function has no
parameters or arguments. This kind of thing happens when a constant or
variable name is used; here the variable name is prefaced with a
``$``. Examples are ``$VersionNumber`` or ``$MachineName``.

As we go along, we'll describe other conventions that are used that
are crucial in getting the interpreter work properly. But for now,
when writing a new Builtin Function, just remember that unless there
is an ``evaluate()`` method, there is a method name in a Mathics
function class that begins with ``apply``, and its docstring is used
to figure out whether the leaves of the list are applicable to that
function.

Here is an example for the `Environment
<https://reference.wolfram.com/language/ref/Environment.html>`_
primitive taken from the code

.. code-block:: python

   class Environment(Builtin):

   def apply(self, var, evaluation):
       """Environment[var_?StringQ]"""
   ...

The ``apply()`` function above will get called when finding a
``Expression`` whose ``Head`` value is ``Environment`` and it has one
leaf or parameter which which we will call ``var``.  That leaf or
parameter should also much be a ``String`` object.

For more information describing Mathics function signatures that are
used in the ``apply`` method's docstring , see `Functions and Programs
<https://reference.wolfram.com/language/tutorial/FunctionsAndPrograms.html>`_
and `Patterns
<https://reference.wolfram.com/language/tutorial/Patterns.html>`_.

One useful Mathics function that is useful in debugging pattern matching is  `Cases <https://reference.wolfram.com/language/ref/Cases.html>`_.

Built-in Function Name Descriptions
===================================

Online and printed documentation for builtin ``Environment`` comes from the docstring for ``class Environment`` if that exists.
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
========================================

Building on the code shown above for parsing an expression,
here is code to evaluate an expression from a string:

.. code-block:: python

   # The below is a repeat of the parsing code...

   from mathics.core.parser import parse, SingleLineFeeder
   from mathics.core.definitions import Definitions

   definitions = Definitions(add_builtin=True)
   str_expression = "1 + 2 / 3"
   expr = parse(definitions, SingleLineFeeder(str_expression))

   # This code is new...

   from mathics.core.evaluation import Evaluation
   evaluation = Evaluation(definitions=definitions, catch_interrupt=False)
   last_result = expr.evaluate(evaluation)

   print("type", type(last_result))
   print("expr: ", last_result)

Running the above produces:

::

   type <class 'mathics.core.expression.Rational'>
   expr:  5/3

All of the above is wrapped nicely in the module ``mathics.session`` which
performs the above. So here is an equivalent program:

.. code-block:: python

    from mathics.session import session
    str_expression = "1 + 2 / 3"
    result = session.evaluate(str_expression)
