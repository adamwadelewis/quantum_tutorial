# Quantum computing tutorial: standalone programs

These 13 scripts follow the order of `quantum_tutorial.ipynb`. Each runs independently and saves charts under `figures/` next to the scripts. Circuit diagrams print in text form. The examples use a local Qiskit Aer simulator; counts for probabilistic measurements vary between runs.

## Set up

```bash
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\Scripts\activate
python -m pip install -r requirements.txt
```

## Run

```bash
python 01_measure_zero.py
python 02_superposition.py
# ... through 13_readout_error.py
```

| Program | Topic |
|---|---|
| 01_measure_zero.py | Measure the initial zero state |
| 02_superposition.py | Hadamard gate and shot counts |
| 03_bell_pair.py | Entanglement and correlated outcomes |
| 04_interference.py | Two Hadamard gates |
| 05_quantum_coin.py | Reusable quantum coin flip |
| 06_bell_challenge.py | Bell pair exercise from notebook |
| 07_deutsch_jozsa.py | Balanced oracle |
| 08_grover.py | Two qubit search |
| 09_shor_order_finding.py | Order finding for factoring 15 |
| 10_qubit_time_evolution.py | Statevector and exact evolution |
| 11_gate_noise.py | Depolarizing gate noise |
| 12_decoherence.py | Thermal relaxation |
| 13_readout_error.py | Measurement error |

The Shor example uses a dense permutation matrix and is intended only for the small teaching example in the notebook.
