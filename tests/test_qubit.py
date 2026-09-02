import numpy as np
import pytest

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


def test_set_state():
    qubit = Qubit()
    qubit.set_state([0, 1])

    np.testing.assert_array_equal(
        qubit.state,
        np.array([0, 1], dtype=np.complex128)
    )


def test_set_state_superposition():
    qubit = Qubit()
    state = [1 / np.sqrt(2), 1 / np.sqrt(2)]

    qubit.set_state(state)

    np.testing.assert_allclose(qubit.state, state)


def test_set_state_complex():
    qubit = Qubit()
    state = [1 / np.sqrt(2), 1j / np.sqrt(2)]

    qubit.set_state(state)

    np.testing.assert_allclose(qubit.state, state)


def test_set_state_invalid_dimension():
    qubit = Qubit()

    with pytest.raises(ValueError):
        qubit.set_state([1, 0, 0])


def test_set_state_invalid_normalization():
    qubit = Qubit()

    with pytest.raises(ValueError):
        qubit.set_state([1, 1])


def test_probabilities_zero_state():
    qubit = Qubit([1, 0])

    np.testing.assert_allclose(
        qubit.probabilities,
        [1.0, 0.0]
    )


def test_probabilities_one_state():
    qubit = Qubit([0, 1])

    np.testing.assert_allclose(
        qubit.probabilities,
        [0.0, 1.0]
    )


def test_probabilities_superposition():
    qubit = Qubit([
        1 / np.sqrt(2),
        1 / np.sqrt(2)
    ])

    np.testing.assert_allclose(
        qubit.probabilities,
        [0.5, 0.5]
    )


def test_probabilities_complex_state():
    qubit = Qubit([
        1 / np.sqrt(2),
        1j / np.sqrt(2)
    ])

    np.testing.assert_allclose(
        qubit.probabilities,
        [0.5, 0.5]
    )


def test_measure_zero_state():
    qubit = Qubit([1, 0])

    assert qubit.measure() == 0
    np.testing.assert_allclose(qubit.state, [1, 0])


def test_measure_one_state():
    qubit = Qubit([0, 1])

    assert qubit.measure() == 1
    np.testing.assert_allclose(qubit.state, [0, 1])


def test_measure_superposition():
    results = set()

    for _ in range(100):
        qubit = Qubit()
        qubit.apply_gate(H)
        results.add(qubit.measure())

    assert results == {0, 1}


def test_measure_collapses_state():
    qubit = Qubit()
    qubit.apply_gate(H)

    result = qubit.measure()

    if result == 0:
        np.testing.assert_allclose(qubit.state, [1, 0])
    else:
        np.testing.assert_allclose(qubit.state, [0, 1])