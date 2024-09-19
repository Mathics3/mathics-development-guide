=====
Rules
=====

.. index:: Rules
.. _rules:

.. contents::

Rules are a core part of the way Mathematica and Mathics3 execute a program.

Expressions which are transformed by rewrite rules (AKA transformation
rules) are handed by the ``Rule`` class.

There are also rules for how to match, assign function parameter
arguments, and then apply a Python "evaluation" function to a Mathics3 Expression.
These kinds of rules are handled by objects in the ``FunctionApplyRule`` class.

The module ``mathics.core.rules`` contains the classes for these two types of rules.

In a ``FunctionApplyRule`` rule, the match status of a rule depends on the evaluation return.

For example, suppose that we try to apply rule ``F[x_]->x^2`` to the expression ``F[2]``. The pattern part of the rule, ``F[x_]`` matches
the expression, ``Blank[x]`` (or ``x_``) is replaced by ``2``, giving the substitution expression ``2^2``. Evaluation then stops
looking for other rules to be applied over ``F[2]``.

On the other hand, suppose that we define a ``FunctionApplyRule`` that associates ``F[x_]`` with the function:

.. code-block:: python

    ...
    class MyFunction(Builtin) -> Optional[Expression]:
        ...
        def eval_f(self, x, evaluation: Evaluation):
           "F[x_]"   # pattern part of FunctionApplyRule
            if x>3:
                return Expression(SymbolPower, x, Integer2)
           return None

Then, if we apply the rule to ``F[2]``, the function is evaluated returning ``None``. Then, in the evaluation loop, we get the same
effect as if the pattern didn't match with the expression. The loop continues then with the next rule associated with ``F``.

Why do things this way?

Sometimes, the cost of deciding if the rule match is similar to the cost of evaluating the function. Suppose for example a rule:

.. code-block:: mathematica

    F[x_/;(G[x]>0)]:=G[x]

with ``G[x]`` a computationally expensive function. To decide if ``G[x]`` is larger than 0, we need to evaluate it,
and once we have evaluated it, just need to return its value.

Also, this allows us to handle several rules in the same function, without relying on our very slow pattern-matching routines.
In particular, this is used for for some critical low-level tasks like building lists in iterators, processing arithmetic expressions,
plotting functions, or evaluating derivatives and integrals.
