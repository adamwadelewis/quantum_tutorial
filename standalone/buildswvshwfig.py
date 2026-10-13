import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def add_box(axis, x, y, width, height, text, color):
    box = FancyBboxPatch(
        (x, y),
        width,
        height,
        boxstyle="round,pad=0.012,rounding_size=0.02",
        linewidth=1.2,
        edgecolor="#263238",
        facecolor=color,
    )
    axis.add_patch(box)
    axis.text(x + width / 2, y + height / 2, text, ha="center", va="center", fontsize=9)


device_figure, axis = plt.subplots(figsize=(14, 5))
axis.set_xlim(0, 1)
axis.set_ylim(0, 1)
axis.axis("off")

hardware_steps = [
    "Qiskit\ncircuit",
    "Compiler /\nnative gates",
    "Control\nelectronics",
    "Physical qubits\n(cryogenic / isolated)",
    "Measurement\nelectronics",
    "Classical\nbit strings",
]
hardware_x = [0.02 + index * 0.163 for index in range(len(hardware_steps))]
box_width = 0.145
box_height = 0.16
hardware_y = 0.62
axis.text(0.5, 0.91, "Real quantum hardware", ha="center", va="center", fontsize=13, weight="bold")
for index, (x, label) in enumerate(zip(hardware_x, hardware_steps)):
    color = "#fcf8e3" if index == len(hardware_steps) - 1 else "#d9edf7"
    add_box(axis, x, hardware_y, box_width, box_height, label, color)
    if index < len(hardware_steps) - 1:
        axis.annotate(
            "",
            xy=(hardware_x[index + 1] - 0.006, hardware_y + box_height / 2),
            xytext=(x + box_width + 0.006, hardware_y + box_height / 2),
            arrowprops={"arrowstyle": "->", "lw": 1.5, "color": "#455a64"},
        )

simulation_steps = [
    "Qiskit circuit",
    "Qiskit Aer\n(ideal or modeled noise)",
    "Classical bit strings",
]
simulation_x = [0.16, 0.42, 0.68]
simulation_y = 0.20
axis.text(0.5, 0.49, "Qiskit Aer simulation", ha="center", va="center", fontsize=13, weight="bold")
for index, (x, label) in enumerate(zip(simulation_x, simulation_steps)):
    color = "#fcf8e3" if index == len(simulation_steps) - 1 else "#dff0d8"
    add_box(axis, x, simulation_y, 0.16, box_height, label, color)
    if index < len(simulation_steps) - 1:
        axis.annotate(
            "",
            xy=(simulation_x[index + 1] - 0.012, simulation_y + box_height / 2),
            xytext=(x + 0.172, simulation_y + box_height / 2),
            arrowprops={"arrowstyle": "->", "lw": 1.5, "color": "#455a64"},
        )

device_figure.tight_layout()
plt.show()
