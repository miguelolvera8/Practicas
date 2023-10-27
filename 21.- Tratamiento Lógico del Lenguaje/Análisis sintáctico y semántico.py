# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 13:08:56 2023

@author: Jose Cruz TP
"""

class SyntaxError(Exception):
    pass

class SemanticError(Exception):
    pass

class Interpreter:
    def __init__(self):
        self.environment = {'variables': {}}

    def interpret(self, ast):
        if isinstance(ast, list):
            if ast[0] == 'print':
                self.environment['variables'][ast[1]] = ast[2]
                return ast[2]
            elif ast[0] == 'variable_assignment':
                self.environment['variables'][ast[1]] = ast[2]
            else:
                raise SyntaxError("Invalid statement")
        else:
            raise SyntaxError("Unexpected input")

class Parser:
    def __init__(self):
        self.tokens = []
        self.index = 0

    def parse(self, tokens):
        self.tokens = tokens
        self.index = 0
        statements = []
        while self.index < len(self.tokens):
            statements.append(self.statement())
        return statements

    def statement(self):
        if self.tokens[self.index] == 'print':
            self.index += 1
            self.consume('IDENTIFIER')
            self.consume('EQUALS')
            expr = self.expression()
            return ['print', self.tokens[self.index - 2], expr]
        elif self.tokens[self.index] == 'IDENTIFIER':
            name = self.tokens[self.index]
            self.index += 1
            self.consume('EQUALS')
            expr = self.expression()
            return ['variable_assignment', name, expr]
        else:
            raise SyntaxError("Unexpected input")

    def expression(self):
        return self.tokens