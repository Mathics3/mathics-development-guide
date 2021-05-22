.. index:: Boxes
.. index:: Forms

Boxes, Forms, and Formats
=========================

In the introduction to this section we gave the 3-step process converting the input you type into output produced:

* the input string is parsed to ``FullForm``
* The ``FullForm`` S-expression is evaluated giving another S-expression
* The result is formatted to the kind of output desired. Formatting can cause additional evaluations to occurs

Here, we are going to go in more detail over the last step which broadly is formatting.

At the top-level the kind of output you get is dictated by the Form specified either explicitly or implicitly. See `Forms of Input and Output <https://reference.wolfram.com/language/tutorial/TextualInputAndOutput.html#12368>`_.

Formatting a "Form" often causes some parts of the form to be "boxed" as the S-expression is traversed. You can think of boxing as akin to adding parenthesis to Mathematical expressions written in normal infix notation. The parenthesis service to mark explicitly groupings. Other than that it does not change the meaning.

In formatting an S-expression in Mathics, Boxing in adding context to the expression may constrain how an expression is formatted.
For example, if an an image is used inside of a list, we might choose to show the image as a thumbnail rather than a full-size image.

Once a form constained by context boxes provide is determined, we still have the problem of doing the formatting.

Right now, Form constraint on formatting is somewhat hardcoded. For example ``MathMLForm`` boxing Graphics force formatting to SVG.
But if the Form is ``TeXForm`` then an Aysmptote format is used.
