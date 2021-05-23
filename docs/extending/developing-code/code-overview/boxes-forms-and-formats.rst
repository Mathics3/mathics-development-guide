.. index:: Boxes
.. index:: Forms

Boxes, Forms, and Formats
=========================

In the introduction to this section we gave the 3-step process converting the input you type into output produced:

* the input string is parsed to ``FullForm``
* The ``FullForm`` S-expression is evaluated giving another S-expression
* The result is formatted to the kind of output desired. Formatting can cause additional evaluations to occurs

Here, we are going to go in more detail over the last step which broadly is formatting.

At the top-level the kind of output you get is dictated by the Form
specified either explicitly or implicitly. See `Forms of Input and
Output
<https://reference.wolfram.com/language/tutorial/TextualInputAndOutput.html#12368>`_.

Formatting a "Form" often causes some parts of the form to be "boxed"
as the S-expression is traversed. You can think of boxing as roughly
the sames as adding parenthesis to Mathematical expressions written in
normal infix notation. The parenthesis serve to mark explicitly
groupings.  This isn't strictly correct, but it gives a rough
idea.

Note that the decision to add a pair of parenthesis or whether to box
is determined by the operation getting performed and the context it is
used. As an S-expression is traversed if the object found is some sort
of object like a ``DateObject``, ``Graphics``, or ``Compilation``
object, those are ripe for boxing, since the internals of those are
somewhat complex or somewhat internal. So note that whether to box or
not is associated with an *object*.  In the Mathics code there will be
a class that ends with ``Box``, like ``CompiledCodeBox`` or
``GraphicsBox``.

Also, how an object is boxed may be influenced by context in which the
expression appears formatted.  For example, if an an image is used
inside of a list, we might choose to show the image as a thumbnail
rather than a full-size image.

After boxing we still have the problem of doing the formatting on everything.

Right now, Form constraint on formatting is somewhat hardcoded. For
example ``MathMLForm`` boxing 2D- Graphics force formatting to SVG.
If instead the Form is ``TeXForm`` then an Aysmptote format is used.
