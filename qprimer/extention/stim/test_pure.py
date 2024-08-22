from unittest import TestCase
from qprimer.extention.stim.pure import StimPureState


class TestStimPureState(TestCase):
    def test_get_samples(self):
        state = StimPureState(2)
        state.h(0)
        print(state.measure(0))
