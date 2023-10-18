# Backend-behave-requests

 Backend test project using [Python](https://www.python.org/), [Behave](https://behave.readthedocs.io/en/latest/) and [Requests](https://pypi.org/project/requests/). 

 
## Table of Contents

- [Pre-requisites](#Pre-requisites)
- [Project Setup](#Project-Setup)
- [Test execution](#tests-execution)


## Pre-requisites
To run this project you need to install `Python3`, `pip` and `venv`. [Google Chrome](https://www.google.com/chrome/) is also needed to be installed.

## Project Setup


**Install Python (Windows)**



If you're using Windows and don't have Python installed, follow these steps to get started:

1. **Download Python:** Visit the official Python website at [python.org](https://www.python.org/) and click on the "Downloads" tab. Choose the latest version of Python for Windows and download the installer executable 

2. **Run the Installer:** Once the installer is downloaded, double-click on it to run. You may see an option to "Add Python X.Y to PATH." Make sure to check this option as it allows you to use Python from the command line.

3. **Customize Installation (Optional):** The installer will guide you through the installation process. You can choose to customize the installation by selecting additional features or modifying the installation directory. For most users, the default settings are sufficient.

4. **Complete Installation:** After customizing (if needed), click the "Install Now" button. The installer will copy the necessary files and set up Python on your system.

5. **Verify Installation:** To verify that Python is installed correctly, open the command prompt and enter the following command:

   ```bash
   python --version
   

### Creating a virtual env with using the Python3 baked module `venv`.
I'd recommend to create a Virtual Env to avoid interfering other Python project on your local , although it is optional due to it does not impact the behavior of this implementation. For more information please visit [this documentation](https://docs.python.org/3/library/venv.html).

0. Clone this repository.
1. Move to the cloned repository's directory.
```
cd <path-to>/demoblaze-frontend
```
2. Create the virtual env.
```
python3 -m venv ./
```
3. Activate the virtual env.
```
source bin/activate
```

### Installing project dependencies.
1. Move to the cloned repository's directory.
```
cd <path-to>/Backend-behave-request
```
2. Use `pip3` to install dependencies.
```
pip3 install -r requirements.txt
```


# Tests execution

Given all the scenarios are tagged the tests execution is pretty flexible by using the `behave` command.

## Test suites

- `@smoke`: contain the tests that ensures the core functionality of the API is healthy.
- `@sanity`: a step forward on validating the main features of the API, ensuring that all the functionalities are working as expected.
- `@regression`: alternative and error validation tests, ensures that the whole API is healthy.

## Execution commands

First of all, execute the steps in the [Setup](#project-setup) section. Once the setup is completed, execute all or specific test cases as follows. 

### All test cases

``` 
behave
```

### Specific suite

``` 
behave --tags=smoke
```

### Specific functionality

``` 
behave --tags=login
```



Follow this Behave [documentation](https://behave.readthedocs.io/en/latest/tag_expressions.html) to know more about using tags.