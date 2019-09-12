'''
QUANTUM COMPUTING STUDIES
Introduction to Qiskit

@ claudio alves monteiro 2019
clam@cin.ufpe.br
'''

#=======================#
# INITIALIZATION
#======================#

# import package
import qiskit as qk

# define nqubits
nqubits = 3

# creating a quantum register with 3 qubits
q = qk.QuantumRegister(nqubits)

# creating a classical register with  nqubits -1 (for measure)
c = qk.ClassicalRegister(nqubits)

# build quantum circuit with the qubits and classical register
circuit = qk.QuantumCircuit(q, c)

# print circuit
print(circuit)

#===============================#
# Quantum State 1
#==============================#

# Hadamard on all qubits
for i in range(nqubits):
    circuit.h(q[i])

# NOT on all qubits
for i in range(nqubits):
    circuit.x(q[i])

# hadamard on the last
circuit.h(q[2])

# controlled Not toffoli for gates
circuit.ccx(q[0], q[1], q[2])

# hadamard on the last
circuit.h(q[2])

# NOT on all qubits
for i in range(nqubits):
    circuit.x(q[i])

# Hadamard on all qubits
for i in range(nqubits):
    circuit.h(q[i])

#===============================#
# ORACLE
#==============================#

# controlled Z 
circuit.cz(q[1], q[2])


#===============================#
# PHASE
#==============================#


# Hadamard on all qubits
for i in range(nqubits):
    circuit.h(q[i])

# controlled NOT toffoli
circuit.ccx(q[0], q[1], q[2])


print(circuit)

#========================#
# SIMULATE ALGORITHM
#======================#

# measure
circuit.measure(q, c)

# using Aer Qasm Simulator
simulator = qk.BasicAer.get_backend('qasm_simulator')

# simulate the circuit and get result
job = qk.execute(circuit, simulator)
result = job.result()

# get the aggregate binary outputs od the circuit
counts = result.get_counts(circuit)
print(counts)

#https://hiqsimulator.readthedocs.io/en/latest/quantumcomputing.html