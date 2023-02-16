.. _doc_markup:

Documentation Markup
====================

There home-grown special markup syntax you can use in the
documentation. It is kind of a mixture of XML, LaTeX, Python doctest,
and custom markup.

*In the future, we plan to use more Sphinx-based documentation.*

The following commands can be used to markup documentation text:

Markup in Documentation
------------------------

.. _doc_help_markup:

.. index:: <dl>, <dt>, <dd>, <ul>, <ol>, <li>, <console>, <con>, <img>, <imgng>, <i>

+----------------------------------+-----------------------------------------+
| Syntax                           | Explanation                             |
+==================================+=========================================+
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
| <li> *item*                      | an item of an unordered or ordered      |
|                                  | list. Note: no </li>.                   |
+----------------------------------+-----------------------------------------+
| ``'`` *code* ``'``               | inline Mathics3 code or other code.     |
+----------------------------------+-----------------------------------------+
| ``$`` *name* ``$``               | Math-mode variable identifier in        |
|                                  | Mathics3 code or in text.               |
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
| <url> :link text: *url* </url>   | a URL with link text                    |
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
| ``## $comment$``                 | a comment line that is not shown in the |
|                                  | documentation.                          |
+----------------------------------+-----------------------------------------+

To include images in the documentation, use the ``img`` tag, place an
EPS file *src* ``.eps`` in `mathics.doc.documentation.images <https://github.com/mathics/Mathics/tree/master/mathics/doc/documentation/images>`_ and run ``images.sh``
in the `mathics.doc <https://github.com/mathics/Mathics/tree/master/mathics/doc>`_ directory.

For long *url*, it is possible to split the url in several lines. Spaces and line break characters are removed when the documentation is compiled. For example,



     <url>:NetworkX:
     https://networkx.org/documentation/networkx-2.8.8/reference/algorithms/\
      generated/networkx.algorithms.tree.mst.minimum_spanning_edges.html
     </url>


produces, in the online documentation, the following ``<a>`` tag: 

``<a href=https://networkx.org/documentation/networkx-2.8.8/reference/algorithms/generated/networkx.algorithms.tree.mst.minimum_spanning_edges.html>NetworkX</a>``


Markup for Code Examples
------------------------

.. _doc_test_markup:

.. index:: >>, #>, X>, S>, ..., \|, =

The following commands can be used to specify test cases.

+------------------------+-----------------------------------------------------------+
| Markup                 | Meaning                                                   |
+========================+===========================================================+
| ``>>`` *Mathics3 code* | Some Mathics3 code to run and to appear in documentation. |
+------------------------+-----------------------------------------------------------+
| ``=`` *output*         | expected output produced by the Mathics3 code.            |
+------------------------+-----------------------------------------------------------+
| ``...``                | matches any output; used when output can vary.            |
+------------------------+-----------------------------------------------------------+
| ``.``                  | a newline which is expected to appear in test output.     |
+------------------------+-----------------------------------------------------------+
| ``-Graphics-``         | graphics in the test result.                              |
+------------------------+-----------------------------------------------------------+
| ``:`` *message*        | a message in the result of the test query.                |
+------------------------+-----------------------------------------------------------+
| ``\|`` *print*         | a printed line in the result of the test query.           |
+------------------------+-----------------------------------------------------------+

It is good to create examples that convey some aspect about the Mathics3 Function.

In the past, the documentation system was abused and ran edge cases
and prior bugs fixed. For that please write a pytest.


We have not purged ourself of this behavior, so will find following
markup in docstrings. These are deprecated.

However please don't create more examples. Instead please consider
moving something like this to a pytest unit test which is far more flexibile.

+------------------------+-----------------------------------------------------------+
| Markup                 | Meaning                                                   |
+========================+===========================================================+
| ``#>`` *Mathics3 code* | Some Mathics3 code to run but not appearing documentation.|
+------------------------+-----------------------------------------------------------+
| ``X>`` *Mathics3 code* | Mathics3 code shown in the documentation but not run.     |
+------------------------+-----------------------------------------------------------+
| ``S>``                 | a test query that is shown in the documentation and run   |
+------------------------+-----------------------------------------------------------+

*Todo: give examples of each of these.*
