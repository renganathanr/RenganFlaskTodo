# RenganTodoWebApp
### Steps to run the todo app on your local machine:
### For windows 10 users:
1. Install python from python.org/downloads
2. Open command prompt and check if pip is installed using the command `pip help` because python 3.4 or above comes with inbuilt pip package.
3. Make sure the recent version of pip is installed using the command `>pip -V` and if not, upgrade the pip using the command `>python -m pip install -U pip`
>For full installation guide for pip installation [click here](https://pip.pypa.io/en/stable/installing/)
4. Install the virtual environment using the command `>python -m pip install virtualenv`
5. Create a local repository named as something related to your Flask app. **i.e. RenganTodoWebApp**
6. Now download this GitHub repository on your machine and extract it to the newly created local repository or navigate to the local repository `cd path\to\RenganTodoWebApp` and clone this GitHub repository using the command `>git clone https://github.com/renganathanr/RenganTodoWebApp`
7. Create a virtual environment (named as your preference **i.e. todolist**) using the command `>python -m venv todolist`
8. Activate the virtual environment using the command `>todolist\Scripts\activate`. Make sure the virtual environment name is visible before the directory address in the command line.
9. Install required packages from requirements.txt file using the command `>pip install -r requirements.txt` and run the todo app using the command `>python app.py`
10. Use any of your browser and go to the url mentioned in the command line after the above command was executed.