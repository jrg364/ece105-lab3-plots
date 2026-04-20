"""Generate publication-quality sensor data visualizations.

This script creates synthetic temperature sensor data using NumPy
and produces scatter, histogram, and box plot visualizations saved
as PNG files.

Usage
-----
    python generate_plots.py
"""

import numpy as np


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
