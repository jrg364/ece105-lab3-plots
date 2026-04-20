"""Generate publication-quality sensor data visualizations.

This script creates synthetic temperature sensor data using NumPy
and produces scatter, histogram, and box plot visualizations saved
as PNG files.

Usage
-----
    python generate_plots.py
"""

import numpy as np
import matplotlib.pyplot as plt


def generate_data(seed):
    """Generate reproducible synthetic sensor temperature data.

    Parameters
    ----------
    seed : int
        Random seed used to initialize the NumPy random number generator.

    Returns
    -------
    sensor_a : numpy.ndarray
        Simulated temperature readings from sensor A.
    sensor_b : numpy.ndarray
        Simulated temperature readings from sensor B.
    timestamps : numpy.ndarray
        Monotonically increasing time points corresponding to each reading.
    """
    rng = np.random.default_rng(seed)
    num_samples = 100
    timestamps = np.arange(num_samples)

    baseline = 20.0 + 0.05 * timestamps
    sensor_a = baseline + rng.normal(scale=0.8, size=num_samples)
    sensor_b = baseline + 0.5 * np.sin(2 * np.pi * timestamps / 24) + rng.normal(scale=0.9, size=num_samples)

    return sensor_a, sensor_b, timestamps


def plot_scatter(sensor_a, sensor_b, timestamps, ax):
    """Draw sensor temperature scatter data on an existing Axes.

    Parameters
    ----------
    sensor_a : numpy.ndarray
        Temperature readings from sensor A.
    sensor_b : numpy.ndarray
        Temperature readings from sensor B.
    timestamps : numpy.ndarray
        Time points corresponding to each sensor reading.
    ax : matplotlib.axes.Axes
        Matplotlib Axes object to modify in place.

    Returns
    -------
    None
        The function updates the provided Axes object and does not return a value.
    """
    ax.scatter(timestamps, sensor_a, label="Sensor A", color="#1f77b4", alpha=0.8, edgecolors="none")
    ax.scatter(timestamps, sensor_b, label="Sensor B", color="#ff7f0e", alpha=0.8, edgecolors="none")
    ax.set_title("Sensor Temperature Scatter Plot")
    ax.set_xlabel("Time")
    ax.set_ylabel("Temperature (°C)")
    ax.legend()
    ax.grid(True, linestyle="--", alpha=0.3)


def plot_histogram(sensor_a, sensor_b, ax):
    """Draw a histogram of both sensor temperature distributions on an Axes.

    Parameters
    ----------
    sensor_a : numpy.ndarray
        Temperature readings from sensor A.
    sensor_b : numpy.ndarray
        Temperature readings from sensor B.
    ax : matplotlib.axes.Axes
        Matplotlib Axes object to modify in place.

    Returns
    -------
    None
        The function updates the provided Axes object and does not return a value.
    """
    bins = 20
    ax.hist(sensor_a, bins=bins, alpha=0.7, label="Sensor A", color="#1f77b4")
    ax.hist(sensor_b, bins=bins, alpha=0.7, label="Sensor B", color="#ff7f0e")
    ax.set_title("Sensor Temperature Distribution")
    ax.set_xlabel("Temperature (°C)")
    ax.set_ylabel("Frequency")
    ax.legend()
    ax.grid(True, linestyle="--", alpha=0.3)


def plot_boxplot(sensor_a, sensor_b, ax):
    """Draw a boxplot comparing two sensor temperature distributions.

    Parameters
    ----------
    sensor_a : numpy.ndarray
        Temperature readings from sensor A.
    sensor_b : numpy.ndarray
        Temperature readings from sensor B.
    ax : matplotlib.axes.Axes
        Matplotlib Axes object to modify in place.

    Returns
    -------
    None
        The function updates the provided Axes object and does not return a value.
    """
    ax.boxplot([sensor_a, sensor_b], labels=["Sensor A", "Sensor B"], patch_artist=True,
               boxprops=dict(facecolor="#ffffff", edgecolor="#333333"),
               medianprops=dict(color="#ff7f0e"),
               flierprops=dict(marker="o", markerfacecolor="#1f77b4", alpha=0.6, markersize=5))
    ax.set_title("Sensor Temperature Boxplot")
    ax.set_ylabel("Temperature (°C)")
    ax.grid(True, linestyle="--", alpha=0.3, axis="y")


def main():
    """Generate sensor data, draw plots, and save the figure.

    This function generates reproducible synthetic sensor readings,
    creates a 2x2 subplot figure, draws the scatter, histogram, and
    boxplot panels on the provided Axes objects, adds a summary statistics
    panel, adjusts the layout, and saves the resulting figure to disk.

    Returns
    -------
    None
        The function saves the figure to 'sensor_analysis.png' and does
        not return a value.
    """
    sensor_a, sensor_b, timestamps = generate_data(seed=42)

    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(14, 10), constrained_layout=False)
    scatter_ax, hist_ax = axes[0]
    box_ax, summary_ax = axes[1]

    plot_scatter(sensor_a, sensor_b, timestamps, scatter_ax)
    plot_histogram(sensor_a, sensor_b, hist_ax)
    plot_boxplot(sensor_a, sensor_b, box_ax)

    summary_text = (
        f"Sensor A mean: {sensor_a.mean():.2f} °C\n"
        f"Sensor A std: {sensor_a.std():.2f} °C\n\n"
        f"Sensor B mean: {sensor_b.mean():.2f} °C\n"
        f"Sensor B std: {sensor_b.std():.2f} °C"
    )
    summary_ax.text(0.5, 0.5, summary_text, ha='center', va='center', fontsize=12)
    summary_ax.set_title('Summary Statistics')
    summary_ax.axis('off')

    fig.tight_layout()
    fig.savefig("sensor_analysis.png", dpi=150, bbox_inches="tight")


if __name__ == '__main__':
    main()
