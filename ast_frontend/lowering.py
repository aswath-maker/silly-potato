# ast_frontend/lowering.py
import ast

from ir.instructions import Const, BinOp, Return
from utils.temp import TempGen

class IRBuilder:
    def __init__(self):
        self.instructions = []
        self.tempgen = TempGen()
        self.env = {}  # variable name → temp

    def lower_expr(self, node):
        if isinstance(node, ast.Constant):
            temp = self.tempgen.new()
            self.instructions.append(Const(temp, node.value))
            return temp

        if isinstance(node, ast.Name):
            return self.env[node.id]

        if isinstance(node, ast.BinOp):
            left = self.lower_expr(node.left)
            right = self.lower_expr(node.right)

            temp = self.tempgen.new()
            op = type(node.op).__name__.upper()

            self.instructions.append(
                BinOp(temp, op, left, right)
            )
            return temp

        raise NotImplementedError(f"Unsupported expression: {node}")

    def lower_expr(self, node):
        if isinstance(node, ast.Constant):
            temp = self.tempgen.new()
            self.instructions.append(Const(temp, node.value))
            return temp

        if isinstance(node, ast.Name):
            return self.env[node.id]

        if isinstance(node, ast.BinOp):
            left = self.lower_expr(node.left)
            right = self.lower_expr(node.right)

            temp = self.tempgen.new()
            op = type(node.op).__name__.upper()

            self.instructions.append(
                BinOp(temp, op, left, right)
            )
            return temp

        raise NotImplementedError(f"Unsupported expression: {node}")

    def lower_stmt(self, node):
        if isinstance(node, ast.Return):
            value = self.lower_expr(node.value)
            self.instructions.append(Return(value))
            return

        raise NotImplementedError(f"Unsupported statement: {node}")

    def lower_function(self, func):
        for arg in func.args.args:
            temp = self.tempgen.new()
            self.env[arg.arg] = temp
            self.instructions.append(Const(temp, 0))  # placeholder arg

        for stmt in func.body:
            self.lower_stmt(stmt)

        return self.instructions

def lower(tree: ast.Module):
    func = tree.body[0]
    builder = IRBuilder()
    return builder.lower_function(func)
