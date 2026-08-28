import numpy as np

from qore import Qubit
from qore import H, S, T, X, Y, Z, RX, RY, RZ



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


def test_rx_gate():
    theta = np.pi / 2

    expected = np.array([
        [np.cos(theta / 2), -1j * np.sin(theta / 2)],
        [-1j * np.sin(theta / 2), np.cos(theta / 2)],
    ])

    gate = RX(theta)

    assert np.allclose(
        gate.matrix,
        expected
    )


def test_ry_gate():
    theta = np.pi / 2

    expected = np.array([
        [np.cos(theta / 2), -np.sin(theta / 2)],
        [np.sin(theta / 2), np.cos(theta / 2)],
    ])

    gate = RY(theta)

    assert np.allclose(
        gate.matrix,
        expected
    )


def test_rz_gate():
    theta = np.pi / 2

    expected = np.array([
        [np.exp(-1j * theta / 2), 0],
        [0, np.exp(1j * theta / 2)],
    ])

    gate = RZ(theta)


def test_rx_gate_is_unitary():
    gate = RX(0.73)

    assert np.allclose(
        gate.matrix.conj().T @ gate.matrix,
        np.eye(2)
    )


def test_ry_gate_is_unitary():
    gate = RY(0.73)

    assert np.allclose(
        gate.matrix.conj().T @ gate.matrix,
        np.eye(2)
    )


def test_rz_gate_is_unitary():
    gate = RZ(0.73)

    assert np.allclose(
        gate.matrix.conj().T @ gate.matrix,
        np.eye(2)
    )


def test_rx_gate_zero_is_identity():
    gate = RX(0)

    assert np.allclose(
        gate.matrix,
        np.eye(2)
    )


def test_ry_gate_zero_is_identity():
    gate = RY(0)

    assert np.allclose(
        gate.matrix,
        np.eye(2)
    )


def test_rz_gate_zero_is_identity():
    gate = RZ(0)

    assert np.allclose(
        gate.matrix,
        np.eye(2)
    )