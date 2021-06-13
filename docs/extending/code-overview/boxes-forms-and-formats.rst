.. index:: Boxes
.. index:: Forms

Boxes, Forms, and Formats
=========================

In the introduction to this section we gave the 3-step process converting the input you type into output produced:

* the input string is parsed to a ``FullForm`` S-Expression
* The ``FullForm`` S-expression is evaluated giving another S-expression
* The result is formatted to the kind of output desired. Formatting can cause additional evaluations to occur.

Here, we are going to go in more detail over the last step which broadly is formatting.

At the top-level the kind of output you get is dictated by the Form
specified either explicitly or implicitly. See `Forms of Input and
Output
<https://reference.wolfram.com/language/tutorial/TextualInputAndOutput.html#12368>`_.

Formatting a "Form" causes parts of the expression to be "boxed"
as the S-expression is traversed. This is sort of like adding
parenthesis around infix expressions at certain places, but we'll
explain in more detail below.

Ever since the typesetting system
TeX was developed, most full-fledged formatters follow a two-level approach
to formatting output. The current HTML has a box model follows this approach.

In the Box-Formatting model, groups of items of a similar category are
"boxed", before final layout.  Boxes have common properties needed in
formatting such as the boxes dimensions, so this simplifies layout
while giving layout the ability to move large collections of items
around by simply positioning the enclosing box.

As with S-Expressions, Boxes can be sequenced and nested.

Within a box, once it is given its initial parameters such as the
dimensions or style attributes, the layout is largely independent of
other boxes in the system.

In the Python code then for each distinct kind of entity, like
``CompiledCode`` or a ``Graphics3D`` object, there will typically be
another class with the the same name bug with word ``Box`` added at
the end.  This convention ties to an entity to methods for how to Box
the entity. For example, the ``CompiledCodeBox`` handles boxing for
``CompiledCode`` objects; ``Graphics3DBox`` handles boxing for
``Graphics3D`` objects.

How an object is boxed may be influenced by context in which the
expression appears formatted.  For example, if an an image is used
inside of a list, we might choose to show the image as a thumbnail
rather than a full-size image.

We should note that right now, "Form" can severly constrain formatting
and is somewhat hardcoded. For example ``MathMLForm`` boxing 2D-
Graphics forces formatting to SVG. Simlarly if the Form is ``TeXForm``
instead of ``MathMLForm`` then an Aysmptote formatting is performed.

In the future, Forms and formatting will be decoupled better.
