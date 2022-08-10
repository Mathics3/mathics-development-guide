Write a non-working basic skeleton
==================================

Armed with information from the previous sections:

* Where the function belongs: "Vector Space Operations", and
* Information from WMA and SymPy on what should be implemented and how it hooks into an existing library function

we are now ready to being with a skeletal version from which we can fill out later.

As noted before, "Vector Space Operations" is located in directory ``mathics/builtin/vectors/vector_space_operations.py``.

Down that the bottom of that file we have:

.. code-block:: python

   # TODO: Orthogonalize, KroneckerProduct

so we have noted the need for that here already. Good. Let's remove KroneckerProduct from that list.

None of the other built-in Mathics Functions serve as good model to copy from so, we'll use a combination ``Transpose`` and ``PauliMatrix``. The former function is selected because it takes a Matrix parameter, and PauliMatrix function because it is a SymPy function which was recently created at the time of this wriging.

Here is the contents of the first cut for that file/module:


.. code-block::

  class KroneckerProduct(SympyFunction):
      """
      <url>:Kronecker product: https://en.wikipedia.org/wiki/Kronecker_product</url> (<url>:SymPy: https://docs.sympy.org/latest/modules/physics/quantum/tensorproduct.html</url>, <url>:WMA: https://reference.wolfram.com/language/ref/KroneckerProduct.html</url>)

      <dl>
        <dt>'KroneckerProduct[$m1$, $m2$, ...]'
        <dd>returns the Kronecker product of the arrays $mi$
      </dl>

      >> av = Array[Subscript[a, ##] &, {2}]; bv = Array[Subscript[b, ##] &, {2}];
      >> KroneckerProduct[av, bv]
       = {{{a1, b1}, {a2, b2}}, {{a2, b1}, {a2, b2}}}
      """

      attributes = A_PROTECTED | A_READ_PROTECTED
      summary_text = "Kronecker product"
      sympy_name = "physics.quantum.TensorProduct"

      def apply(self, mi: ListExpression, evaluation: Evaluation):
          "KroneckerProduct[mi__]"
          sympy_mi = mi.to_sympy()
          return from_sympy(TensorProduct(sympy_mi))


In the above, I needed to add imports for ``SympyFunction``, ``ListExpression``, ``Evaluation`` and other places. Examples of these of of course can be adapted from the place where you copied the code from.

Now let's go over the changes...

The line:

.. code-block:: python

  class KroneckerProduct(SympyFunction):

is pretty simple, I just changed the name from ``PauliMatrix``. Please
note that class names are in alphabetic order. So this comes first before the ``Normalize`` class

The url lines in the docstring

.. code-block:: python

    """
      ...
      <url>:Kronecker product: https://en.wikipedia.org/wiki/Kronecker_product</url> (<url>:SymPy: https://docs.sympy.org/latest/modules/physics/quantum/tensorproduct.html</url>, <url>:WMA: https://reference.wolfram.com/language/ref/KroneckerProduct.html</url>)
   """

Were also adapted from ``PauliMatrix``. I looked up in Wikipedia the link for Kronecker project. However we had previously looked up links for SymPy and WMA.

Now consider lines:

.. code-block:: python

      attributes = A_PROTECTED | A_READ_PROTECTED
      summary_text = "Kronecker product"
      sympy_name = "physics.quantum.TensorProduct"

Setting the class variable ``attributes`` sets the Mathics Function attributes.
``A_PROTECTED`` if the mask values for ``Protected`` which prevents the function from getting modified without further action beforehand, and ``A_READ_PROTECTED`` is the mask value or ``ReadProtected`` which prevents attributes from being seen. These may be the default attribute settings, but I like to be expliicit.

``summary_text`` is the name that will appear in Django when showing this function in the list of functions for "Vector Space Operations". If there is a verb given, use the active tense, e.g. "compute" instead of "computes", "perform" instead of "performs", and so on.

``sympy_name`` like ``attributes`` here is technically not needed. However it severs to document correspondenceds between Mathics builtins functions and their SymPy equivalent and this information may be extracted and used elsewhere in the future.


...

Now let's test. Go into Django and type "Vector Space Operations" in the documentation section and you should see KroneckerProducgt appear first beore Normalize. And note that it has the summary text that we added above.

Click on "KroneckerProduct" in that list and we now see all of the information in the docstring we just entered.

In particular click on "KronckerProduct" and you should go to the wikipedia page. So the same for "Sympy" and "WMA".


...

.. code-block::

  $ mathics

  Mathics 5.0.3dev0
  on CPython 3.8.12 (heads/v2.3.4.1_release:4a6b4d3504, Jun  3 2022, 15:46:12)
  ...

  In[1]:= ?KroneckerProduct
  Kronecker product
  Out[1]= Null

  In[2]:= av = Array[Subscript[a, ##] &, {2}]; bv = Array[Subscript[b, ##] &, {2}];
  Out[2]= None

  In[3]:= av
  Out[3]= {Subscript[a, 1], Subscript[a, 2]}

  In[4]:= bv
  Out[4]= {Subscript[b, 1], Subscript[b, 2]}

  In[5]:= Cases[{av, bv}, __]
  Out[5]= {{Subscript[a, 1], Subscript[a, 2]}, {Subscript[b, 1], Subscript[b, 2]}}

  In[6]:= KroneckerProduct[av, bv]
  Out[6]= Sequence[av, bv]
