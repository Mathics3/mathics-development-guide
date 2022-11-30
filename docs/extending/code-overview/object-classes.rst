==============
Object Classes
==============

The fundamental classes that functions are built up from are described
below.

Most of these classes are defined in `mathics.builtin.base
<https://github.com/mathics/Mathics/tree/master/mathics/builtin/base.py>`_
or `mathics.core.expression <https://github.com/mathics/Mathics/tree/master/mathics/core/expression.py>`_.

Class Diagram for Some of the Classes
=====================================

Below is a `UML 2.5 Class diagram
<https://creately.com/blog/diagrams/class-diagram-tutorial/>`_ for some
of the classes described below:


.. image:: /images/uml-diagram.png
  :alt: UML 2.5 Class diagram

A Class name that begins with ``Base`` is a `Virtual class <https://en.wikipedia.org/wiki/Virtual_class>`_.

.. index:: Atom, AtomQ

Atom Class
==========

Recall that an Expression to be evaluated is initially a kind of :term:`M-expression`,
an object in the ``Expression`` class, where each list item is either itself
an :term:`Expression` or an object in a class derived from :term:`Atom`.

The ``Atom`` class we encountered earlier when describing the nodes
that get created intially from a parse. Those were:

* ``Number``
* ``String``
* ``Symbol``
* ``Filename``

Atoms here is from module ``mathics.core.parse.ast``

However this is converted in ``mathics.core.parser.convert.Converter.convert()``
into another kind of expression where ``Number`` is replaced by a more
specific kind of number like ``Integer``, or ``Real``.

There are a few other kinds of Atoms or fundamental objects like:

* ``ByteArray``
* ``CompiledCode``
* ``Complex``
* ``Dispatch``
* ``Image``

In general, atoms are objects might have an underlying internal representation with no user-visable subparts that can be pulled out using ``Part[]``.

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


BaseElement Class
=================

A Mathics M-expression is the main data structure which evalution is
performed on. An M-expression is, in general, a tree.  The nodes of this
tree come from the ``BaseElement`` class. Note that element in
addition to being a ``BaseElement`` are an ``Atom`` as well. In other words,
an ``Atom`` is a subclass of ``BaseElement``.

The other subclass of ``BaseElement`` is an ``Expression``.

Note as the prefix ``Base`` implies, a BaseElement is a virtual class.


.. index:: Symbol

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

        def eval(self, expr, evaluation):
            "Head[expr_]"

            return expr.get_head()

In the above, we have not defined an ``evaluation()`` method
explicitly so we get ``Expressions``'s built-in ``evaluation()``
method.

A feature of the ``Builtin`` class is the convention that its provides
a convention by which "eval" methods of the class can be matched
using the method's name which must start with "eval" and a pattern
listed in the method's doc string. This is used in the example above.

Here, ``Head`` has one paramater which is called *expr*. Note that in
the Python method there is also *expr* variable it its method
signature which is listed right after the usual *self* method that you
find on all method functions.

At the end is an *evaluation* parameter and this contains definitions
and the context if the method needs to evaluate expressions.

Definition Class
================
.. index:: Definition


A Definition is a collection of Rules and attributes which are associated with a ``Symbol``.

A ``Rule`` is internally organized in terms of the context of application in

* ``OwnValues``,
* ``UpValues``,
* ``Downvalues``,
* ``Subvalues``,
* ``FormatValues``,  etc.

.. index:: Definitions

Definitions Class
=================

The Definitions class hold state of one instance of the Mathics
interpreter is stored in this object.

The state is then stored as ``Definition`` object of the different symbols defined during the runtime.

In the current implementation, the ``Definitions`` object stores ``Definition`` s in four dictionaries:

- builtins: stores the defintions of the ``Builtin`` symbols
- pymathics: stores the definitions of the ``Builtin`` symbols added from pymathics modules.
- user: stores the definitions created during the runtime.
- definition_cache: keep definitions obtained by merging builtins, pymathics, and user definitions associated to the same symbol.

.. index:: Predefined

Expression Class
================

An Expression object the main object that we evaluate over. It
represents an M-expression formed from input.

Although objects derived from ``Atom``, e.g. symbols and integers, are
valid expressions, this class describes *compound* expressions, or
expressions that are more than a single atom/element. So in contrast to an
object of type ``Atom``, an ``Expression`` object is some sort of
structured node that as in Mathics itself, has a ``Head`` (function
designator) and a ``Rest`` (or arguments) component.

.. index:: Expression

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


Symbol Class
============
.. index:: Symbol

Just above the ``Atom`` class is the ``Symbol`` which is an atomic element of an ``Expression``.
See `Atomic Elements of Expressions <https://reference.wolfram.com/language/guide/AtomicElementsOfExpressions.html>`_.

As born from the parser, Symbols start off like Lisp
Symbols. Following WL, Mathics has about a thousand named characters,
some common ones like "+", "-", and some pretty obscure ones. After
parsing, each of these can be incorporated into a Symbol object. But
in the evaluation process in conjuction with the ``Definitions``
object that is in the evaluation object, these symbols get bound to
values in a scope, and then they act more like a programming language
variable. The Symbol class described here has fields and properties
that you of the kind that you'd expect a variable in a programming
language to have.

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

Which Class should be used for a Mathics Object?
================================================

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
