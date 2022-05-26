# A Small poetry.lock visualizer
Reaktor Fall 2022 Software Developer Trainee\
Preliminary Assignment


## Description
A small program for parsing poetry.lock files and visualizing them with a html front\
\
More info for the assignment @ https://www.reaktor.com/assignment-fall-2022-developers/.


### Built with
* [Python](https://www.python.org/)
* [Flask](https://flask.palletsprojects.com/)


## Getting started
To get your local copy up and running follow these steps

### Prerequisites
I suggest running the API in a virtual environment

1. Install the virtual environment
  ```sh
  pip install venv
  ```
 2. Create the virtual environment
  ```sh
   python -m venv /path/to/directory
   ```
 3. Activate the virtual environment
  ```sh
   path\to\venv\Scripts\activate.bat
   ```


### Installation
1. Navigate to the environment folder and unpack the provided zip there
 ```sh
 cd /path/to/venv
 ```
 ```sh
 tar -xf r.trainee-2022.zip
 ```
 2. Install the required depencies
 ```sh
 pip install -r requirements.txt
 ```
 3. Run the tests to check that everything is ok
 ```sh
 cd tests
 Python test_tomlparser.py
 ```
 ```sh
 Python test_package.py
 ```
 4. Go back to main folder and start the program
 ```sh
 cd ..
 py wsgi.py
 ```


## Usage
 When the app is up and running you can test it by going to
 ```sh
 http://localhost:5000/
 ```
 Upload a poetry.lock file from your computer and click send
 
 ![esim1](https://user-images.githubusercontent.com/98524196/170256800-41d8e816-9b81-4044-8ff4-f1514d8dd67a.png)
 
 After that you have your projects depency tree visualized and navigate it by clicking the links!
 
 ![esim2](https://user-images.githubusercontent.com/98524196/170257238-37e50cc3-4268-4680-8c33-f2bdc64aa3b0.png)
 

## Contact
Jukka Pelli - jukka.pelli@tuni.fi
