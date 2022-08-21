Write a non-working basic skeleton
==================================

Armed with information from the previous sections:

* Where the function belongs: "Mathematical Operations", and
* Information from WMA and SymPy on what should be implemented and how it hooks into an existing library function

we are now ready to being with a skeletal version from which we can fill out later.

"Mathematical Operations" is located in directory ``mathics/builtin/vectors/math_ops.py``.

.. code-block:: python

    # TODO: Curl, Div

so we have noted the need for that here already. Good. Let's remove Curl from that list.

Can this be done in Mathics itself?
------------------------------------

Curl is defined as:

.. math::

    \partial f_2 / \partial x_1 - \partial f_1 / \partial x_2

for two-dimensional vectors and:

.. math::

    ( \partial f_3 / \partial x_2 - \partial f_2 / \partial x_3, \ \ %
      \partial f_1 / \partial x_3 - \partial f_3 / \partial x_1, \ \ %
      \partial f_2 / \partial x_1 - \partial f_1 / \partial x_2 )

for three-dimensional vectors.


First Basic non-working version
--------------------------------

Looking at other built-in Mathics Functions, ``Cross`` seems like it might make as good model. So let us use that.

Here is the contents of the first cut for that file/module:


.. code-block::

  class Curl(SympyFunction):
      """
      <url>:Curl: https://en.wikipedia.org/wiki/Curl_(mathematics)</url> (<url>:SymPy: https://docs.sympy.org/latest/modules/vector/api/vectorfunctions.html#sympy.vector.curl</url>, <url>:WMA: https://reference.wolfram.com/language/ref/Curl.html</url>)

      <dl>
        <dt>'Curl[{$f1$, $f2$}, {$x1$, $x2$}]'
        <dd>returns the curl $df2$/$dx1$ - $df1$/$dx2$

        <dt>'Curl[{$f1$, $f2$, $f3} {$x1$, $x2$, $x3}]'
        <dd>returns the curl ($df3$/$dx2$ - $df2$/$dx3$, $dx3$/$df$3 - $df3$/$dx1$, $df2$/$df1$ - $df1$/$dx2$)
      </dl>

      >> Curl[{y, -x}, {x, y}]
       = -2
      """

      attributes = A_PROTECTED | A_READ_PROTECTED
      summary_text = "Kronecker product"
      sympy_name = "curl"

      def apply(self,f1, f2, x1, x2, evaluation: Evaluation):
          "Curl[{f1_,f2_}, {x1_, x2}]"
          sympy_mi = ... # to_sympy()
          return from_sympy(curl(sympy_mi))


Now let's test. Go into Django and type "Mathematical Operations" in the documentation section and you should see "Curl" appear first before "Cross". And note that it has the summary text that we added above.

Click on "Curl" in that list and we now see all of the information in the docstring we just entered.

You should check the following links shown in blue:

* Curl,
* SymPy, and
* WMA
