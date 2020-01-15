from typing import List

from math import sqrt, exp, pi

Matrix = List[List[complex]]

class Gate:
    def __init__(self, matrix: Matrix, target: int, control: int = -1, secControl: int = -1):
        self.matrix: Matrix = [[complex(n) for n in row] for row in matrix]
        self.target: int = target
        self.control: int = control
        self.secControl: int = secControl
        self.controlInverse = False
        self.secControlInverse = False
        self.name = self.__class__.__name__
    
    def __repr__(self) -> str:
        return f"{self.name}({self.target}{', ' + str(self.control) if self.control > -1 else ''}{', ' + str(self.secControl) if self.secControl > -1 else ''})"
    
    def __str__(self) -> str:
        return self.__repr__()

class X(Gate):
    def __init__(self, target: int):
        super().__init__([
            [0, 1],
            [1, 0]
        ], target)

class Y(Gate):
    def __init__(self, target: int):
        super().__init__([
            [0, -1j],
            [1j, 0]
        ], target)

class Z(Gate):
    def __init__(self, target: int):
        super().__init__([
            [1, 0],
            [0, -1]
        ], target)

class H(Gate):
    def __init__(self, target: int):
        super().__init__([
            [1/sqrt(2), 1/sqrt(2)],
            [1/sqrt(2), -1/sqrt(2)]
        ], target)

class CX(Gate):
    def __init__(self, target: int, control: int):
        super().__init__([
            [0, 1],
            [1, 0]
        ], target, control)

class CY(Gate):
    def __init__(self, target: int, control: int):
        super().__init__([
            [0, -1j],
            [1j, 0]
        ], target, control)

class CZ(Gate):
    def __init__(self, target: int, control: int):
        super().__init__([
            [1, 0],
            [0, -1]
        ], target, control)

class CCX(Gate):
    def __init__(self, target: int, control: int, secControl: int):
        super().__init__([
            [0, 1],
            [1, 0]
        ], target, control, secControl)

class CCY(Gate):
    def __init__(self, target: int, control: int, secControl: int):
        super().__init__([
            [0, -1j],
            [1j, 0]
        ], target, control, secControl)

class CCZ(Gate):
    def __init__(self, target: int, control: int, secControl: int):
        super().__init__([
            [1, 0],
            [0, -1]
        ], target, control, secControl)

class S(Gate):
    def __init__(self, target: int):
        super().__init__([
            [1, 0],
            [0, 1j]
        ], target)

class St(Gate):
    def __init__(self, target: int):
        super().__init__([
            [1, 0],
            [0, -1j]
        ], target)

class T(Gate):
    def __init__(self, target: int):
        super().__init__([
            [1, 0],
            [0, exp((1j * pi)/4)]
        ], target)

class Tt(Gate):
    def __init__(self, target: int):
        super().__init__([
            [1, 0],
            [0, exp((-1j * pi)/4)]
        ], target)

class SWAP(Gate):
    def __init__(self, target: int, control: int):
        super().__init__([
            [1, 0],
            [0, 1]
        ], target, control)