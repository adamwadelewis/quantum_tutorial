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
    qc = QuantumCircuit(2, 2)

    # Put qubit 0 into superposition.
    qc.h(0)

    # Entangle qubit 0 with qubit 1.
    qc.cx(0, 1)

    # Measure both qubits.
    qc.measure(0, 0)
    qc.measure(1, 1)

    save_circuit(qc, "03_bell_pair")
    result = sim.run(qc, shots=1000).result()
    counts = result.get_counts()

    print("Counts:", counts)

    plot_probabilities(counts, "03_bell_pair")

if __name__ == "__main__":
    main()
