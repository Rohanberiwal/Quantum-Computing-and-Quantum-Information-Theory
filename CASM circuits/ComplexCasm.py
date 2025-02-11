import cassm

circuit = cassm.QuantumCircuit(5)

for qubit in range(5):
    circuit.h(qubit)

circuit.cx(0, 1)
circuit.cx(1, 2)
circuit.cx(2, 3)
circuit.cx(3, 4)

circuit.t(0)
circuit.s(1)
circuit.z(2)

circuit.ccx(0, 1, 2)
circuit.ccx(2, 3, 4)

circuit.rx(1.57, 0)
circuit.ry(0.78, 1)
circuit.rz(1.35, 2)

circuit.swap(3, 4)

circuit.measure_all()

backend = cassm.get_backend('simulator')
result = backend.run(circuit, shots=1024)

print(result.get_counts())
