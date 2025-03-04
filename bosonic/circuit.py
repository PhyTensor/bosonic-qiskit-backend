import logging
from typing import Optional, Union

from qiskit import ClassicalRegister, QuantumCircuit, QuantumRegister
from qiskit.circuit import InstructionSet, Qubit

from bosonic.operators import ContinuousVariableOperators
from bosonic.qumoderegister import QumodeRegister

logger = logging.getLogger(__name__)


class ContinuousVariableCircuit(QuantumCircuit):
    def __init__(
        self,
        *registers: Union[QumodeRegister, QuantumRegister, ClassicalRegister],
        name: Optional[str] = None,
        probe_measure: bool = False,
    ) -> None:
        """
        Initialize a ContinuousVariableCircuit circuit.

        Parameters:
            *registers (Union[QumodeRegister, QuantumRegister, ClassicalRegister]): The registers to add to the circuit.
            name: An optional name for the circuit (string).
            probe_measure: An optional boolean indicating whether to perform a probe measurement.

        Raises:
            TypeError: If any of the provided registers are not of the correct type.
            ValueError: If no QumodeRegister is not provided.
        """

        # list of qumode registers tracked by the circuit
        self.qumode_registers: list[QumodeRegister] = []
        # list of quantum (qubit) registers tracked by the circuit
        self.quantum_registers: list[QuantumRegister] = []
        # all registers tracked by the circuit
        self.registers: list[QuantumRegister | ClassicalRegister] = []

        # number of qubits in the circuit
        num_qubits: int = 0

        for reg in registers:
            if isinstance(reg, QumodeRegister):
                self.qumode_registers.append(reg)
                self.registers.append(reg.quantum_register)
                num_qubits += reg.size
            elif isinstance(reg, QuantumRegister): # or isinstance(reg, Qubit):
                self.quantum_registers.append(reg)
                self.registers.append(reg)
                num_qubits += reg.size
            elif isinstance(reg, ClassicalRegister):
                self.registers.append(reg)
            else:
                logger.error(f"Error: Invalid register type provided: {type(reg)}")
                raise TypeError("Invalid register type provided.")

        if len(self.qumode_registers) == 0:
            logger.error("Error: No QumodeRegister provided.")
            raise ValueError("No QumodeRegister provided.")

        logger.info(f"Pass: ContinuousVariableCircuit {name} created with {len(self.registers)} registers.")
        super().__init__(*self.registers, name=name)

        self.operators = ContinuousVariableOperators()


    def get_qumode_register_index(self, qubit: Qubit) -> int:
        """Returns the qumode index for the given qubit. If not found, return -1."""
        for index, qumode_register in enumerate(self.qumode_registers):
            if qubit in qumode_register:
                return index
        raise ValueError(f"Bit {qubit} not found in circuit.")

