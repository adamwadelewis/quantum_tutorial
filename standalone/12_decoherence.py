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

from qiskit_aer.noise import NoiseModel

def main():
    from qiskit_aer.noise import thermal_relaxation_error

    waiting_circuit = QuantumCircuit(1, 1)
    waiting_circuit.x(0)
    waiting_circuit.id(0)
    waiting_circuit.measure(0, 0)

    # T1 and T2 are simplified relaxation and dephasing time scales.
    relaxation_noise = NoiseModel()
    relaxation_noise.add_all_qubit_quantum_error(
        thermal_relaxation_error(t1=30, t2=20, time=15), ["id"]
    )

    relaxed_counts = sim.run(
        waiting_circuit, shots=1000, noise_model=relaxation_noise
    ).result().get_counts()

    print("After modeled waiting:", relaxed_counts)

    plot_probabilities(relaxed_counts, "12_decoherence")

if __name__ == "__main__":
    main()
