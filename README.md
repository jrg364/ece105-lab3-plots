# Sensor Data Visualization

A small Python script that generates synthetic sensor temperature data and creates publication-quality plots saved as a single PNG file.

## Installation

1. Activate the `ece105` conda environment:

   ```bash
   conda activate ece105
   ```

2. Install the required plotting dependencies using `conda` or `mamba`:

   ```bash
   conda install numpy matplotlib
   ```

   or

   ```bash
   mamba install numpy matplotlib
   ```

## Usage

Run the script from the project root:

```bash
python generate_plots.py
```

## Example output

The script saves a figure called `sensor_analysis.png` containing three subplots:

- A scatter plot of two synthetic temperature sensors over time.
- An overlaid histogram comparing the temperature distributions from both sensors.
- A boxplot showing the summary statistics for each sensor's temperature readings.

## AI tools used and disclosure

This section is left as a placeholder for disclosure details and any AI-assisted development notes.
