# Playing Card Classifier 

Convolutional neural network for identifying suit and number from a deck of cards. Integrated into a web application where users can upload photos of a playing card and receive a classification.

## Installation

### Set Up Python Environment

If using Anaconda, you can create a new environment and install the required dependencies as follows:

```bash
conda create --name your_env_name python=3.8
conda activate your_env_name
pip install -r requirements.txt
```
Alternatively, if you are not using Anaconda, you can set up a virtual environment using Python's built-in venv module:
```bash
python -m venv your_env_name
source your_env_name/bin/activate  # On Windows use `your_env_name\Scripts\activate`
pip install -r requirements.txt
```

## Launch the Application

Navigate to the project's root directory and run the following command:

```bash
python start.py
```

This script will automatically launch both the FastAPI backend on port 8001 and serve the HTML frontend on port 8000. Your default web browser will open automatically to http://localhost:8000/frontend/, where you can interact with the application.

## Repository Structure

Here's a breakdown of the main directories and files in this repository:

### `/notebooks`
This directory contains Jupyter notebooks used for various stages of the machine learning workflow:
- `data_exploration.ipynb`: Used for the initial exploration and visualization of the data, helping to understand patterns, distributions, and potential preprocessing steps.
- `model_building.ipynb`: Contains code for building and training the machine learning model.
- `model_evaluation.ipynb`: Focused on evaluating the machine learning model, including generating performance metrics and visualizations to assess model efficacy.

### `/backend`
Contains all the code for the FastCPI backend application, including API endpoints, utility functions, and the server setup.

### `/frontend`
Houses the static HTML and CSS files for the frontend interface of the application, providing the user interface for interactions such as file uploads.

### `/data`
Stores data files used by the application, typically not tracked in version control due to size but important for running the application locally.

### `/scripts`
Includes utility scripts like `start_app.py` which can be used to start the FastAPI server and open the frontend in a web browser.

### `/tests`
Contains tests for the backend, ensuring that API endpoints and utility functions behave as expected.
