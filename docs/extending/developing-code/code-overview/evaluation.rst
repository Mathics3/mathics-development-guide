.. index:: evaluation
.. _evaluation:

===========================
Evaluation of an Expression
===========================

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


Mathics Function Name to Python method lookup
=============================================

.. index:: Symbol, Predefined, Builtin, Expression

When the first leaf, called the "head" (or ``Head[]``) of an
``Expression`` is a ``Symbol`` this is assumed to be a Mathics
function call. The function name comes from the head. If this is a
built-in function, like ``Plus``, the Mathics function name is the name
of a Python class derived ultimately from ``Builtin``. These
Mathics function-like classes are described in later sections.

However before invoking that Mathics function, we need to check if
there is a rewrite rule that applies to the Mathics function call.  A
function-like class like ``Plus`` can have a class ``rules`` variable.
When given, the ``rules`` class varaible specifies rewrite rules that
are to be considered before invoking the function. If one of these
rewrite rules matches against the Mathics function call, the
expression is rewritten into another expression and another trip is
made around the evaluation loop. Eventually rewriting stops.

And when rewriting stops, if the head is a Mathics built-in function
name, like ``Plus``, we still need to figure out which ``apply``
method to call inside an object created from that class. We will
describe how this is done elsewhere.

Here, we will just say that is done using each ``apply`` method's
docsstring. And this apply-method determination is kicked off through
Expression's ``evaluate``. Ignoring the detailis of how this is
done, one of the ``apply`` methods is found to match, and the
remaining leaves of the ``Expression`` indicate parameters to be given
to the found ``apply`` function. In addition, an instance of an
``Evaluation`` is also supplied as a parameter in the call to the
``apply`` method. .

In the simplest case, there is no rule rewriting, or apply methods,
and the instance method's *evaluate()* method is called. This is used
when a function has no parameters or arguments. This kind of thing
happens when a constant or variable name is used; here the variable
name is prefaced with a ``$``. Examples are ``$VersionNumber`` or
``$MachineName``.

When a function takes parameters it method's Object class is derived
either directly indirectly from the ``Builtin`` class rather than the
``Predefine`` class.

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
