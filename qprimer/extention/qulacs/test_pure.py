from unittest import TestCase
from qprimer.extention.qulacs.pure import QulacsPureState


class TestQulacsPureState(TestCase):
    def test_measure(self):
        state = QulacsPureState(2)
        state.h(0)
        state.cnot(0, 1)
        result = state.measure(0)
        self.assertEquals(result, state.measure(0))

    def test_sample(self):
        state = QulacsPureState(2)
        state.h(0)
        for s in state.get_samples(10):
            self.assertEqual(s[1], 0)
