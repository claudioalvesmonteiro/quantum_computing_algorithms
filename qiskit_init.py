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

# creating a quantum register with 2 qubits
q = qk.QuantumRegister(2)

# creating a classical register with 2 bits (for measure)
c = qk.ClassicalRegister(2)

# build quantum circuit with the qubits and classical register
circuit = qk.QuantumCircuit(q, c)

# print circuit
print(circuit)

#===============================#
# APPLY QUANTUM GATES ON QUBITS
#==============================#

# Hadamard gate on first qubit
circuit.h(q[0])

# CNOT gate on the first and second qubits
circuit.cx(q[0], q[1])

# measure qubits
circuit.measure(q, c)

# print circuit
print(circuit)

#========================#
# SIMULATE ALGORITHM
#======================#

# using Aer Qasm Simulator
simulator = qk.BasicAer.get_backend('qasm_simulator')

# simulate the circuit and get result
job = qk.execute(circuit, simulator)
result = job.result()

# get the aggregate binary outputs od the circuit
counts = result.get_counts(circuit)
print(counts)