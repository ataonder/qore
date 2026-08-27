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