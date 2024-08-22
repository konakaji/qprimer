from qprimer.core.pure import PureState

try:
    from stim import Circuit, TableauSimulator
except ImportError as e:
    print(e, "To use StimPureState, you need to install stim")


class StimPureState(PureState):
    def __init__(self, num_qubits):
        super().__init__(num_qubits)
        self.circuit = TableauSimulator()

    def copy(self):
        pass

    def h(self, index):
        self.circuit.h(index)

    def s(self, index):
        self.circuit.s(index)

    def sdag(self, index):
        self.circuit.s_dag(index)

    def x(self, index):
        self.circuit.x(index)

    def y(self, index):
        self.circuit.y(index)

    def z(self, index):
        self.circuit.z(index)

    def rx(self, theta, index):
        raise NotImplementedError("Stim does not support non Clifford gate")

    def ry(self, theta, index):
        raise NotImplementedError("Stim does not support non Clifford gate")

    def rz(self, theta, index):
        raise NotImplementedError("Stim does not support non Clifford gate")

    def cnot(self, c_index, t_index):
        self.circuit.cnot(c_index, t_index)

    def cy(self, c_index, t_index):
        self.circuit.cy(c_index, t_index)

    def cz(self, c_index, t_index):
        self.circuit.cz(c_index, t_index)

    def t(self, index):
        raise NotImplementedError("Stim does not support non Clifford gate")

    def measure(self, index):
        return int(self.circuit.measure(index))

    def barrier(self):
        pass

    def draw(self, output=None):
        pass

    def draw_and_show(self):
        pass
