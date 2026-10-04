# Quantum Tutorial: Introduction to QC for Those Somewhat Computing Aware
---

Quantum computing is one of "hype" topics in computing at the moment and
this set of tutorials are an attempt to smooth out the hype and explain
the concepts.

We assume the reader has at least an undergraduate-level understanding
of computer science for all of the tutorials and a similar understanding
of the concepts of calculus and linear algebra for the later tutorials.

## Format

Tutorial documentation is provided in Juypter Notebooks to include a mix
of discussion and executable code.   Standalone versions of the code in
the Juypter Notebooks are available for some, but not all of the
notebooks.

## Setup 

There is a bit of setup required for this tutorial.

It is rather strongly suggested that you use your favorite tool (`pip/venv` or `conda`) to create a virutal envioronment for this tutorial.   We will be using `conda` in today's tutorial.

For example, using `conda`:

```bash
conda create --name quantum
conda activate quantum
# Add should you wish to use this environment with tools like VSCode or 
# other IDEs that support the Jupyter Notebook format
conda install ipykernel
python -m ipykernel install --user --name=quantum --user-name="Python (quantum)"
```

If you are running this locally, install the required packages with either:

```bash
pip install qiskit qiskit-aer matplotlib pylatexenc
```
or

```bash
conda install -c conda-forge qiskit qiskit-aer matplotlib pylatexenc
```

## License

This material is dedicated to the public domain by waiving all copyright
and related rights worldwide under the Creative Commons CC0 1.0
Universal Public Domain Dedication. You are free to copy, modify,
distribute, and perform the work, even for commercial purposes, all
without asking permission. The content is provided as-is without any
warranties of any kind, and the author disclaims all liability for any
use of the material.


