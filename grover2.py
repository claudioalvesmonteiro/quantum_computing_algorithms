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

# creating a classical register with  nqubits(for measure)
c = qk.ClassicalRegister(nqubits)

# build quantum circuit with the qubits and classical register
circuit = qk.QuantumCircuit(q, c)

# print circuit
print(circuit)

#===============================#
# Quantum State 1
#==============================#

# not on last qubit
circuit.x(q[2])

# Hadamard on all qubits
for i in range(nqubits):
    circuit.h(q[i])


#===============================#
# ORACLE
#==============================#

# multi controlled not 
circuit.ccx(q[0], q[1], q[2])

#===============================#
# CONDITIONAL PHASE SHIFT
#==============================#

# Hadamard on all but last
for i in range(nqubits-1):
    circuit.h(q[i])

# not in all but last
for i in range(nqubits-1):
    circuit.x(q[i])

# hadamrd before last
circuit.h(q[1])

# cnot
circuit.cx(q[0], q[1])

# hadamrd before last
circuit.h(q[1])

# not in all but last
for i in range(nqubits-1):
    circuit.x(q[i])

# Hadamard on all but last
for i in range(nqubits-1):
    circuit.h(q[i])

#========================#
# SIMULATE ALGORITHM
#======================#

# measure
circuit.measure(q[0:2], c[0:2])

print(circuit)

# using Aer Qasm Simulator
simulator = qk.BasicAer.get_backend('qasm_simulator')

# simulate the circuit and get result
job = qk.execute(circuit, simulator)
result = job.result()

# get the aggregate binary outputs od the circuit
counts = result.get_counts(circuit)
print(counts)

#https://hiqsimulator.readthedocs.io/en/latest/quantumcomputing.html