# HW4 Starter Code and Instructions

Please consult the [homework assignment](https://cmu-313.github.io//assignments/hw4) for additional context and instructions for this code.

## pipenv

[pipenv](https://pipenv.pypa.io/en/latest) is a packaging tool for Python that solves some common problems associated with the typical workflow using pip, virtualenv, and the good old requirements.txt.

### Installation

#### Prereqs

- The version of Python you and your team will be using (version greater than 3.8)
- pip package manager is updated to latest version
- For additional resources, check out [this link](https://pipenv-fork.readthedocs.io/en/latest/install.html#installing-pipenv)

#### Mac OS

To install pipenv from the command line, execute the following:

```terminal
sudo -H pip install -U pipenv
```

#### Windows OS

The same instructions for Mac OS **should** work for windows, but if it doesn't, follow the instructions [here](https://www.pythontutorial.net/python-basics/install-pipenv-windows).

### Usage

#### Downloading Packages

The repository contains `Pipfile` that declares which packages are necessary to run the `model_build.ipnyb`.
To install packages declared by the Pipfile, run `pipenv install` in the command line from the root directory.

You might want to use additional packages throughout the assignment.
To do so, run `pipenv install [PACKAGE_NAME]`, as you would install python packages using pip.
This should also update `Pipfile` and add the downloaded package under `[packages]`.
Note that `Pipfile.lock` will also be updated with the specific versions of the dependencies that were installed.
Any changes to `Pipfile.lock` should also be committed to your Git repository to ensure that all of your team is using the same dependency versions.

#### Virtual Environment

Working in teams can be a hassle since different team members might be using different versions of Python.
To avoid this issue, you can create a python virtual environment, so you and your team will be working with the same version of Python and PyPi packages.
Run `pipenv shell` in your command line to activate this project's virtual environment.
If you have more than one version of Python installed on your machine, you can use pipenv's `--python` option to specify which version of Python should be used to create the virtual environment.
If you want to learn more about virtual environments, read [this article](https://docs.python-guide.org/dev/virtualenvs/#using-installed-packages).
You can also specify which version of python you and your team should use under the `[requires]` section in `Pipfile`.

## Jupyter Notebook

You should run your notebook in the virtual environment from pipenv.
To do, you should run the following command from the root of your repository:

```terminal
pipenv run jupyter notebook
```

## API Endpoints

You should also use pipenv to run your Flask API server.
To do so, execute the following commands from the `app` directory in the pip venv shell.


Set an environment variable for FLASK_APP.
For Mac and Linux:
```terminal
export FLASK_APP=app.py
```

For Windows:
```terminal
set FLASK_APP=app
```

To run:
```terminal
pipenv run flask run
```

Or if you're in the pipenv shell, run:
```terminal
flask run
```

You can alter the port number that is used by the Flask server by changing the following line in `app/app.py`:

```python
app.run(host="0.0.0.0", debug=True, port=80)
```

## Testing

To run tests, execute the following command from the `app` directory:

```terminal
pytest
```

If you're not in the Pipenv shell, then execute the following command from the `app` directory:

```terminal
pipenv run pytest
```

## Documentation

The old model used three variables: age, health, and number of absences.

For our new model, we used the six variables: the first period grade (G1), 
                                              the second period grade (G2), 
                                              the number of school absences (absences), 
                                              the categorical weekly studytime (studytime), 
                                              the categorical amount of freetime after school (freetime), 
                                              and the number of past class failures up to four (failures).

Our model returns a json with a variable 'prediction' that is either a 0 or 1 for whether or not the student is a good student.
A student is a good student if the predicted grade of period 3 is greater than equal to 15.

Our retrained model does better than the original model. We decided to use the same seed to split the data into the same test and train datasets. We trained our models on the train dataset and tested on the test dataset. Our new model has a 100% accuracy on the train dataset and a 97.48% on the test dataset. Our old model has a 88.77% accuracy on the train dataset and a 73.11% on the test dataset. Thus, our new model has better accuracy than the old model.