Scanning
========

.. index:: tokenizer
.. index:: scanner

We have split out the scanner into a separate github repository
`<https://pypi.org/project/Mathics-Scanner/>`_ which has its own `PyPI
package <https://pypi.org/project/Mathics-Scanner/>`_.

==============================================================
Deciding what goes into Scanning and what goes into Parsing
==============================================================

Computer and human languages are generally understood by dividing the understanding process into at least two levels. In human speech, there
is the concept of *phonemes*, which are the smallest unit of sound,
and those are joined together to form the higher-level words,
sentences, paragraphs, etc.

In written human language, *phonemes* are generally replaced by the concept
of a syllable.

In computer languages, the equivalent of a phoneme or syllable is
called a *token*; the process that makes the initial determination
is called a *scanner*.

Where to make a level split between what should be recognized in the
scanner and what should be recognized by a parser, is dictated by the
technology that compilers typically use. (Something analogous in
Biological construction and evolution are probably the reason for the
the levels in human languages, as well.)

Conventionally, the set of strings that can be recognized by *regular
expressions* constitutes the lower-level scanning phase. The
language of strings and tokens that can be produced by context-free grammars constitutes what goes into the higher-level parsing phase.

Strictly speaking, the set of strings recognized by context-free grammars is a superset of what can be recognized by regular expressions.

However, context-free grammars can handle nesting while regular
expressions cannot.  For example, checking the nesting of a ``List``
literal like ``[1 2 [3 4]]`` or an boxing format expression like ``\(a \% b\)`` is typically and more naturally done in parsing,
not scanning.  Parsing can match nesting as part of its grammar, while regular expressions in of themselves can't capture nesting.

That said, there are perhaps hacky ways of adding code counts in
object variables that can work around this. Mathics3 code doesn't do
this, though.

On the other hand, since the class of context-free grammars is
greater than regular expressions, it is possible inside a
parser grammar, to encode constructs that could be recognized inside the scanner.

Consider a fully-qualified symbol name like ``System`$MachineName``.
The scanner could treat this as 3 tokens: ``System``, `````, and
``$MachineName`` and the parser could join these into a
fully-qualified variable name. But this is not necessary, because
there is no nesting involved here. The language of regular expressions
can handle this fine. And Mathics3 specifically doesn't do this. The
scanner is responsible for detecting the boundaries of a fully-qualified symbol name.

*In general, the scanner handles all constructs that do not require nesting.*


==================================================
What makes WMA Scanning and parsing hard?
==================================================

WMA defines over 400 characters and has over 1000 operators.  The list
is so large, and the details of the individual characters and operators is so involved that we need to store all of this inside a separate
table rather than try to hard-code this information directly into scanning and parsing code.

Information about characters includes things like whether the
character acts like a letter and can be part of a symbol name, or whether this character symbol, by itself, is an operator.

Information about operators contains things like whether the operator
is infix, prefix, or postfix, and its operator precedence.

These kinds of character and operator properties influence the symbol-name
tokenization in the scanner and how a compound M-expression is parsed in the parser.

The parser also needs to detect when space represents multiplication.
Some operators are valid only inside "boxing expressions". Finally,
WMA has a rich set of escape sequences that include not only detecting
special symbols like white space newlines (``\n``), tabs (``\t``) or
carriage return (``\r``), but it also includes sequences entering characters in hexadecimal (``\:03b8`` and ``\.42``, Unicode, octal (e.g. ``\065``, or by long
character name ``\[theta]``). See `Entering Characters <https://reference.wolfram.com/language/tutorial/InputSyntax.html#29301>`_ for more details.

There are escape sequences for boxing operators like ``\+`` that are valid only in a boxing expression context.

Characters entered using an escape sequence function as though they were added directly; escape characters can be found as part of a Symbol name or as an operator.


=====================
How the Scanner Works
=====================

Currently, there are two passes made in the scanner, and a "pre-scan" is found in
`mathics_scanner.prescanner
<https://github.com/Mathics3/mathics-scanner/blob/master/mathics_scanner/prescanner.py>`_
which converts some WL-specific character codes to character or long
names and the `mathics_scanner.tokeniser
<https://github.com/Mathics3/mathics-scanner/blob/master/mathics_scanner/tokeniser.py>`_
which runs after that.

The prescanner may get dropped in the future by incorporating the
escape-sequence handling into the main scanning.

The tokenizer breaks up a string into *tokens*,
classifications of a sequence of characters, which is then used as the
atoms on which the parser pattern matches.

There are various modes or contexts in which the scanner can be. The modes are

* inside an expression; this is how things start out
* inside a string
* inside a filename

Comments are handled, but these do not constitute a special mode.

The way a string is matched is determined by its leading character. Depending on the character, a custom function beginning with ``t_`` can be called. Custom routines include:

* ``t_Filename``
* ``t_Get``
* ``t_Number``
* ``t_Put``
* ``t_PutAppend``
* ``t_String``

Failing to have a custom routine, matching is determined by Python
regular expression matching that starts with the string prefix.

================
Scanner Testing
================

The command-line utility ``mathics3-tokens`` from the `Mathics-Scanner <https://pypi.org/project/Mathics-Scanner/>`_ package can be used to show tokenization.

For WMA, the `CodeTokenize <https://reference.wolfram.com/language/CodeParser/ref/CodeTokenize.html>`_ function of the ``CodeParser`` package will show tokenization.

Over time, Mathics3 will align its token names to better match the names produced by ``CodeTokenize``.
