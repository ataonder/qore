from qore import Qubit

qubit = Qubit.superposition()

print(qubit)
print("State:", qubit.state)
print("Probabilities:", qubit.probabilities)