# ast_frontend/validator.py
import ast

class Validator(ast.NodeVisitor):

    def visit_Attribute(self, node):
        raise SyntaxError("Attributes are not allowed")

    def visit_Call(self, node):
        raise SyntaxError("Function calls are not allowed")

    def visit_Import(self, node):
        raise SyntaxError("Imports are not allowed")

    def visit_While(self, node):
        raise SyntaxError("While loops are not allowed")

    def visit_For(self, node):
        raise SyntaxError("For loops are not allowed")

    def generic_visit(self, node):
        super().generic_visit(node)


def validate(tree: ast.AST):
    Validator().visit(tree)
