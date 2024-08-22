from qprimer.core.pure import PureState
import random

try:
    from qulacs import QuantumCircuit as QCircuit, QuantumState
    from qulacs.gate import Measurement
except ImportError as e:
    print(e, "To use QulacsPureState, you need to install qulacs")


def from_bitstring(str):
    array = []
    for c in reversed(str):
        array.append(int(c))
    return array


class QulacsPureState(PureState):
    def __init__(self, num_qubits):
        super().__init__(num_qubits)
        self.circuit = QCircuit(num_qubits)
        self._state = QuantumState(self.num_qubits)

    def copy(self):
        result = QulacsPureState(self.num_qubits)
        result.circuit = self.circuit.copy()
        return result

    def h(self, index):
        self.circuit.add_H_gate(index)

    def s(self, index):
        self.circuit.add_S_gate(index)

    def t(self, index):
        self.circuit.add_T_gate(index)

    def sdag(self, index):
        self.circuit.add_Sdag_gate(index)

    def x(self, index):
        self.circuit.add_X_gate(index)

    def y(self, index):
        self.circuit.add_Y_gate(index)

    def z(self, index):
        self.circuit.add_Z_gate(index)

    def rx(self, theta, index):
        self.circuit.add_RX_gate(index, -theta)

    def ry(self, theta, index):
        self.circuit.add_RY_gate(index, -theta)

    def rz(self, theta, index):
        self.circuit.add_RZ_gate(index, -theta)

    def cnot(self, c_index, t_index):
        self.circuit.add_CNOT_gate(c_index, t_index)

    def cy(self, c_index, t_index):
        self.sdag(t_index)
        self.cx(c_index, t_index)
        self.s(t_index)

    def cz(self, c_index, t_index):
        self.circuit.add_CZ_gate(c_index, t_index)

    def measure(self, index):
        """
        :param measures specific one qubit and returns the value.
        :return:
        """
        state = self._state.copy()
        self.circuit.add_gate(Measurement(index, index))
        self.circuit.update_quantum_state(state)
        self._state = state
        self.circuit = QCircuit(self.num_qubits)
        return state.get_classical_value(index)

    def barrier(self):
        pass

    def draw(self, output="mpl"):
        pass

    def draw_and_show(self):
        pass

    def get_state(self):
        state = self._state.copy()
        self.circuit.update_quantum_state(state)
        return state

    def get_state_vector(self):
        state = self._state.copy()
        self.circuit.update_quantum_state(state)
        return state.get_vector()
