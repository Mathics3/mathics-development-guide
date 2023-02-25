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



Guidelines for writting documentation
=====================================


When a new builtin is added, it is expected to follow the following guidelines regarding the format of the docstrings and `summary_text` attribute, which are used for building the documentation. Some of these guidelines are reinforced by the CI.

`summary_text` is used in the online documentation as a brief description of what the symbol represents. For builtins representing the head of expressions, `summary_text`, starts with an active verb with the word in lowercase, e.g. "retrieve" as opposed to "Retrieve".  If you look at the section that the summary appears it is nice to use the same verb for similar kinds of things. For example we may "list" builtins that end with "List" (EdgeList, VertexList" but, "find" builtins with "Index" at the end of the name "EdgeIndex", "VertexIndex". For variables, and options, we _do not_ start with an active verb.

Docstrings contain information about the content of the documentation entry. They must consist on the following parts:
* Title and url refs.
* `<dl>..</dl>` usage description.
* Extended description section.




Title
------

We can use use pymathics.graph as an example to compare against.

If there is a wikipedia entry that goes first. See AdjacencyList for an example.

It may be that only a part of the Wikipedia entry is available. Fill in other text outside of the URL. See DirectedEdge for an example. 

If there is no wikipedia mention, it is okay to give some free title. EdgeDelete is an example. 

Or you can omit the title altogether. `RandomGraph` is an Example.

In general we go with the Wikipedia name rather than the WMA for the title. And this includes symbolic parameter names. CompleteKaryTree is an example.

When the only thing we have is a WMA link we add "link" to the title. EdgeList is an example .

Remember that line breaks are significant. `\` can be used to wrap a long line. 
Start the url name on a new line after `<url>`. For example: 

```
<url>
:WMA link:
https://reference.wolfram.com/language/ref/EdgeList.html</url>
```

Note that there is no line break at the end before or after `</url>`. 

Please don't get too creative in formatting. There are many other areas in the selection of words to describe what is need may require care. But here it shouldn't require much thought for the _formatting_ aspects. 

If the URL is too long, of course, you can split it up in a way that the URL tag understands.  Please inspect the URLs in a browser for change.  Ideally you would click the link, but if not or before, look at the URL that appears when the link is hovered over. 



There should be at least one doc example for each function in that is focused on describing what the function does (not how it can be tested).  Examples for tests should be added as pytests.


`<dl>...</dl>` usage block
----------------------------

The title must be followed by a `<dl>...</dl>`, describing the diffferent ways to use the symbol. For example, in the  `Builtin` class `LaguerreL`:

    ```
     <dl>
       <dt>'LaguerreL[$n$, $x$]'
       <dd>returns the Laguerre polynomial L_$n$($x$).

       <dt>'LaguerreL[$n$, $a$, $x$]'
       <dd>returns the generalised Laguerre polynomial L^$a$_$n$($x$).
     </dl>
    ```

Notice the 2 space indentation regarding `<dl>` tag.

Extended description section
-----------------------------

After the usage block, it is expected a brief explanation about the context in which the symbol is used, including examples of use, details of the implementations and possible issues. This section must contain at least one doctest example for each entry in the usage block.






