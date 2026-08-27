# Contributing to Qore

Thank you for your interest in contributing to Qore.

## Getting Started

Clone the repository and install the development dependencies:
```bash
git clone https://github.com/ataonder/qore.git
cd qore
python -m pip install -e ".[dev]"
```

## Development
Create a feature branch:
```bash
git checkout -b feat/your-feature
```

Run the test suite before submitting a pull request:
```bash
pytest
```

## Pull Requests
Please keep pull requests focused on a single change whenever possible.

Include tests for new functionality and make sure existing tests continue to pass.

For significant architectual changes, open an issue before starting implementation.

## Commit Messages

Use clear commit messages following the Conventional Commits style:
```
feat: add Hadamard gate
fix: correct gate validation
test: add qubit state tests
refactor: simplify gate representation
docs: update installation guide
```

## Code Style

Keep the code simple, readable, and consistent with the existing project structure.