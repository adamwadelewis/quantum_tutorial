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
    grover_circuit = QuantumCircuit(2, 2)
    grover_circuit.h([0, 1])

    # Oracle: mark |11> by changing its phase.
    grover_circuit.cz(0, 1)

    # Diffuser: reflect amplitudes about their average.
    grover_circuit.h([0, 1])
    grover_circuit.x([0, 1])
    grover_circuit.cz(0, 1)
    grover_circuit.x([0, 1])
    grover_circuit.h([0, 1])

    grover_circuit.measure([0, 1], [0, 1])

    save_circuit(grover_circuit, "08_grover")
    grover_counts = sim.run(grover_circuit, shots=512).result().get_counts()
    print("Grover counts:", grover_counts)

    plot_probabilities(grover_counts, "08_grover")

if __name__ == "__main__":
    main()
