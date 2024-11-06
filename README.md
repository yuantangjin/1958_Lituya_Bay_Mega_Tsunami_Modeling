# Mesh-Free Modeling of the 1958 Landslide-Generated Mega-Tsunami in Lituya Bay, Alaska

This repository contains data and code associated with research on mesh-free modeling of the 1958 landslide-generated mega-tsunami in Lituya Bay, Alaska. The data files provide amplitude values of surge waves observed during simulations, while the Python script performs non-linear fitting on the data to extract insights into wave behavior.

## Repository Contents

- **Data Files**:
  - `max_height_wave_885_all_cases.xlsx`: Excel file containing surge wave amplitude data for all cases at the x = 885 m.
  - `max_height_wave_Global_all_cases.xlsx`: Excel file containing global surge wave amplitude data for all cases.

- **Python Script**:
  - `wave_amplitude_fitting.py`: A Python script for non-linear fitting of surge wave amplitude data. The fitting model is designed to capture relationships in the data, achieving a coefficient of determination (R²) of 0.9981, indicating a high degree of fit accuracy. The script uses libraries such as `NumPy`, `SciPy`, and `scikit-learn` to optimize parameters and evaluate the model.

## Usage Instructions

1. **Data Analysis**: Load the Excel files (`max_height_wave_885_all_cases.xlsx` and `max_height_wave_Global_all_cases.xlsx`) for amplitude data in your preferred data analysis software or directly in Python using libraries like `pandas`.

2. **Running the Python Script**:
   - The script performs non-linear curve fitting on the provided data.
   - To execute the script, ensure you have the required dependencies installed:
     ```bash
     pip install numpy scipy scikit-learn matplotlib
     ```
   - Run the script to view the fitting results, including a plot of the original data and the fitted curve, along with key metrics such as R², Mean Squared Error (MSE), and Root Mean Squared Error (RMSE).

## Requirements

- Python 3.6 or higher
- Required packages: `numpy`, `scipy`, `matplotlib`, `scikit-learn`

## Citation

If you use this data or code, please cite the corresponding research paper:

> *Mesh-Free Modeling of the 1958 Landslide-Generated Mega-Tsunami in Lituya Bay, Alaska*

## License

This repository is shared under the MIT License. Please see `LICENSE` for details.
