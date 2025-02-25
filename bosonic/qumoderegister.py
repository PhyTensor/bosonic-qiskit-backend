from qiskit import QuantumRegister


class QumodeRegister:
    def __init__(self, num_qumodes: int, qubits_per_qumode: int = 2, name: str = "q") -> None:
        """
        Initialise a QumodeRegister object.

        Parameters:
            num_qumodes (int): The number of qumodes in the register.
            qubits_per_mode (int): The number of qubits representing each qumode. Defaults to 2.
            name (str): The name of the register. Defaults to "q".
        """
        self.num_qumodes: int = num_qumodes
        self.qubits_per_mode: int = qubits_per_qumode
        self.name: str = name

        self.size: int = self.num_qumodes * self.qubits_per_mode
        self.cutoff: int = 2**self.qubits_per_mode

        self.quantum_register: QuantumRegister = QuantumRegister(size=self.size, name=self.name)


    @staticmethod
    def calculate_cutoff(num_qubits_per_mode: int) -> int:
        return 2**num_qubits_per_mode

