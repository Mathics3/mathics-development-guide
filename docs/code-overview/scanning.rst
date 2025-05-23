Scanning
========

.. index:: tokenizer
.. index:: scanner

We have split out the scanner into a separate `github repository
<https://pypi.org/project/Mathics-Scanner/>`_ which has its own `PyPI
package <https://pypi.org/project/Mathics-Scanner/>`_.

==============================================================
Deciding what is goes into Scanning and what goes into Parsing
==============================================================

Compilers and human language often have work on at least
two-levels. In human speech, there is the concept of *phonemes* which
are the smallest unit of sound, and those are joined together to form
the higher-level words, sentences, paragraphs, etc.

In human written, *phonemes* are often broken replaced by the concept
of a syllable.

In computer languages, the equivalent of a phoneme or syllable is
called a *token*, and the process that makes the initial determination
is called a *scanner*.

But in computer languages, things are a little different. The breakout
between the phases is biased by the technology used.

Conventionally, the language of strings that can be recognized by
*regular expressions* forms what constitutes scanning, and the
language of strings that can be produced by context-free grammars
constitutes what goes into parsing.

Strictly speaking, the set of strings recognized by context-free
grammars is a superset of what can be recognized by regular expressions.

The difference, is that context free grammars can handle nesting while
regular expression cannot.  For example, making sure a List literal
like ``[1 2 [3 4]]`` or an output format expression like ``\( a \%
b\)`` nests properly is typically and more naturally must be done in
parsing, not scanning.  Parsing can match nesting as part of its
grammar, while in regular expressions in of themselves can't capture
nesting.

That said, there are perhaps hacky ways of adding code counts in
object variables that can work around this. Mathics3 code doesn't do
this though.

On the other hand, since the class of context free grammars is
greater than regular expressions it is possible inside a
parser grammar, to encode constructs that could recognized inside the scanner.

Consider a fully-qualified symbol name like ``System`$MachineName``.
The scanner could treat this as 3 tokens: "System", "`", and
"$MachineName" and the parser could could join these into
fully-qualified variable name. But this is not necessary, because
there is no nesting involved here. The language of regular expressions
can handle this fine. And Mathics3 specifically doesn't do this. The
scanner is responsible for detecting the boundaries of a fully-qualified symbol name.

*In general, the scanner handles all of the kinds of constructs that do not require nesting.*


==================================================
What makes WMA Scanning scanning and parsing hard?
==================================================

WMA defines over 400 characters and has over 1000 operators.  The list
is so large and the details of the individual characters and operators
is so involved, that we need to store all of this inside separate
table rather than try to hard-code this information directly into scanning and parsing code.

Information about characters includes things like whether the
character acts like a letter and can be part of a symbol name, or
whether this character symbol, by itself, is an operator.

Information about operators contains things like whether the operator
is infix, prefix, or postfix, and its operator precedence.

These kinds of character and operator properties influence symbol-name
tokenization in the scanner and how a compound M-expression are parsed
in the parser.

The parser also needs to detect when space represents multiplication.
Some operators are valid only inside "boxing expressions". Finally,
WMA has a rich set of escape-sequence which include not only detecting
special symbols like white space newlines (``\n``), tabs (``\t``) or
carriage return (``\r``), but it also includes sequences for all of
the named characters like ``\[theta]`` and boxing operators like
``\+`` which are valid only in a boxing expression context.


=====================
How the Scanner works
=====================

Currently there are two passes made in the scanner, a "pre-scan" in found in
`mathics_scanner.prescanner
<https://github.com/Mathics3/mathics-scanner/blob/master/mathics_scanner/prescanner.py>`_
which converts some WL-specific character codes to character or long
names and the `mathics_scanner.tokeniser
<https://github.com/Mathics3/mathics-scanner/blob/master/mathics_scanner/tokeniser.py>`_
which runs after that.

The prescanner may get dropped in the future by incorporating the
escape-sequence handling into the main scanning.

The tokenizer breaks up a string into *tokens*,
classifications of a sequence of characters, which is then as the
atoms on which the parser pattern matches on.

There are various modes or contexts the scanner can be in. The modes are

* inside an expression; this is how things start out
* inside a string
* inside a filename

Comments are handled, but these do not contitute a special mode.

The way a string is matched is determined by its leading character. Depending on the character, a custom function beginning with ``t_`` can be called. Custom routines include:

* ``t_Filename``
* ``t_Get``
* ``t_Number``
* ``t_Put``
* ``t_PutAppend``
* ``t_String``

Failing having a custom routine, matching is determined by Python
regular expression matching that starts with the string prefix.

================
Scanner Testing
================

The command-line utility ``mathics3-tokens`` from the `Mathics-Scanner <https://pypi.org/project/Mathics-Scanner/>`_ package can be used to show tokenization.

For WMA, the `CodeTokenize <https://reference.wolfram.com/language/CodeParser/ref/CodeTokenize.html>`_ function of the ``CodeParser`` package will show tokenization.

Over time Mathics3 will align its token names to better match the names produced by ``CodeTokenize``.
