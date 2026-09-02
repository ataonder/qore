import numpy as np

from .gate import Gate

class Qubit:
    def __init__(self, state: None | list | np.ndarray =None):
        if state is None:
            state = [1, 0]

        self.state = self._validate_state(state)

    @staticmethod
    def _validate_state(state):
        state = np.asarray(state, dtype=np.complex128)

        if state.ndim != 1:
            raise ValueError("Qubit state must be a 1-dimensional vector.")

        if state.shape[0] != 2:
            raise ValueError("Qubit state must contain exactly 2 amplitudes.")

        norm = np.sum(np.abs(state) ** 2)

        if not np.isclose(norm, 1.0):
            raise ValueError("Qubit state must be normalized.")

        return state

    @property
    def probabilities(self) -> np.ndarray:
        return np.abs(self.state) ** 2

    def apply_gate(self, gate: Gate) -> None:
        if gate.num_qubits != 1:
            raise ValueError("A single Qubit can only apply singe-qubit gates.")

        self.state = gate.matrix @ self.state

    def set_state(self, state) -> None:
        self.state = self._validate_state(state)

    def __repr__(self) -> str:
        return f"Qubit(state={self.state})"