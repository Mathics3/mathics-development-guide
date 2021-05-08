.. index:: evaluation
.. _evaluation:

=============================
 Evaluation of an Expression
=============================

In contrast to the simplicity and regularity for representing the data
for ``Expression``, *evaluation* of this data or expression is more involved
than conventional programming languages. I suppose this is to be expected.

Part of the complexity involves the way function method lookup works
by pattern matching the expression. Also, there can be rule-based
term-rewriting which goes on in conjunction with method lookup.

If you have programmed in WL, aside from the Python-syntax and
conventions used here, a lot of this should seem familiar,

If however you are not familiar with WL, but very familiar with Python
or similar languages, a lot of this can seem very mysterious at first:
functions don't get called using a traditional way where you create an
object like ``Number()`` and then instantiate a method on that, like
``+``, ``__plus__()``, or even ``Times()``.

Of course, since the underlying interpreter language *is* Python,
Python object creation and method lookup on that does happen. But it
happens in a much more roundabout way using methods off of an object
such as an *evaluate()* method or the various *apply()* methods in
conjuction with the apply method's doc string. More on this is
described later.

For Python and Object-Oriented programmers, as an analogy for the
complexity and indirectness, an Object-Oriented "method dispatch" is
analogous. In Python or any Object-Oriented programming language, when
you write ``a.b()``: there is a method lookup in the ``a`` object, so
*at runtime* the type of ``a`` has to be inspected. And after having
that, the method handle ``b`` needs to be computed. And this comes
from a class heirarchy.

Mathics and WL are not Object Oriented, so there is no such
class-hierarchy lookup.  Instead, as mentioned above, pattern matching
is used to decide which method of the object to call.

Function Name to Python method lookup
=====================================

.. index:: Symbol, Predefined, Builtin, Expression

When an ``Expression`` has not been rewritten, the entire function
invocation in Mathics comes from the first leaf (or ``Head[]``) which
should be a ``Symbol``. In Python this will be a class some sort, such
as ``Builtin`` or ``Predefined`` or ``SympyFunction`` or a methe
derived from one of these. These classes are described in a later
section.

The remaining leaves of the ``Expression`` are the parameters to give
to an ``apply`` method.

In the simplest case, the *evaluate()* method is called. This is
used when a function has no parameters or arguments. In other words,
it looks like a constant or variable name, and usually is prefaced
with a ``$``. Examples here are ``$VersionNumber`` or ``$MachineName``.

When a function takes parameters it method's Object class is derived
either directly indirectly from the ``Builtin`` class rather than the
``Predefine`` class. To figure out which ``apply`` method in the class
object to call, each method's document string (or docstring) is
consulted. The lookup process is kicked off using the ``evaluate()``
method found in the ``Predefined`` class.

As we go along, we'll describe other conventions that are used that
are crucial in getting the interpreter work properly. But for now,
just remember that unless there is an ``evaluate()`` method, there is
a method name in a Mathics function class that begins with ``apply``,
and its docstring is used to figure out whether the leaves of the list
are applicable to that function.

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

Function Name Descriptions
==========================

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


===============
 Object Classes
===============

The fundamental classes that functions are built up from are described
below. Most of these classes are defined in `mathics.builtin.base
<https://github.com/mathics/Mathics/tree/master/mathics/builtin/base>`_.

.. index:: Atom

Atom Class
==========

Recall that an Expression to be evaluated is kind of S-expression
called and ``ExpressionList``, where each list item is either itself
an ``ExpressionList`` or an object in a class derived from ``Atom``.

The ``Atom`` class we encountered earlier when describing the nodes
that get created intially from a parse. However there are a few other
kinds of Atoms or fundamention objects that can appear in an
Evaluation list. These are

* ``CompiledCode``
* ``Image``

.. index:: Builtin, Predefined

Symbol Class
============
.. index:: Symbol

Just above the ``Atom`` class is the ``Symbol`` which is an atomic element of an ``Expression``.
See `Atomic Elements of Expressions <https://reference.wolfram.com/language/guide/AtomicElementsOfExpressions.html>`_.

Symbols are like Lisp symbols: you can think of them as starting out as a string name. But in contrast to a string, once set the symbol is set, it is immutable and indivisable.


Predefined class
================

A number of variables and functions are loaded when Mathics starts up,
even before any packages are loaded. As with other Mathics objects,
variables and functions are implemented through Python classes.

The reason that we use a *class* for a Mathics variable or a Mathics
function is so that we can give those Mathics object properties and
attributes.

At the lowest level of the class hierarch is ``Builtin`` from which
``Predefined`` is derived.

An object created with ``Predefined`` does not have leaves.

Some Mathics values like ``True`` are derived directly
from ``Predefined``. For example:

.. code:: python

    class True_(Predefined):
        """
        <dl>
          <dt>'True'
          <dd>represents the Boolean true value.
        </dl>
        """

        name = "True"

In the above, note that the class name has an underscore (``_``)
appended it. We do this so as not to conflict with the Python value ``True``. The
class variable ``name`` is used to associate the Mathics name.

A number of Mathics variables like ``$ByteOrdering`` are also derived
directly from the ``Predefined`` class. Since Python class names
cannot start with a dollar sign (``$``), we drop off the leading
``$``, in the class name, and that gives us: ``ByteOrdering``.

As with the ``True`` example shown above, the Mathics name is set
using class variable ``name`` defined in the ``ByteOrdering``
class. For example:

.. code:: python

   class ByteOrdering(Predefined):
      """
      <dl>
        <dt>'$ByteOrdering'
        <dd>returns the native ordering of bytes in binary data on your computer system.
      </dl>
      """
      name = "$ByteOrdering"

    def evaluate(self, evaluation) -> Integer:
        return Integer(1 if sys.byteorder == "big" else -1)


The ``evaluate()`` function above is called to get the value of variable ``$ByteOrdering``.

A feature of the ``Predefined`` class is the convention that its
default ``evaluation()`` method looks at the docstring of its methods that start
out with ``applied`` in order to figure out which method to call. We will
see an example of this next when describing the ``Builtin`` class.


Builtin class
=============

Mathics has over thousand built-in functions. Except the few that are
derived from ``Predefined``, the rest are derived directly or
indirectly from ``Builtin``.

Lets look at a simple one:

.. code:: python

    class Head(Builtin):
        """
        <dl>
        <dt>'Head[$expr$]'
            <dd>returns the head of the expression or atom $expr$.
        </dl>

        >> Head[a * b]
         = Times
        >> Head[6]
         = Integer
        >> Head[x]
         = Symbol
        """

        def apply(self, expr, evaluation):
            "Head[expr_]"

            return expr.get_head()

In the above, we have not defined an ``evaluation()`` method
explicitly so we get ``Predfined``'s built-in ``evaluation()``
method. What that does is look for the methods that start ``apply``
and it looks at its docstring to get the Mathics Form which to match
on for the apply method to call, and the arguments to pass it.

For ``Head`` above, we see that it has one paramater which is called
*expr*. Note that in the Python method there is also *expr* variable
it its method signature which is listed right after the usual *self*
method that you find on all method functions.

At the end is an *evaluation* parameter and this contains definitions
and the context if the method needs to evaluate expressions.

.. index:: Operator

Operator
========

PrefixOperator and PostFixOperator
==================================

BinaryOperator and UnaryOperator
================================

SympyFunction and _MPMathFunction
=================================
