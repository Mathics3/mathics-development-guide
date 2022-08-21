First Skeletal version
=======================

.. contents::
   :depth: 1
   :local:

Armed with the information above we are now ready to draft the virst version of this.

Mathics built-in symbols are defined by writing a class which is based off of the class ``Builtin``.

The docstring for this class lists

* The common name for this, if a corresponding match can be found Wikipedia, use that name and link to it
* links to the WMA reference we found before.
* If there is a corresponding SymPy, mpmath, or SciPy function, then link to that
* A HTML "definition list" to enclose the defintion of each form that can appear
* User-Oriented Examples

``Undefined`` Title line
-------------------------

Here, there is no Wikipedia common name, so we'll go with the Mathematica-like description "Undefined symbol or value". The WMA link is put in parenthesis after that.
See the next case study :ref:`Adding Builtin Function ``KroneckerProduct``` for an example where we fill a Wikipedia and SymPy entry.

To start out then we have:


.. code-block:: python


    class Undefined(Builtin):
        """
        Undefined symbol/value (<url>:WMA: https://reference.wolfram.com/language/ref/Undefined.html</url>)
	...
	"""

Due to current limitations in our homegrown documentation system, the title line has to appear as one unbroken line. To accomodate this, We have arrange ``pylint`` to ignore long lines.

``Undefined`` Symbol Definition
-------------------------------

Let us filling out the docstring further, the line above with ``...`` in it.

After the title line, we get to the definition list part where we list the forms that this can appear. Here there is just one form ``Undefined``

.. code-block:: python

    class Undefined(Builtin):
        """
        Undefined symbol/value (<url>:WMA: https://reference.wolfram.com/language/ref/Undefined.html</url>)

        <dl>
          <dt>'Undefined[]'
          <dd>a symbol that represents a quantity with no defined value.
        </dl>

    	...
	"""

User-Oriented Examples
----------------------

Now we get to the example portion of the docstring. We will copy an example found in the WMA documentation for this and add an example that shows the attributes.

.. code-block:: python


    class Undefined(Builtin):
        """
        Undefined symbol/value (<url>:WMA: https://reference.wolfram.com/language/ref/Undefined.html</url>)

        <dl>
         <dt>'Undefined'
         <dd>a symbol that represents a quantity with no defined value.
    </dl>

    >> ConditionalExpression[a, False]
     = Undefined
    >> Attributes[Undefined]
     = {Protected}
    """
    # ...

In a later we will describe in more detail what the lines with ``>>`` and ``=`` below that mean.

Next:

.. toctree::
   :maxdepth: 1

   checking
