
.. index:: patternmatching
.. _patternmatching:

.. contents::

=================
Pattern matching
=================



One of the most involved aspects of the core implementation is the pattern matching mechanism. The evaluation mechanism in the core 
consists on taking an (S-)expression,  looking for replace rules stored in the `Definitions` object that match the full expression or some of 
its sub-expressions, and apply them until the expression converges to its final form. The power of the WL then relies in the possibility of defining 
rules by patterns that can match with many different expressions, and building new expressions based on the variable part of the pattern.
For this reason, when performance is important, to understand the pattern matching mechanism becomes essential.

Lets start from the begining. `Pattern` (defined in `mathics.core.pattern`) is the base class that represents the pattern for an expression. 
We have two basic subclasses: `AtomPattern`s that represent  patterns that match with a given atomic expression,  and `ExpressionPattern`s that represent patterns
that matches with non-atomic expressions (i.e., expressions with a head and leaves). We also have several `Builtin` symbols (defined in `mathics.builtin.patterns`)
representing different pattern constructions (like `Pattern_`, `Blank`, `PatternTest` or `Alternatives`). All of these `Builtin`s are derivated from 
the `PatternObject' class, which is at its time is derivated from `InstanceableBuiltin` and `Pattern`.

Every `Pattern` object has three important methods: `does_match`, `get_match_candidates`, and `match`.  The first one checks if certain expression matches the pattern. 
`get_match_candidates` takes a list of leaves and finds all the elements that matches. Finally, `match` is the most involved method and has the following profile:

`match(yield_func,
       expression,
       vars,
       evaluation,
       head=None,
       leaf_index=None,
       leaf_count=None,
       fully=True,
       wrap_oneid=True,
)`

When called, this method explores `expression` and its leaves, looking for subexpressions that match the pattern. Each time a coincidence is found,
`yield_func(vars, rest)` is called with `vars` as a first parameter, and the second parameter depends on the specific context.

