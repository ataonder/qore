import numpy as np

from qore import Qubit
from qore import H, S, T, X, Y, Z



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


def test_s_gate():
    qubit = Qubit()

    qubit.apply_gate(S)

    expected = np.array([1, 0])

    assert np.allclose(
        qubit.state,
        expected
    )


def test_t_gate():
    qubit = Qubit()

    qubit.apply_gate(T)

    expected = np.array([1, 0])

    assert np.allclose(
        qubit.state,
        expected
    )


def test_x_gate():
    qubit = Qubit()

    qubit.apply_gate(X)

    expected = np.array([0, 1])

    assert np.allclose(
        qubit.state,
        expected
    )


def test_y_gate():
    qubit = Qubit()

    qubit.apply_gate(Y)

    expected = np.array([0, 1j])

    assert np.allclose(
        qubit.state,
        expected
    )


def test_z_gate():
    qubit = Qubit()

    qubit.apply_gate(Z)

    expected = np.array([1, 0])

    assert np.allclose(
        qubit.state,
        expected
    )