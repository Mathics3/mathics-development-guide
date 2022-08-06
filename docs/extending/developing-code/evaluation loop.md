

The evaluation loop
===================

All the front-ends (django, mathicsscript, mathics, MathicsSession)
build a `Definitions` object, and an `Evaluation` object, that has
the `Definitions` as a property. Then, when an input text is received,
it is parsed by the Mathics Parser and passed to the `evaluate` method
of the `Evaluation` object. This method produces a `Result` object, containing:
* `out`:  a python list containing all the messages and printed strings produced
  during the evaluation
* `result`: a python string containing the formatted version of the result of the evaluation
* `line_no`: a counter stating how many calls to the evaluation method where called over the same Definitions object.
* `last_eval`: the last result of the evaluation (an S-Expression), without formatting.

![](evaluationloop.svg)


Let's focus now on the pass that produces `result` from `last_eval`. In the current implementation, this work is done by
the method `format_output`. This method receives two arguments: the expression and a string, indicating the format.
According to the format, the expression first is wrapped as the argument of a `Format` expression. Then, the method `format`
from the resulting `Expression` object is called, which produces a `Box` expression. This box expression is at the end converted into a string by means of the method `Expression.boxes_to_text`, and is what at the end will be processed and shown in the front end.

So, most of the format is actually performed by the `Expression.format` method. This method does its task in two steps. In a first step, the `self.do_format`  method is called. This method applies all the format rules associated to the head and elements of the expression recursively.
The result of this is a new expression, with certain subexpressions transformed according the rules.
Then, `Expression.format` applies the  `MakeBoxes` rules. `Makeboxes` then produces es formatted expression consisting of `Box` symbols, lists, strings, and BoxConstruct objects. The last ones are a kind of "atoms" that represents the textual representation of a certain Expression (Graphics, Graphics3D, CompìledCode, ...).
If some of the elements of the expression is wrapped inside a `MathMLForm` (`TeXForm`) expression, the corresponding box expression is produced by first applying evaluating `MakeBoxes[element]`, then converted into a `str` by calling the `boxes_to_mathml` (`boxes_to_tex`) method of the resulting Expression, converting it into a `String` and then putting this inside a `RowBox[{}]`.
