.. _doc_markup:

Documentation Markup
====================

There is a lot of special markup syntax you can use in the
documentation. It is kind of a mixture of XML, LaTeX, Python doctest,
and custom markup.

*In the future, we plan to use more Sphinx-based documentation.*

The following commands can be used to specify test cases.

+------------------------+-----------------------------------------------------------+
| Markup                 | Meaning                                                   |
+========================+===========================================================+
| ``>>`` *Mathics code*  | Some Mathics code to run and to appear in documentation.  |
+------------------------+-----------------------------------------------------------+
| ``#>`` *Mathics code*  | Some Mathics code torun but not appearin documentation.   |
+------------------------+-----------------------------------------------------------+
| ``X>`` *Mathics code*  | Mathics code shown in the documentation but not run.      |
+------------------------+-----------------------------------------------------------+
| ``S>``                 | a test query that is shown in the documentation and run   |
|                        | if the ``SANDBOX`` environment variable is not set.       |
+------------------------+-----------------------------------------------------------+
| ``=`` *output*         | expected output produced by the Mathics code.             |
+------------------------+-----------------------------------------------------------+
| ``...``                | matches any output; used when output can vary.            |
+------------------------+-----------------------------------------------------------+
| ``.``                  | a newline which is expected to appear in test ouput.      |
+------------------------+-----------------------------------------------------------+
| ``$`` *name* ``$``     +  variable identifier in Mathics code or in text.          |
+------------------------+-----------------------------------------------------------+
| ``-Graphics-``         | graphics in the test result.                              |
+------------------------+-----------------------------------------------------------+
| ``:`` *message*        | a message in the result of the test query.                |
+------------------------+-----------------------------------------------------------+
| ``\|`` *print*         | a printed line in the result of the test query.           |
+------------------------+-----------------------------------------------------------+

*Todo: give examples of each of these.*

The following commands can be used to markup documentation text:

+----------------------------------+-----------------------------------------+
| Syntax                           | Explanation                             |
+==================================+=========================================+
| ``## $comment$``                 | a comment line that is not shown in the |
|                                  | documentation.                          |
+----------------------------------+-----------------------------------------+
|  <dl> *dl-list* </dl>            | a definition list with ``<dt>`` and     |
|                                  | ``<dd>`` entries.                       |
+----------------------------------+-----------------------------------------+
|  <dt> *title*                    | the title of a description item.        |
+----------------------------------+-----------------------------------------+
| <dd> *description*               | the description of a description item.  |
+----------------------------------+-----------------------------------------+
| <ul> *list* </ul>                | an unordered list of <li>               |
|                                  | entries.                                |
+----------------------------------+-----------------------------------------+
| <ol> *list* </ol>                | an ordered list of <li> entries.        |
+----------------------------------+-----------------------------------------+
| <li> *item*  `                   | an item of an unordered or ordered      |
|                                  | list.                                   |
+----------------------------------+-----------------------------------------+
| ``'`` _code_ ``'``               | inline Mathics code or other code.      |
+----------------------------------+-----------------------------------------+
| <console> *text* </console>      | a console (shell/bash/Terminal)         |
|                                  | transcript in its own paragraph.        |
+----------------------------------+-----------------------------------------+
| <con> *text* </con>              | an inline console transcript.           |
+----------------------------------+-----------------------------------------+
| <em> *text* </em>                | emphasized (italic) text.               |
+----------------------------------+-----------------------------------------+
| <i> *text* </i>                  | the same as <em>.                       |
+----------------------------------+-----------------------------------------+
| <url> *url* </url>               | a URL.                                  |
+----------------------------------+-----------------------------------------+
| <img ``src="`` *src* ``"``       | an image.                               |
| ``title="`` *title* ``"``        |                                         |
| ``label="`` *label* ``"``        |                                         |
+----------------------------------+-----------------------------------------+
| <imgpng ``src="`` *src* "        | the same as <img>.                      |
| ``title="`` *title* ``"``        |                                         |
| ``label="`` *label* ``"``        |                                         |
+----------------------------------+-----------------------------------------+
| <ref label=" *label* ">``        | a reference to an image.                |
+----------------------------------+-----------------------------------------+
| ``\skip``                        | a vertical skip.                        |
+----------------------------------+-----------------------------------------+
| ``\LaTeX``, ``\Mathematica``,    | special product and company names.      |
| ``\Mathics``                     |                                         |
+----------------------------------+-----------------------------------------+
| ``\'``                           | a single ``'``.                         |
+----------------------------------+-----------------------------------------+

To include images in the documentation, use the ``img`` tag, place an
EPS file *src* ``.eps`` in `mathics.doc.documentation.images <https://github.com/mathics/Mathics/tree/master/mathics/doc/documentation/images>`_ and run ``images.sh``
in the `mathics.doc <https://github.com/mathics/Mathics/tree/master/mathics/doc>`_ directory.
