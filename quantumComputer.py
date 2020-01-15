from circuit import Circuit
import gates as g

FILENAME = "test"

def main():
    with open(FILENAME) as f:
        code = [l.split() for line in f.read().splitlines() if len(l := line.strip()) > 0 and l[0] != "#"]
    circuit = Circuit()
    for inst in code:
        if inst[0] == "qubits":
            circuit.setNQubits(int(inst[1]))
        elif inst[0] == "X":
            circuit.addGate(g.X(int(inst[1])))
        elif inst[0] == "Y":
            circuit.addGate(g.Y(int(inst[1])))
        elif inst[0] == "Z":
            circuit.addGate(g.Z(int(inst[1])))
        elif inst[0] == "H":
            circuit.addGate(g.H(int(inst[1])))
        elif inst[0] == "CX":
            circuit.addGate(g.CX(int(inst[1]), int(inst[2])))
        elif inst[0] == "CY":
            circuit.addGate(g.CY(int(inst[1]), int(inst[2])))
        elif inst[0] == "CZ":
            circuit.addGate(g.CZ(int(inst[1]), int(inst[2])))
        elif inst[0] == "CCX":
            circuit.addGate(g.CCX(int(inst[1]), int(inst[2]), int(inst[3])))
        elif inst[0] == "CCY":
            circuit.addGate(g.CCY(int(inst[1]), int(inst[2]), int(inst[3])))
        elif inst[0] == "CCZ":
            circuit.addGate(g.CCZ(int(inst[1]), int(inst[2]), int(inst[3])))
        elif inst[0] == "S":
            circuit.addGate(g.S(int(inst[1])))
        elif inst[0] == "St":
            circuit.addGate(g.St(int(inst[1])))
        elif inst[0] == "T":
            circuit.addGate(g.T(int(inst[1])))
        elif inst[0] == "Tt":
            circuit.addGate(g.Tt(int(inst[1])))
        elif inst[0] == "SWAP":
            circuit.addGate(g.SWAP(int(inst[1]), int(inst[2])))
    print(circuit)
    print(f"results: {circuit.run()}")

if __name__ == "__main__":
    main()