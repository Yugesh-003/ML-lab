from qiskit import QuantumCircuit
from qiskit_aer.primitives import Sampler

# Build a simple quantum circuit
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()

# Run using AerSampler
sampler = Sampler()
result = sampler.run(qc).result()

# Display result
print(result.quasi_dists)
