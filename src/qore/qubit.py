import numpy as np

from .gate import Gate

class Qubit:
    def __init__(self):
        self.state = np.array(
            [1.0 + 0.0j, 0.0 + 0.0j],
            dtype=np.complex128
        )

    def apply_gate(self, gate: Gate) -> None:
        if gate.num_qubits != 1:
            raise ValueError("A single Qubit can only apply singe-qubit gates.")

        self.state = gate.matrix @ self.state

    def __repr__(self) -> str:
        return f"Qubit(state={self.state})"