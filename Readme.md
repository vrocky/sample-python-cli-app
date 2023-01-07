# Sample Python CLI App

A simple command-line application for demonstrating how to parse arguments and validate input in Python.

## Installation

To install the application, clone the repository and run the following command:

```bash
pip install .
```

## Usage

To use the application, run the following command:


```bash
cli input_dir -f input.txt
```
This will parse the `input_dir` and `input.txt` arguments and validate that they are valid inputs. The input validation is handled by the `validate_args()` function in the `validation.py` module.

## Testing

Unit tests for the application are located in the `tests` directory. To run the tests, navigate to the `tests` directory and run the following command:

```bash
pytest .
```
The unit tests cover the input validation functionality as well as the main functionality of the application.

## License
```
This project is licensed under the Apache License 2.0.

```
