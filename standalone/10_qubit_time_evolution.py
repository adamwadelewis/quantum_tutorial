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

import numpy as np
from qiskit.quantum_info import Statevector

def main():
    from qiskit.quantum_info import Statevector

    omega = 1.0
    times = np.linspace(0, 2 * np.pi, 25)
    simulated_probability = []
    exact_probability = []

    for time in times:
        evolution = QuantumCircuit(1)
        evolution.ry(omega * time, 0)
        state = Statevector.from_instruction(evolution)
        simulated_probability.append(abs(state.data[1]) ** 2)
        exact_probability.append(np.sin(omega * time / 2) ** 2)

    figure, axis = plt.subplots(figsize=(7, 4))
    axis.plot(times, simulated_probability, "o", label="Statevector simulation")
    axis.plot(times, exact_probability, label=r"Exact $\sin^2(\omega t / 2)$")
    axis.set_xlabel("Time")
    axis.set_ylabel("Probability of measuring 1")
    axis.set_title("Time evolution under a Y Hamiltonian")
    axis.legend()
    figure.tight_layout()
    print(f"Final simulated probability: {simulated_probability[-1]:.3f}")
    path = OUTPUT / "10_qubit_time_evolution.png"
    figure.savefig(path)
    plt.close(figure)
    print(f"Figure: {path}")

if __name__ == "__main__":
    main()
