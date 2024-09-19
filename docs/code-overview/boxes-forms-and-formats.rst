.. index:: Boxes
.. index:: Forms

Forms, Boxes, and Formats
=========================

In the introduction to this section we gave the 3-step process converting the input you type into output produced:

* the input string is parsed to a ``FullForm`` M-Expression
* The ``FullForm`` M-expression is evaluated giving another M-expression
* The result is formatted to the kind of output desired. Formatting can cause additional evaluations to occur.

Here, we are going to go in more detail over the last step which broadly is formatting.

Forms
-----

At the top-level, the kind of output you get is dictated by the Form
specified either explicitly or implicitly. See `Forms of Input and
Output
<https://reference.wolfram.com/language/tutorial/TextualInputAndOutput.html#12368>`_.

Formatting a "Form" can cause parts of the expression to be "boxed"
as the M-expression is traversed. This is sort of like adding
parenthesis around infix expressions at certain places, but we'll
explain in more detail below.

The Box Model
-------------

Ever since the typesetting system TeX was developed, most full-fledged
formatters follow a two-level approach to formatting output. The
current HTML has a box model that follows this approach.

In the Box-Formatting model, groups of items of a similar category are
"boxed", before final layout.  In "Box"ing, object details which are
not relevant for formatting are hidden. This is good because the
objects themself can have wildly different attributes and properties.

On the other hand, common layout formatting properties, such as the
box dimensions are exposed. Therefore layout is simplified, and
we have the ability to move large collections of items around by
simply positioning the enclosing box.

As with M-Expressions, Boxes can be sequenced and nested.

Within a box, once it is given its initial parameters such as the
dimensions or style attributes, the layout is largely independent of
other boxes in the system.

In the Python code then for each distinct kind of entity, like
``CompiledCode`` or a ``Graphics3D`` object, there will typically be
another class with the the same name but with word ``Box`` added at
the end.  This convention ties to an entity to methods for how to Box
the entity. For example, the ``CompiledCodeBox`` handles boxing for
``CompiledCode`` objects; ``Graphics3DBox`` handles boxing for
``Graphics3D`` objects.

How an object is boxed may be influenced by context in which the
expression appears formatted.  For example, if an an image is used
inside of a list, we might choose to show the image as a thumbnail
rather than a full-size image.

Output Formats
--------------

For each Box type, such as a ``CircleBox`` there can be a formatter for
the kind of output format you want, such as ``SVG`` or ``Asymptote``.

If a Box is not defined for a particular entity, there will be an
enclosing entity which does define a Boxing routine, and that will
need to be be to handle all of the objects inside it whether or not
those objects are boxed.
