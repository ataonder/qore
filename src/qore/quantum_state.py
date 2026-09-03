import numpy as np

from .qubit import Qubit
from .gate import Gate

class QuantumState:
    def __init__(self, num_qubits: int, state=None) -> None:

        if not isinstance(num_qubits, int) or num_qubits < 1:
            raise ValueError("Number of qubits must be a positive integer.")

        self.num_qubits = num_qubits
        dimension = 2 ** num_qubits

        if state is None:
            state = np.zeros(
                dimension,
                dtype=np.complex128
            )
            state[0] = 1.0

        self.state = self._validate_state(state)

    @classmethod
    def from_qubits(cls, *qubits: Qubit) -> "QuantumState":
        if not qubits:
            raise ValueError("At least one qubit is required.")

        state = np.array([1.0 + 0j], dtype=np.complex128)

        for qubit in qubits:
            if not isinstance(qubit, Qubit):
                raise TypeError("All arguments must be Qubit instances.")

            state = np.kron(state, qubit.state)

        return cls(len(qubits), state)

    def _validate_state(self, state):
        state = np.asarray(state, dtype=np.complex128)

        dimension = 2 ** self.num_qubits

        if state.ndim != 1:
            raise ValueError(
                "Quantum state must be a 1-dimensional vector."
            )

        if state.shape[0] != dimension:
            raise ValueError(
                f"Quantum state must contain exactly "
                f"{dimension} amplitudes."
            )

        norm = np.sum(np.abs(state) ** 2)

        if not np.isclose(norm, 1.0):
            raise ValueError(
                "Quantum state must be normalized."
            )

        return state

    def set_state(self, state) -> None:
        self.state = self._validate_state(state)

    @property
    def probabilities(self) -> np.ndarray:
        return np.abs(self.state) ** 2

    def apply_gate(self, gate: Gate, qubit: int = 0) -> None:
        if not isinstance(gate, Gate):
            raise TypeError("Gate must be a Gate instance.")

        if gate.num_qubits != 1:
            raise ValueError(
                "QuantumState.apply_gate currently supports"
                "single-qubit gates only."
            )

        if not isinstance(qubit, int):
            raise TypeError("Qubit index must be an integer.")

        if qubit < 0 or qubit >= self.num_qubits:
            raise IndexError(
                f"Qubit index must be between 0 and {self.num_qubits - 1}."
            )

        stride = 2 ** (self.num_qubits - qubit - 1)
        step = stride * 2

        for start in range(0, len(self.state), step):
            for offset in range(stride):
                i = start + offset
                j = i + stride

                pair = self.state[[i, j]]
                self.state[[i, j]] = gate.matrix @ pair

    def __repr__(self) -> str:
        return (
            f"QuantumState("
            f"\tnum_qubits={self.num_qubits}"
            f"\tstate={self.state}"
            f")"
        )