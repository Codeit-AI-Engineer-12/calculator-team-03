from ops.add import add
from ops.divide import divide
from ops.ido import decrease, increase
from ops.int_divide import int_divide
from ops.mod import mod
from ops.multiply import multiply
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
}
