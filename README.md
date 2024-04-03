# eScriptorium Live Segmonto Checker

This application is a simple app that allows for checking your document against the Segmonto guidelines, without downloading the XML from eScriptorium.

## Getting Started

These instructions will help you set up the project on your local machine using Conda or Miniconda for managing the environment and dependencies.

### Prerequisites

- Conda or Miniconda or Python 3
- Git 

### Cloning the Repository

First, clone the repository to your local machine using the following command:

```bash
git clone https://github.com/username/repository.git
```

### Using Virtual Environment


#### Setting up

Navigate to the project directory and create a virtual environment. You can do this using the following commands:

```bash
cd repository
python -m venv venv
```

then activate the virtual environment

- On Windows, `venv\Scripts\activate`
- On macOS/Linux, `source venv/bin/activate`

then install dependencies:

```bash
pip install -r requirements.txt
```

#### Running

After installing the dependencies, navigate to the project directory, activate your environment:

- On Windows, `venv\Scripts\activate`
- On macOS/Linux, `source venv/bin/activate`

then you can launch the Flask app using the flask run command:

```bash
flask run
```
This command will start the development server, and you can access the app in your web browser at http://localhost:5000.

### Using Anaconda or Miniconda

#### Setting Up

Navigate to the project directory and create a new Conda environment using the environment.yml file provided in the repository:

```bash
cd repository
conda env create -f environment.yml
```

#### Running the application

Activate the Conda environment with the following command (make sure you are in the correct directory)

```bash
conda activate segmontoEnv
flask run
```

This command will start the development server, and you can access the app in your web browser at http://localhost:5000.