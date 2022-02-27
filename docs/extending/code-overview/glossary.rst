Glossary
========

.. glossary::

   Atom

     The leaves of an :term:`S-expression` or an expression. It is an object that has no structure below it.
     See also "Atomic Primitives" in the Mathics documentation for builtin-functions.

     In the code there are to kinds of Atoms. Those produced by the
     parser, which get converted to Atoms used in the interpreter. The
     main difference between the two is that ``Number`` is converted into something more specific like, ``Real`` or ``Integer``.

   apply
   application

     The process by which we take an :term:`S-expression` and prepare that expression evaluation at the top-level of the expression given.

     In Mathics this involves looking at the head symbol (``Head[]``)
     and taking action based on information that symbols binding.

     There are distinct kinds of application: rule application, and function application.

     See also `Apply <https://en.wikipedia.org/wiki/Apply>`_.

   binding

     Associating a symbol name with a value. In Mathics, the symbol names an expression or :term:`S-expression` and the
     values come from an definitions found in an evaluation. See also `Free and bound variables <https://en.wikipedia.org/wiki/Free_variables_and_bound_variables>`_ and
     `Name binding <https://en.wikipedia.org/wiki/Name_binding>`_.

   builtin function

     A Mathics function which is predefined when the system starts up. There are thousands of these in Mathics.

   boxing

     A special type of evaluation that is kicked off by
     formatting. Mathics objects can have formatting or boxing rules
     associated with them. This process allows objects objects to be
     displayed in flexibile way depending on the context that the
     object appears.  See `Formatted Output <https://reference.wolfram.com/language/tutorial/TextualInputAndOutput.html#6589676>`_.

   Definition

    A Python class used which provides for a way for a Symbol get its value, attributes or properties.
    The mathics builtin function ``Definition`` can be used to get information about a Symbol's definition.

   DownValue

     A binding in an evaluation which can be used in a subexpression
     should one of the other binding methods, i.e. ownvalue fail.

     Mathics function ``DownValues`` can be used to query downvalues.

   element
   elements

     In the singular form, *element* is any node of an Expression or
     :term:`S-expression`.  The base class :ref:`BaseElement Class`
     defines properties that an element of the the expression.

     At any given level of the expression tree described in an S-expression, the
     head element or first element is a little different in that it
     represents a function or operator. So generally when we refer to
     this kind of element, we will use the more qualified term "head element".

     In the plural, *elements* when applied to a given level in an
     expression tree, we generally mean the elements other than the
     head element. Possibly a better word, might be "arguments" or
     "function arguments", since that is the role they play in a
     S-expression.

     In the code there are accessor methods ``get_elements()``,
     property ``elements`` and attribute ``_elements``.

   eval

     A functional compuation. We use this in the functional
     programming sense; it is distinct from :term:`evaluate` which is more
     complex, but has *eval()* as a component of that.

     See `eval <https://en.wikipedia.org/wiki/Eval>`_.

   evaluate
   evaluation

     The process of taking an Mathics Expression or :term:`S-expression`
     producing a transformation or computation on that.

     It involves the distinct phases:

        * rewriting the expression, and
	* function application which performs eval()

     Note that function appliction can kick off another *evaluate()*,
     so this process is recursive.

   Expression

     This is both a Symbol defined in Mathics, and a Python class
     which implements the idea of a generalized List used in
     :term:`evaluation`. In this document we are usually referring to
     the Python class, not the built-in Symbol.

     Conceptually, an object in this class represents a sequence atoms, and (nested)
     Expressions. An expression has two parts, a ``Head`` which is expected be a function reference,
     and 0 or more :term:`elements`.

     Atoms like ``String`` or ``Integer`` are degnerate forms of
     expressions. However when we refer to the class, we are referring
     to non-degenerate or compound Expressions. In the code, both are
     forms of :ref:`BaseElement Class`.

   form

   format

   OwnValue

     A binding in an evaluation which is intended to be use across a level of an evaluation.

   literal value

     An constant value, symbol that has a constant value, or an atom that isn't a symbol. Numbers like 5,
     The Symbol ``True``, the string "goo" are all examples of literal values.

     Lists consisting of literal values are also be literal values.


   namespace

   NValues

     Numeric values associated with a symbol.
     It is one of the kinds of values that can be associated with a Symbol. The others are:

       * ``Attributes``,
       * ``DefaultValues``,
       * ``FormatValues``,
       * ``Messages``
       * ``Options``
       * ``OwnValues``, and
       * ``Upvalues``

     See the documentation for the Mathics builtin function ``NValues``.


   pattern

     A object found in a definition associated with a symbol an ``Expression`` or a part of the ``Expression``.
     See the documentation for Mathics builtin ``Pattern``.

   replacement rule

     A replacement rule is a kind of ``Rule`` that consists of a
     ``Pattern`` and a specification for how to transform the
     expression using the mathing parts. Rules are said to be
     *applied* to an ``Expression`` to produce a new ``Expression``.

     For example ``F[x_Real]-> x^2`` is a rule that when applied to
     the expression ``G[F[1.], F[a]]`` produces the new expression
     ``G[1.^2, F[a]]``. Certain (internal) rules can also produce changes
     in the state of the system (writing files, printing a string, changing
     the definitions of a symbol, or setting a timeout). This happens for
     internal rules, like the associated to the pattern ``Set[a,1.]``, which
     modifies the definition of ``a`` adding the rule ``a->1``.

   rewrite

     The first phase in evaluating an expression, where an expression is rewritten based on
     attributes and rewrite rules bound to an expression's ``Head`` Symbol.

     For the general concept, see `Rewriting <https://en.wikipedia.org/wiki/Rewriting>`_.

   S-expression

     A structure which consists of a sequence atoms, and (nested)
     expressions. However at each level there is a ``Head`` which
     represents an operator or function.

     The ``Expression`` produced by the parser is an S-expression. In
     evaluation though this pure data structure is transformed and has
     additional state which can be attached to :term:`elements` of the expression.

     See `S-expression <https://en.wikipedia.org/wiki/S-expression>`_.

   scope

   subexpression

     See :term:`element`.

   UpValue
