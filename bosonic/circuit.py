from qiskit import ClassicalRegister, QuantumCircuit, QuantumRegister

from bosonic import QumodeRegister


class ContinuousVariableCircuit(QuantumCircuit):
    def __init__(
        self,
        qumode_register: QumodeRegister,
        quantum_register: QuantumRegister,
        classical_register: ClassicalRegister,
        name: str = str(),
    ) -> None:
        super().__init__(
            qumode_register.quantum_register,
            quantum_register,
            classical_register,
            name=name
        )

        self.qumode_register: QumodeRegister = qumode_register
        self.quantum_register: QuantumRegister = quantum_register
        self.classical_register: ClassicalRegister = classical_register

