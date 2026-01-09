# ir/instructions.py
from dataclasses import dataclass

class Instr:
    pass

@dataclass
class Const(Instr):
    target: str
    value: int

@dataclass
class BinOp(Instr):
    target: str
    op: str
    left: str
    right: str

@dataclass
class Return(Instr):
    value: str
