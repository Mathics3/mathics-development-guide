===============
 Object Classes
===============

The fundamental classes that functions are built up from are described
below.

Most of these classes are defined in `mathics.builtin.base
<https://github.com/mathics/Mathics/tree/master/mathics/builtin/base.py>`_
or `mathics.core.expression <https://github.com/mathics/Mathics/tree/master/mathics/core/expression.py>`_.

The below are heuristics:

* To define a Mathics constant based on a Sympy constant, e.g. ``Infinity`` use ``SympyConstant``
* To define Mathics constants based on a mpmath constant, e.g. ``Glaisure``,
  use ``MPMathConstant``
* To define a Mathics constant based on a numpy constant, use ``NumpyConstant``
* To define a Mathics functions based on a Sympy function, e.g. ``Sqrt``, use ``SympyFunction``
* To define a Mathics operator use ``UnaryOperator``,
  ``PrefixOperator``, ``PostfixOperator``, or ``BinaryOperator`` depending on the
  type of operator that is being defined
* To define a Mathics function which returns a Boolean value e.g. ``MatchQ`` use ``Test``
* To define a Mathics function that doesn't fall into a category above, e.g. ``Attributes`` use ``Builtin``
* To define a Mathics variable e.g. ``$TimeZone`` or Mathics Symbols, e.g. ``True`` use ``Predefined``
* To define a Mathics atomic expression, e.g. ``ImageAtom`` use ``AtomicBuiltin``


.. index:: Atom, AtomQ

Atom Class
==========

Recall that an Expression to be evaluated is kind of M-expression
called and ``ExpressionList``, where each list item is either itself
an ``ExpressionList`` or an object in a class derived from ``Atom``.

The ``Atom`` class we encountered earlier when describing the nodes
that get created intially from a parse. Those were:

* ``Number``
* ``String``
* ``Symbol``
* ``Filename``


However there are a few other kinds of Atoms or fundamental objects
that can appear in an Evaluation list.  In the evaluation process,
other kinds of Atoms can get created. These include things like:

* ``ByteArray``
* ``CompiledCode``
* ``Complex``
* ``Dispatch``
* ``Image``
* ``Integer``
* ``Real``

In other words, things that might have an underlying internal representation of an object with no subparts that can be pulled out using ``Part[]``.

In Mathics, the function ``AtomQ[]`` will tell you if something is an Atom, or can't be subdivided into subexpressions.

Some examples:

.. code-block:: mathematica

    (* Strings and expressions that produce strings are atoms: *)
    >> Map[AtomQ, {"x", "x" <> "y", StringReverse["live"]}]
     = {True, True, True}

    (* Numeric literals are atoms: *)
    >> Map[AtomQ, {2, 2.1, 1/2, 2 + I, 2^^101}]
     = {True, True, True, True, True}

    (* So are Mathematical Constants: *)
    >> Map[AtomQ, {Pi, E, I, Degree}]
     = {True, True, True, True}

    (* A 'Symbol' not bound to a value is an atom too: *)
    >> AtomQ[x]
     = True

    (* On the other hand, expressions with more than one 'Part' after evaluation, even those resulting in numeric values, aren't atoms: *)
    >> AtomQ[2 + Pi]
     = False

    (* Similarly any compound 'Expression', even lists of literals, aren't atoms: *)
    >> Map[AtomQ, {{}, {1}, {2, 3, 4}}]
     = {False, False, False}

    (* Note that evaluation or the binding of "x" to an expression is taken into account: *)
    >> x = 2 + Pi; AtomQ[x]
     = False

    (* Again, note that the expression evaluation to a number occurs before 'AtomQ' evaluated: *)
    >> AtomQ[2 + 3.1415]
     = True



.. index:: Symbol

Symbol Class
============
.. index:: Symbol

Just above the ``Atom`` class is the ``Symbol`` which is an atomic element of an ``Expression``.
See `Atomic Elements of Expressions <https://reference.wolfram.com/language/guide/AtomicElementsOfExpressions.html>`_.

As born from the parser, Symbols start off like Lisp
Symbols. Following WL, Mathics has about a thousand named characters,
some common ones like "+", "-", and some pretty obscure ones. After
parsing, each of these can be incorporated into a Symbol object. But in the
evaluation process these symbols get bound to values in a scope, and
then they act more like a programming language variable. The Symbol
class described here has fields and properties that you of the kind
that you'd expect a variable in a programming language to have.

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

SympyConstant, MPMathConstant, and NumpyConstant
================================================

SympyFunction and MPMathFunction
================================
