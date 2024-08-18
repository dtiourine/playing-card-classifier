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

### `/scripts`
Includes utility scripts like `start_app.py` which can be used to start the FastAPI server and open the frontend in a web browser.

### `/tests`
Contains tests for the backend, ensuring that API endpoints and utility functions behave as expected.
