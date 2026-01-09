# main.py
from ast_frontend.parser import parse_source
from ast_frontend.validator import validate
from ast_frontend.lowering import lower
from backend.llvm_emitter import LLVMEmitter

source = """
def add(x, y):
    return x + y
print(add(3, 4))
"""

tree = parse_source(source)
validate(tree)
ir = lower(tree)

emitter = LLVMEmitter(ir)
llvm_ir = emitter.emit()

with open("output.ll", "w") as f:
    f.write(llvm_ir)

print("Generated LLVM IR:")
print(llvm_ir)
