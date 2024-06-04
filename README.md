# Playing Card Classifier 

Convolutional neural network for identifying suit and number from a deck of cards. Integrated into a web application where users can upload photos of a playing card and receive a classification.

## Instructions to launch app

### 1. Set up python environment

If using anaconda, create a new environment and install dependencies from requirements.txt: 

```
conda create --name your_env_name
conda activate your_env_name
pip install -r requirements.txt
```

## Repository Structure

Here's a breakdown of the main directories and files in this repository:

### `/backend`
Contains all the code for the FastCPI backend application, including API endpoints, utility functions, and the server setup.

### `/frontend`
Houses the static HTML and CSS files for the frontend interface of the application, providing the user interface for interactions such as file uploads.

### `/notebooks`
This directory contains Jupyter notebooks used for various stages of the machine learning workflow:
- `model_building.ipynb`: Contains code for building and training the machine learning model.
- `data_exploration.ipynb`: Used for the initial exploration and visualization of the data, helping to understand patterns, distributions, and potential preprocessing steps.
- `model_evaluation.ipynb`: Focused on evaluating the machine learning model, including generating performance metrics and visualizations to assess model efficacy.

### `/data`
Stores data files used by the application, typically not tracked in version control due to size but important for running the application locally.

### `/scripts`
Includes utility scripts like `start_app.py` which can be used to start the FastAPI server and open the frontend in a web browser.

### `/tests`
Contains tests for the backend, ensuring that API endpoints and utility functions behave as expected.

### `README.md`
Provides an overview of the project, setup instructions, and other necessary documentation to get started with using or contributing to the project.

### `requirements.txt`
Lists all necessary Python dependencies for running the project, ensuring that all libraries can be installed using `pip`.


