from ops.add import add
from ops.combination import combination
from ops.Combination_with_Repetition import combination_with_repetition
from ops.differentiator import differentiator
from ops.divide import divide
from ops.factorial import factorial
from ops.ido import decrease, increase
from ops.int_divide import int_divide
from ops.log import log
from ops.max import max_num
from ops.min import min_num
from ops.mod import mod
from ops.multiply import multiply
from ops.permutation import permutation
from ops.power import power
from ops.subtract import subtract

operations = {
    "+": add,
    "%": mod,
    "*": multiply,
    "-": subtract,
    "/": divide,
    "//": int_divide,
    "**": power,
    "++": increase,
    "--": decrease,
    "log": log,
    "diff": differentiator,
    "max": max_num,
    "min": min_num,
    "!": factorial,
    "inc": increase,
    "dec": decrease,
    "factorial": factorial,
    "combination": combination,
    "permutation": permutation,
    "combination_with_repetition": combination_with_repetition,
}
