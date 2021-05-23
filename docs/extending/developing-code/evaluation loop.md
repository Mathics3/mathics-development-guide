

The evaluation loop
===================

All the front-ends (django, mathicsscript, mathics, MathicsSession)
build a `Definitions` object, and an `Evaluation` object, that has
the `Definitions` as a property. Then, when an input text is received,
it is parsed by the Mathics Parser and passed to the `evaluate` method
of the `Evaluation` object. This method produces a `Result` object, containing:
* out:  a python list containing all the messages and printed strings produced
  during the evaluation
* result: a python string containing the formatted version of the result of the evaluation
* line_no: a counter stating how many calls to the evaluation method where called over the same Definitions object.
* last_eval: the last result of the evaluation (an S-Expression), without formatting.




![](evaluation loop.png)
