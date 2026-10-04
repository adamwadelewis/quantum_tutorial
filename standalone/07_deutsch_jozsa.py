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

    deutsch_jozsa = QuantumCircuit(2, 1)

    # Prepare the input in |+> and the helper qubit in |->.
    deutsch_jozsa.h(0)
    deutsch_jozsa.x(1)
    deutsch_jozsa.h(1)

    # Balanced oracle for f(x) = x: flip the helper when input qubit 0 is 1.
    deutsch_jozsa.cx(0, 1)

    # Interference reveals whether the function is constant or balanced.
    deutsch_jozsa.h(0)
    deutsch_jozsa.measure(0, 0)

    save_circuit(deutsch_jozsa, "07_deutsch_jozsa")

    dj_result = sim.run(deutsch_jozsa, shots=1000).result()
    dj_counts = dj_result.get_counts()

    print("Counts:", dj_counts)

    plot_probabilities(dj_counts, "07_deutsch_jozsa")

if __name__ == "__main__":
    main()
