import numpy as np
 
from qore import Qubit
from qore import H, X

def test_initial_state():
    qubit = Qubit()

    assert np.allclose(
        qubit.state,
        [1, 0]
    )

def test_x_gate():
    qubit = Qubit()

    qubit.apply_gate(X)

    assert np.allclose(
        qubit.state,
        [0, 1]
    )


def test_h_gate():
    qubit = Qubit()

    qubit.apply_gate(H)

    expected = np.array([
        1 / np.sqrt(2),
        1 / np.sqrt(2)
    ])

    assert np.allclose(
        qubit.state,
        expected
    )


def test_hadamard_twice():
    qubit = Qubit()

    qubit.apply_gate(H)
    qubit.apply_gate(H)

    assert np.allclose(
        qubit.state,
        [1, 0]
    )