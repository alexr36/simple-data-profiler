# Simple Data Profiler
This is a simple data profiler for CSV files built with the `ydata-profiling` Python library.

## Installation
First, create Python virtual environment and activate it:
```bash
python3 -m venv <venv_name>
source <venv_name>/bin/activate
```

Then, install all the dependencies from `requirements.txt` file:
```bash
pip install -r requirements.txt
```

The tool is now ready to use.

## Usage
To run the script on UNIX-like systems, execute the following command:

```bash
./data_profiler.py -f <path_to_file>
```

If `-f <path_to_file>` is not provided, data profiling will be performed on the default input file `dane.csv`.

Result is saved in `report.html` file in the project's root directory.

## Dependencies
This project uses the `ydata-profiling` library, which is distributed under the MIT License.

## Dataset

This repository includes the `dirty_cafe_sales.csv` dataset (`dane.csv` file), originally published as
**Cafe Sales - Dirty Data for Cleaning Training** on Kaggle.

Source: Kaggle dataset by Ahmed Mohamed  
Dataset page: https://www.kaggle.com/datasets/ahmedmohamed2003/cafe-sales-dirty-data-for-cleaning-training

License for the dataset: **CC BY-SA 4.0**

## License
This project's source code is licensed under the MIT License.