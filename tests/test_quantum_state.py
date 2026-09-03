import numpy as np
import pytest

from qore import Qubit
from qore import QuantumState
from qore import X, H


def test_initial_state():
    state = QuantumState(1)

    np.testing.assert_allclose(
        state.state,
        [1, 0]
    )


def test_two_qubit_initial_state():
    state = QuantumState(2)

    np.testing.assert_allclose(
        state.state,
        [1, 0, 0, 0]
    )


def test_state_dimension():
    for num_qubits in range(1, 5):
        state = QuantumState(num_qubits=num_qubits)

        assert len(state.state) == 2 ** num_qubits


def test_custom_state():
    state = QuantumState(
        2,
        [1 / np.sqrt(2), 0, 0, 1 / np.sqrt(2)]
    )

    np.testing.assert_allclose(
        state.state,
        [1 / np.sqrt(2), 0, 0, 1 / np.sqrt(2)]
    )


def test_probabilities():
    state = QuantumState(
        2,
        [1 / np.sqrt(2), 0, 0, 1 / np.sqrt(2)]
    )

    np.testing.assert_allclose(
        state.probabilities,
        [0.5, 0, 0, 0.5]
    )


def test_invalid_num_qubits():
    with pytest.raises(ValueError):
        QuantumState(0)

    with pytest.raises(ValueError):
        QuantumState(-1)


def test_invalid_state_dimension():
    with pytest.raises(ValueError):
        QuantumState(2, [1, 0])


def test_invalid_state_normalization():
    with pytest.raises(ValueError):
        QuantumState(2, [1, 1, 0, 0])


def test_from_qubits():
    q1 = Qubit.zero()
    q2 = Qubit.one()

    state = QuantumState.from_qubits(q1, q2)

    np.testing.assert_allclose(
        state.state,
        [0, 1, 0, 0]
    )


def test_from_three_qubits():
    q1 = Qubit.zero()
    q2 = Qubit.one()
    q3 = Qubit.zero()

    state = QuantumState.from_qubits(q1, q2, q3)

    np.testing.assert_allclose(
        state.state,
        [0, 0, 1, 0, 0, 0, 0, 0]
    )


def test_from_superposition_qubits():
    q1 = Qubit.superposition()
    q2 = Qubit.zero()

    state = QuantumState.from_qubits(q1, q2)

    np.testing.assert_allclose(
        state.state,
        [
            1 / np.sqrt(2),
            0,
            1 / np.sqrt(2),
            0
        ]
    )


def test_from_qubits_requires_qubit():
    with pytest.raises(TypeError):
        QuantumState.from_qubits(Qubit.zero(), [1, 0])


def test_from_qubits_requires_at_least_one_qubit():
    with pytest.raises(ValueError):
        QuantumState.from_qubits()


def test_apply_gate_zero_state():
    state = QuantumState(1)

    state.apply_gate(X)

    np.testing.assert_allclose(
        state.state,
        [0, 1]
    )


def test_apply_gate_hadamard():
    state = QuantumState(1)

    state.apply_gate(H)

    np.testing.assert_allclose(
        state.state,
        [1 / np.sqrt(2), 1 / np.sqrt(2)]
    )


def test_apply_gate_two_qubits_first_qubit():
    state = QuantumState(2)

    state.apply_gate(H, qubit=0)

    np.testing.assert_allclose(
        state.state,
        [
            1 / np.sqrt(2),
            0,
            1 / np.sqrt(2),
            0
        ]
    )


def test_apply_gate_two_qubits_second_qubit():
    state = QuantumState(2)

    state.apply_gate(H, qubit=1)

    np.testing.assert_allclose(
        state.state,
        [
            1 / np.sqrt(2),
            1 / np.sqrt(2),
            0,
            0
        ]
    )


def test_apply_gate_preserves_normalization():
    state = QuantumState(3)

    state.apply_gate(H, qubit=0)
    state.apply_gate(X, qubit=1)
    state.apply_gate(H, qubit=2)

    assert np.isclose(
        np.sum(np.abs(state.state) ** 2),
        1.0
    )


def test_apply_gate_invalid_gate():
    state = QuantumState(2)

    with pytest.raises(TypeError):
        state.apply_gate([[1, 0], [0, 1]])


def test_apply_gate_invalid_qubit_index():
    state = QuantumState(2)

    with pytest.raises(IndexError):
        state.apply_gate(H, qubit=2)

    with pytest.raises(IndexError):
        state.apply_gate(H, qubit=-1)


def test_apply_gate_invalid_qubit_type():
    state = QuantumState(2)

    with pytest.raises(TypeError):
        state.apply_gate(H, qubit=0.5)