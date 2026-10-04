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
    from qiskit_aer.noise import NoiseModel, depolarizing_error, ReadoutError

    noisy_gate_circuit = QuantumCircuit(1, 1)
    noisy_gate_circuit.x(0)
    noisy_gate_circuit.measure(0, 0)

    # A depolarizing error models a gate that sometimes disturbs the state.
    gate_noise = NoiseModel()
    gate_noise.add_all_qubit_quantum_error(depolarizing_error(0.10, 1), ["x"])

    ideal_counts = sim.run(noisy_gate_circuit, shots=1000).result().get_counts()
    noisy_counts = sim.run(
        noisy_gate_circuit, shots=1000, noise_model=gate_noise
    ).result().get_counts()

    print("Ideal:", ideal_counts)
    print("With gate noise:", noisy_counts)

    plot_probabilities(ideal_counts, "11_gate_noise_ideal")

    plot_probabilities(noisy_counts, "11_gate_noise_noisy")

if __name__ == "__main__":
    main()
