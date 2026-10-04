"""Standalone example extracted from quantum_tutorial.ipynb."""

from pathlib import Path
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sim = AerSimulator()
OUTPUT = Path(__file__).resolve().parent / "figures"
OUTPUT.mkdir(exist_ok=True)

def save_circuit(circuit, name):
    # Text circuit works even when optional pylatexenc is absent.
    print(circuit.draw("text"))

def plot_probabilities(counts, name):
    total = sum(counts.values())
    outcomes = sorted(counts)
    probabilities = [counts[x] / total for x in outcomes]
    fig, ax = plt.subplots(figsize=(6, 4))
    bars = ax.bar(outcomes, probabilities, color="#2f6690")
    ax.set_ylim(0, 1.05)
    ax.set_xlabel("Measured outcome")
    ax.set_ylabel("Probability")
    ax.set_title(f"Measurement probabilities ({total} shots)")
    ax.bar_label(bars, labels=[f"{p:.1%}" for p in probabilities], padding=3)
    fig.tight_layout()
    path = OUTPUT / f"{name}.png"
    fig.savefig(path)
    plt.close(fig)
    print(f"Figure: {path}")


def main():
    import math
    from fractions import Fraction
    import numpy as np
    from qiskit import transpile
    from qiskit.circuit.library import QFTGate, UnitaryGate

    N = 15
    a = 2
    counting_qubits = 4
    work_qubits = 4


    def modular_multiplication_gate(multiplier, modulus, width):
        dimension = 2**width
        matrix = np.zeros((dimension, dimension), dtype=complex)
        for value in range(dimension):
            target = (multiplier * value) % modulus if value < modulus else value
            matrix[target, value] = 1
        return UnitaryGate(matrix, label=f"x{multiplier} mod {modulus}")


    shor_circuit = QuantumCircuit(counting_qubits + work_qubits, counting_qubits)
    shor_circuit.x(counting_qubits)  # Start the work register in |1>.
    shor_circuit.h(range(counting_qubits))

    for index in range(counting_qubits):
        multiplier = pow(a, 2**index, N)
        controlled_gate = modular_multiplication_gate(
            multiplier, N, work_qubits
        ).control()
        shor_circuit.append(
            controlled_gate,
            [index] + list(range(counting_qubits, counting_qubits + work_qubits)),
        )

    shor_circuit.append(
        QFTGate(counting_qubits).inverse(),
        range(counting_qubits),
    )
    shor_circuit.measure(range(counting_qubits), range(counting_qubits))

    compiled_shor = transpile(shor_circuit, sim)
    shor_counts = sim.run(compiled_shor, shots=1024).result().get_counts()
    print("Order-finding samples:", shor_counts)

    candidate_orders = set()
    for bitstring in shor_counts:
        phase = int(bitstring, 2) / 2**counting_qubits
        denominator = Fraction(phase).limit_denominator(N).denominator
        if denominator % 2 == 0 and pow(a, denominator, N) == 1:
            candidate_orders.add(denominator)

    order = min(candidate_orders) if candidate_orders else None
    if order is not None:
        factors = (
            math.gcd(a ** (order // 2) - 1, N),
            math.gcd(a ** (order // 2) + 1, N),
        )
        print("Candidate period:", order)
        print("Factors of 15:", factors)
    else:
        print("No usable period was recovered; try more shots.")

if __name__ == "__main__":
    main()
