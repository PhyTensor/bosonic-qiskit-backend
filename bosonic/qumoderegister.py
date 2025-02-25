from qiskit import QuantumRegister


class QumodeRegister:
    def __init__(self, num_qumodes: int, num_qubits_per_qumode: int = 2, name: str = "q") -> None:
        """
        Initialise a QumodeRegister object.

        Parameters:
            num_qumodes (int): The number of qumodes in the register.
            num_qubits_per_mode (int): The number of qubits representing each qumode. Defaults to 2.
            name (str): The name of the register. Defaults to "q".
        """
        self.num_qumodes: int = num_qumodes
        self.num_qubits_per_mode: int = num_qubits_per_qumode
        self.name: str = name

        self.size: int = self.num_qumodes * self.num_qubits_per_mode
        self.cutoff: int = 2**self.num_qubits_per_mode

        self.quantum_register: QuantumRegister = QuantumRegister(size=self.size, name=self.name)


    @staticmethod
    def calculate_cutoff(num_qubits_per_mode: int) -> int:
        return 2**num_qubits_per_mode


    def get_qumode_index(self, qubit: int) -> int:
        """Returns the qumode index of the qubit."""
        qubit_index: int = self.quantum_register.index(qubit)
        return qubit_index // self.num_qubits_per_mode


    def __len__(self) -> int:
        """Returns the number of qumodes in the qumode register."""
        return self.num_qumodes

