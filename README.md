## Coralcity Real-Estate Django Website 
 This website is build for Coralcity Real-Estate business, You will get an admin page where you can manage your users, listings, realtors and queries from other users about listings. You will get search page where users can find listings from your database which suits their needs. You will get a listing page where users can see listings and when they click on those listings they will get a detailed page of that listing with photos of the property. You can manage users. All the passwords of the users are stored in hash value to protect users privacy. Link to your all Social Media pages. About page, Apartments, Dashbord, Agents, Contact us, Log out, Become an agent.

### Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites
Install pip if it is not installed yet in your system

### To install virtual environment, run in your terminal:

* pip install virtualenv

### To create a virtual environment, in the root folder of the cloned app, run:
* virtualenv -p python3 venv

### To activate the virtualenv:
* source venv/bin/activate

### Run the command below to install all the project dependencies:
* pip install -r requirements.txt

### To deactivate the virtualenv:
* deactivate
* Installing
* Clone this repository
* https://github.com/GR8T/coralcity
* Cd into the cloned app, create a virtualenv and activate(see instruction above for steps to create a virtualenv)
* Create a .env file, copy the variables in the .env_sample in the root directory of the project and set up the configurations according to your system.

### Ensure to makemigrations then migrate by running the following commands sequencially:
* - python manage.py makemigrations
* - python manage.py migrate

### To start the application, in the root directory of the project, run:
* python manage.py runserver

## Features of the Project:
* Become an agent
* Login
* Logout
* Upload Passport Photo
* Admin Create listings and Realtors
* Make inquires
* Dashboard monitoring
* Receive notification as Email
* Check Inquire Status
* Built With
* Python 3
* sqlite3
* License
This project is licensed under the MIT License - see the LICENCE file for details
