import numpy as np

class Gate:
    def __init__(self, name: str, matrix: np.ndarray) -> None:
        matrix = np.asarray(matrix, dtype=np.complex128)   # turning matrix into complex number matrix

        if matrix.ndim != 2:
            raise ValueError("Gate matrix must be 2-dimensional.")

        if matrix.shape[0] != matrix.shape[1]:
            raise ValueError("Gate matrix must be square.")

        if matrix.shape[0] & (matrix.shape[1] - 1):
            raise ValueError("Gate matrix dimension must be power of 2.")

        if not np.allclose(
            matrix.conj().T @ matrix,
            np.eye(matrix.shape[0])
        ):
            raise ValueError("Gate matrix must be unitary.")

        self.name = name
        self.matrix = matrix

    @property
    def num_qubits(self) -> int:
        return int(np.log2(self.matrix.shape[0]))

    def __repr__(self) -> str:
        return f"Gate(name='{self.name}', num_qubits={self.num_qubits})"