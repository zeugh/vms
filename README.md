Running the Web App on a Linux Server
First make sure your system is up to date by running:

$ sudo apt update
$ sudo apt-get -y upgrade
Make sure that you have installed the latest version of Python first. To see which version of Python you have installed, open a terminal and run:

$ python --version
If you don't have Python installed on your device, then you can easily install with the following commands:

$ sudo apt-get install python python3-pip python3-venv
Also check if you have the latest version of pip.

$ python3 -m pip install --user --upgrade pip
$ python3 -m pip --version
You can install python virtual environment via:

$ python3 -m pip install --user virtualenv
Create a new working directory and cd into it. Then create a virtual environemnt inside by running:

$ python3 -m venv env
The above command uses venv to create a virtual Python installation in the env folder.

Once the virtual environment is created you can activate it by running:

$ source env/bin/activate
or
$. /env/bin/activate
Clone the repository into your working directory and install the required dependencies.

$ pip install -r requirements.txt
Now you are ready to run the django server. You can manage.py within the vms directory. To run the server"

$ python3 manage.py runserver
or
$ python3 manage.py runserver 0.0.0.0:8000
Open your browser to access the web app:

http://localhost:8000/
