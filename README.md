# Project Setup Guide

## Overview
This guide provides instructions on how to set up and manage a Python virtual environment for this project.

## Setting Up the Virtual Environment
A virtual environment helps manage dependencies and avoid conflicts with system-wide Python packages.

### Create venv
```sh
python -m venv .venv
```

### Activating the Virtual Environment
To activate the virtual environment, use the following command:
```sh
.venv\Scripts\activate
```
This will switch your terminal to use the isolated Python environment within the `.venv` directory.

### Deactivating the Virtual Environment
To deactivate the virtual environment, simply run:
```sh
.venv\Scripts\deactivate
```
This will return your terminal to the system's default Python environment.

## Installing and Managing Dependencies

### Upgrading `pip`
To ensure you have the latest version of `pip`, run:
```sh
pip install --upgrade pip
```
This will upgrade the package manager to the latest version, ensuring smooth installation of dependencies.

### Installing Required Packages
To install all necessary dependencies from the `requirements.txt` file, use:
```sh
pip install -r requirements.txt
```
This will install all libraries and dependencies listed in the `requirements.txt` file.

### Running the project
To running the project, use:
```sh
fastapi dev main.py
```

## Additional Notes
- Ensure that you are inside the project directory before executing these commands.
- If the virtual environment is not created, you may need to set it up first using:
  ```sh
  python -m venv .venv
  ```
- Use `pip freeze > requirements.txt` to update `requirements.txt` with the latest installed dependencies.

For any issues, refer to the official Python [venv documentation](https://docs.python.org/3/library/venv.html).