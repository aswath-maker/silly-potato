# ast_frontend/parser.py
import ast

def parse_source(source: str) -> ast.Module:
    return ast.parse(source)
