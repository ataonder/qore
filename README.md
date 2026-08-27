# Qore

A ligthweight quantum computing library built from scratch with Python

> **Early development:** The API is unstable and subject to change.

## Features

Currently, Qore provides:
- Qubit state representation
- Quantum gate abstraction
- Basic single-qubit gates
- NumPy-based state manipulation

## Installation

For installing the **Qore**:
```bash
pip install -e .
```

## Quick Start

```python
from qore import Qubit
from qore import H, X

qubit = Qubit()

qubit.apply_gate(H)
print(qubit.state)

qubit.apply_gate(X)
print(qubit.state)
```

## Roadmap

- [X] Qubit
- [X] Gate abstraction
- [ ] Basic quantum gates
- [ ] Parametric gates
- [ ] Multi-qubit operations
- [ ] Measurement
- [ ] Quantum circuits
- [ ] Circuit optimization
- [ ] Performance backends (NumPy, C/C++, Rust)
- [ ] GPU acceleration

## Development
Qore is currently developed in Python using NumPy. The architecture is intended to support future high-performance C/C++ and Rust backends.  

Run tests with:
```bash
pytest
```

## Contributing
Contributions are welcome.

Before opening a pull request:
1. Create a feature branch.
2. Keep changes focused and minimal.
3. Add or update tests when applicable.
4. Make sure all tests pass with `pytest`.
5. Use clear and descriptive commit messages.

For larger changes, please open an issue first to discuss the proposed approach.

See [CONTRIBUTING.md] for more details.

## License
Qore is licensed under the *MIT License*. See [LICENSE] for more details.