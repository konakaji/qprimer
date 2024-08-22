def initialize(num_qubits, tool="qulacs"):
    if tool == "qulacs":
        from extention.qulacs.pure import QulacsPureState
        return QulacsPureState(num_qubits)
    elif tool == "stim":
        from extention.stim.pure import StimPureState
        return StimPureState(num_qubits)
    raise AttributeError("Tool must be either qulacs or stim")
