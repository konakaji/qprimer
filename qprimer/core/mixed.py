from abc import ABC, abstractmethod


class MixedState(ABC):
    def __init__(self, num_qubits):
        self.num_qubits = num_qubits

    def cx(self, c_index, t_index):
        return self.cnot(c_index, t_index)

    @abstractmethod
    def copy(self):
        pass

    @abstractmethod
    def h(self, index):
        pass

    @abstractmethod
    def s(self, index):
        pass

    @abstractmethod
    def sdag(self, index):
        pass

    def hsdag(self, index):
        self.sdag(index)
        self.h(index)

    @abstractmethod
    def x(self, index):
        pass

    @abstractmethod
    def y(self, index):
        pass

    @abstractmethod
    def z(self, index):
        pass

    @abstractmethod
    def get_q_register(self):
        pass

    @abstractmethod
    def rx(self, theta, index):
        pass

    @abstractmethod
    def ry(self, theta, index):
        pass

    @abstractmethod
    def rz(self, theta, index):
        pass

    @abstractmethod
    def cnot(self, c_index, t_index):
        pass

    @abstractmethod
    def cy(self, c_index, t_index):
        pass

    @abstractmethod
    def cz(self, c_index, t_index):
        pass

    @abstractmethod
    def measure(self, index):
        pass

    @abstractmethod
    def measure_all(self):
        pass

    @abstractmethod
    def barrier(self):
        pass

    @abstractmethod
    def draw(self, output="mpl"):
        pass

    @abstractmethod
    def draw_and_show(self):
        pass

    @abstractmethod
    def get_samples(self, nshot):
        pass

    @abstractmethod
    def get_counts(self, nshot):
        pass

    @abstractmethod
    def get_state_vector(self):
        pass
