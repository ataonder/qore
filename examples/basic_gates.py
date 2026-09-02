from qore import Qubit
from qore import H, X, Z

qubit = Qubit()

qubit.apply_gate(X)
print("After X gate:", qubit.state)

qubit.apply_gate(H)
print("After H gate:", qubit.state)

qubit.apply_gate(Z)
print("After Z:", qubit.state)