
.. index:: Pattern Matching; Evaluation
.. _patternmatching:

.. contents::

==============================
Pattern Matching in Evaluation
==============================

Pattern matching is used in evaluation of Mathics3 Expression and therefore in Function resolution. Because this process is both time-consuming and involved, it is important to understand how it works. We describe some of this process here.

In the evaluation loop, each ``Element`` of an ``Expression``  is looked up in the rules of an evaluation's ``definitions`` object for the evaluation. Each rule matching the Element (``Downvalues``) or the subexpression (``Upvalues``, ``Subvalues``) containing the ``Element`` is considered.
When a rule matches an expression, the rule specifies how sub-expressions get bound to names, and how the expression is transformed. After this happens, the evaluation process is repeated using the replaced expression.

The process repeats until the expression converges and there are no further changes.

The power of the WL then relies in the possibility of defining rules by patterns that can match with many different expressions, and building new expressions based on the variable part of the pattern.

See also :ref:`Rules <rules>`.

Pattern Classes
---------------

We now describe the Class hierarchy for ``BasePattern`` which is defined inside ``mathics.core.pattern``.  This is the abstract base class that represents the pattern.

Its subclasses are:

* ``AtomPattern`` patterns that match with a given atomic expression,  and
* ``ExpressionPattern`` patterns match with non-atomic expressions (i.e., expressions with a head and elements).

Every ``Pattern`` object has three important methods: ``does_match()``, ``get_match_candidates()``, and ``match()``:

* ``does_match()`` checks if a given expression matches the pattern
* ``get_match_candidates()`` finds all the potential matches
* ``match()`` performs what needs to be done when there is a match

The last method, ``match()``, is the most involved. It has the following function signature:

.. code-block:: python

    match(yield_func, expression,
          vars,
          evaluation,
          head=None,
          element_index=None,
          element_count=None,
          fully=True,
          wrap_oneid=True
	  )

When called, this method binds subexpressions of the expression to
parts of the pattern. For each match, ``yield_func(vars, rest)`` is
called with ``vars`` as a first parameter, and the second parameter
depends on the specific context.

PatternObject
-------------

A Mathics3 Pattern contains and is defined in terms of one or more pattern objects (class ``PatternObject``), ``PatternObject`` is defined in ``mathics.builtin.patterns``.
Builtin functions ``Blank``, ``Pattern`` and ``Alternatives`` are three kinds of pattern object. All of these ``Builtin`` classes are derived from
the ``PatternObject`` class, which is derived from both the ``InstanceableBuiltin`` and ``BasePattern``.

See also `<https://reference.wolfram.com/language/guide/Patterns.html>`_
