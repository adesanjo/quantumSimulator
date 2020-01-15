from __future__ import annotations
from typing import Dict, Tuple, List, Optional

import random
from math import sqrt

from gates import Gate

PRINT_STATES = True

class Circuit:
    def __init__(self):
        self.nQubits: int = 2
        self.gates: List[Gate] = []
    
    def setNQubits(self, nQubits: int):
        self.nQubits = nQubits
    
    def addGate(self, gate: Gate):
        self.gates.append(gate)
    
    def run(self, shots: int = 1024) -> Dict[Tuple[int], int]:
        results = {}
        for i in range(shots):
            state = self.runSingle(i == 0)
            bits = f"{state.measure():0{self.nQubits}b}"
            results[bits] = results.get(bits, 0) + 1
        sortedResults = {result: results[result] for result in sorted(results)}
        return sortedResults
    
    def runSingle(self, isFirst: bool) -> List[State]:
        state = State(self.nQubits)
        printStates = isFirst and PRINT_STATES
        if printStates:
            print()
            print(state)
        for gate in self.gates:
            state.applyGate(gate)
            if printStates:
                print()
                print(gate)
                print(state)
                print()
        return state
    
    def __repr__(self) -> str:
        return f"nQubits: {self.nQubits}\ngates: {self.gates}"
    
    def __str__(self) -> str:
        return self.__repr__()

class State:
    def __init__(self, nQubits: int):
        self.nQubits: int = nQubits
        self.coef: List[complex] = [1 + 0j] + [0j] * (2 ** nQubits - 1)
    
    def applyGate(self, gate: Gate):
        newCoef = [0j] * len(self.coef)
        for i, c in enumerate(self.coef):
            if c == 0j:
                continue
            controlPassed = False
            if gate.name == "SWAP":
                controlPassed = True
                val1 = (i >> gate.target) & 1
                val2 = (i >> gate.control) & 1
                s = i & ~(1 << gate.control) & ~(1 << gate.target) | (val1 << gate.control) | (val2 << gate.target)
                newCoef[s] += c
            else:
                val = (i >> gate.target) & 1
                if gate.control == -1:
                    controlVal = 1
                else:
                    controlVal = (i >> gate.control) & 1
                if controlVal ^ gate.controlInverse:
                    if gate.secControl == -1:
                        secControlVal = 1
                    else:
                        secControlVal = (i >> gate.secControl) & 1
                    if secControlVal ^ gate.secControlInverse:
                        controlPassed = True
                        zero = i & ~(1 << gate.target)
                        one = i | (1 << gate.target)
                        newCoef[zero] += c * gate.matrix[val][0]
                        newCoef[one] += c * gate.matrix[val][1]
            if not controlPassed:
                newCoef[i] += c
        self.coef[:] = newCoef
    
    def measure(self) -> int:
        for i, c in enumerate(self.coef):
            if random.uniform(0, sum(map(self.norm, self.coef[i:]))) < self.norm(c):
                return i
        return 0
    
    def norm(self, c: complex) -> float:
        return (c * c.conjugate()).real
    
    def __repr__(self) -> str:
        #return " + ".join(f"{c} |{i:0{self.nQubits}b}⟩" for i, c in enumerate(self.coef))
        return " + ".join(f"{c} |{i:0{self.nQubits}b}⟩" for i, c in enumerate(self.coef) if c != 0j)
    
    def __str__(self) -> str:
        return self.__repr__()