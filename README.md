# Linear Regression Deployment with Python

This project demonstrates how to build and deploy a simple linear regression model using **Streamlit** (for rapid interactive deployment).

Users can specify parameters such as the slope (`a`), intercept (`b`), number of data points, and noise level to generate synthetic data, train the model, and evaluate its performance.

## My GPT prompts:
- [hw1-1](https://chatgpt.com/share/6718a127-08b0-8008-902a-f6d8136f44c3)
- [hw1-2](https://chatgpt.com/share/6718a108-5d54-8009-9438-a6ae405004da)

## Table of Contents
- [Project Structure](#project-structure)
- [Setup](#setup)
- [Running the Project](#running-the-project)
  - [Streamlit Deployment](#streamlit-deployment)

## Project Structure
```plaintext
├── dataset/
│   └── mydata.csv             # HW1-1 dataset
│   └── S&P500_stock_5y.csv    # HW1-2 dataset
├── hw1-1/
│   └── app.py                 # HW1-1:  simple linear regression
├── hw1-2/
│   └── stock.ipynb            # HW1-2: auto regression , multiple linear regression 
├── README.md                  # Project README
└── requirements.txt           # List of dependencies
```
## Setup

### 1. Clone the repository:
```bash
git clone https://github.com/IdONTKnowCHEK/HW1-Linear-regression.git
cd HW1-Linear-regression
```

### 2. Create and activate a virtual environment using `venv`:
To avoid installing dependencies globally, it's recommended to use a Python virtual environment.

#### On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

#### On Mac/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies:
```bash
pip install -r requirements.txt
```

This will install all required Python libraries, including:
- `streamlit`
- `Flask`
- `scikit-learn`
- `matplotlib`
- `pandas`

## Running the Project

### Streamlit Deployment

To run the **Streamlit** application:

1. Ensure that you are in your virtual environment (check if it's active using `which python` or `python --version`).
2. Run the following command:
   ```bash
   streamlit run hw1-1/app.py
   ```

3. Open your browser and go to `http://localhost:8501/`. You can now interact with the app by adjusting the slope (`a`), intercept (`b`), number of data points, and noise level, and see the results in real time.


### Explanation of Sections:
- **Project Structure**: Describes the structure of your project, highlighting key files.
- **Setup**: Explains how to create a virtual environment, activate it, and install dependencies.
- **Running the Project**: Provides instructions for running the Streamlit and Flask applications.
- **License**: Placeholder for the license under which the project is distributed.
