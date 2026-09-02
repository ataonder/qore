from qore import Qubit

qubit = Qubit.superposition()

print("Before measurement:", qubit.state)

result = qubit.measure()

print("Measurement result:", result)
print("After measurement:", qubit.state)