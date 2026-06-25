from ops.add import add
from ops.avg import avg
from ops.differentiator import differentiator
from ops.divide import divide
from ops.ido import decrease, increase
from ops.int_divide import int_divide
from ops.log import log
from ops.mod import mod
from ops.multiply import multiply
from ops.power import power
from ops.root import root
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
    "root": root,
    "avg": avg,
    "min": min,
}
