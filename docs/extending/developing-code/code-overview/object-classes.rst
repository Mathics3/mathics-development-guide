===============
 Object Classes
===============

The fundamental classes that functions are built up from are described
below.

Most of these classes are defined in `mathics.builtin.base
<https://github.com/mathics/Mathics/tree/master/mathics/builtin/base.py>`_
or `mathics.core.expression <https://github.com/mathics/Mathics/tree/master/mathics/core/expression.py>`_.

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

.. index:: Symbol

Symbol Class
============
.. index:: Symbol

Just above the ``Atom`` class is the ``Symbol`` which is an atomic element of an ``Expression``.
See `Atomic Elements of Expressions <https://reference.wolfram.com/language/guide/AtomicElementsOfExpressions.html>`_.

Symbols are like Lisp symbols: you can think of them as starting out as a string name. But in contrast to a string, once set the symbol is set, it is immutable and indivisable.

Builtin class
=============

A number of Mathics variables and functions are loaded when Mathics starts up,
thousands of functions even before any Mathics packages are loaded. As with other Mathics objects
like ``Atom`` and ``Symbol``, Mathics variables and functions are
implemented through Python classes.

The reason that we use a *class* for a Mathics variable or a Mathics
function is so that we can give those Mathics object properties and
attributes.

At the lowest level of the class hierarchy is ``Builtin``.

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
explicitly so we get ``Expressions``'s built-in ``evaluation()``
method.

A feature of the ``Builtin`` class is the convention that its provides
a convention by which "apply" methods of the class can be matched
using the method's name which must start with "apply" and a pattern
listed in the method's doc string. This is used in the example above.

Here, ``Head`` has one paramater which is called *expr*. Note that in
the Python method there is also *expr* variable it its method
signature which is listed right after the usual *self* method that you
find on all method functions.

At the end is an *evaluation* parameter and this contains definitions
and the context if the method needs to evaluate expressions.



.. index:: Predefined

Predefined Class
================

Just above ``Builtin`` in the Mathics object class hierarchy is
``Predefined``.

Some Mathics values like ``True`` are derived from ``Predefined``. For example:

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

.. index:: Builtin


.. index:: Operator

Operator
========

PrefixOperator and PostFixOperator
==================================

BinaryOperator and UnaryOperator
================================

SympyFunction and _MPMathFunction
=================================
