from qprimer.core.pure import PureState
import random

try:
    from qulacs import QuantumCircuit as QCircuit, QuantumState
    from qulacs.gate import Measurement
except ImportError as e:
    print(e, "To use QulacsPureState, you need to install qulacs")


def from_bitstring(str):
    array = []
    for c in str:
        array.append(int(c))
    return array


class QulacsPureState(PureState):
    def __init__(self, num_qubits, gpu=False):
        super().__init__(num_qubits)
        self.gpu = gpu
        self.circuit = QCircuit(num_qubits)
        self._ref_state = None

    def copy(self):
        result = QulacsPureState(self.num_qubits)
        result.circuit = self.circuit.copy()
        result._ref_state = self._ref_state
        return result

    def add_gate(self, gate):
        self.circuit.add_gate(gate)

    def h(self, index):
        self.circuit.add_H_gate(index)

    def s(self, index):
        self.circuit.add_S_gate(index)

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
        state = self._get_ref_state()
        self.circuit.add_gate(Measurement(index, index))
        self.circuit.update_quantum_state(state)
        self._ref_state = state
        self.circuit = QCircuit(self.num_qubits)
        return state.get_classical_value(index)

    def barrier(self):
        pass

    def draw(self, output="mpl"):
        pass

    def draw_and_show(self):
        pass

    def get_samples(self, nshot):
        state = self._get_ref_state()
        self.circuit.update_quantum_state(state)
        rs = []
        dictionary = {}
        for sample in state.sampling(nshot, random_seed=random.randint(0, 100000)):
            if sample in dictionary:
                rs.append(dictionary[sample])
            else:
                r = from_bitstring(self._get_bin(sample, self.num_qubits))
                dictionary[sample] = r
                rs.append(r)
        return rs

    def get_counts(self, nshot):
        state = self._get_ref_state()
        self.circuit.update_quantum_state(state)
        r = {}
        n_q = state.get_qubit_count()
        for sample in state.sampling(nshot, random_seed=random.randint(0, 100000)):
            b = self._get_bin(sample, n_q)
            if b not in r:
                r[b] = 0
            r[b] = r[b] + 1
        return r

    def get_state(self):
        state = self._get_ref_state()
        self.circuit.update_quantum_state(state)
        return state

    def get_state_vector(self):
        state = self._get_ref_state()
        self.circuit.update_quantum_state(state)
        return state.get_vector()

    def set_ref_state(self, vector):
        if self.gpu:
            from qulacs import QuantumStateGpu
            state = QuantumStateGpu(self.num_qubits)
        else:
            state = QuantumState(self.num_qubits)
        state.load(vector)
        self._ref_state = state

    def _get_ref_state(self):
        if self._ref_state is not None:
            return self._ref_state.copy()
        if self.gpu:
            from qulacs import QuantumStateGpu
            state = QuantumStateGpu(self.num_qubits)
        else:
            state = QuantumState(self.num_qubits)
        state.set_zero_state()
        return state

    @classmethod
    def _get_bin(cls, x, n=0):
        """
        Get the binary representation of x.

        Parameters
        ----------
        x : int
        n : int
            Minimum number of digits. If x needs less digits in binary, the rest
            is filled with zeros.

        Returns
        -------
        str
        """
        return format(x, 'b').zfill(n)
