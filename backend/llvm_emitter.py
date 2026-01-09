# backend/llvm_emitter.py
from ir.instructions import Const, BinOp, Return

class LLVMEmitter:
    def __init__(self, instructions):
        self.instructions = instructions
        self.lines = []

    def emit(self):
        self.emit_add_function()
        self.emit_main_function()
        return "\n".join(self.lines)

    def emit_add_function(self):
        self.lines.append("define i32 @add(i32 %0, i32 %1) {")
        self.lines.append("entry:")

        for instr in self.instructions:
            if isinstance(instr, Const):
                if instr.target in ("%0", "%1"):
                    continue
                self.lines.append(
                    f"  {instr.target} = add i32 0, {instr.value}"
                )

            elif isinstance(instr, BinOp):
                op_map = {
                    "ADD": "add",
                    "SUB": "sub",
                    "MULT": "mul",
                    "DIV": "sdiv",
                }
                llvm_op = op_map[instr.op]
                self.lines.append(
                    f"  {instr.target} = {llvm_op} i32 {instr.left}, {instr.right}"
                )

            elif isinstance(instr, Return):
                self.lines.append(f"  ret i32 {instr.value}")

        self.lines.append("}")
        self.lines.append("")

    def emit_main_function(self):
        self.lines.append("define i32 @main() {")
        self.lines.append("entry:")
        self.lines.append("  %r = call i32 @add(i32 3, i32 4)")
        self.lines.append("  ret i32 %r")
        self.lines.append("}")
