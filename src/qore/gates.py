import numpy as np

from .gate import Gate

X = Gate(
    "X",
    np.array([
        [0, 1],
        [1, 0]
    ])
)

Y = Gate(
    "Y",
    np.array([
        [0, -1j],
        [1j, 0]
    ])
)

Z = Gate(
    "Z",
    np.array([
        [1, 0],
        [0, -1]
    ])
)

H = Gate(
    "H",
    (1 / np.sqrt(2)) * np.array([
        [1, 1],
        [1, -1]
    ])
)

S = Gate(
    "S",
    np.array([
        [1, 0],
        [0, 1j]
    ])
)

T = Gate(
    "T",
    np.array([
        [1, 0],
        [0, np.exp(1j * np.pi / 4)]
    ])
)

def RX(theta: float) -> Gate:
    cos = np.cos(theta / 2)
    sin = np.sin(theta / 2)

    matrix = np.array([
        [cos, -1j * sin],
        [-1j * sin, cos]
    ])

    return Gate("RX", matrix=matrix)

def RY(theta: float) -> Gate:
    cos = np.cos(theta / 2)
    sin = np.sin(theta / 2)

    matrix = np.array([
        [cos, -sin],
        [sin, cos]
    ])

    return Gate("RY", matrix=matrix)

def RZ(theta: float) -> Gate:
    matrix = np.array([
        [np.exp(-1j * theta / 2), 0],
        [0, np.exp(1j * theta / 2)],
    ])

    return Gate("RZ", matrix=matrix)