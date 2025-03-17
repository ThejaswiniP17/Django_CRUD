# Forest Django Project

## Overview
Forest is a Django-based web application that includes multiple apps such as **Animal**, **Bird**, and **HomeApp**. This project implements CRUD (Create, Read, Update, Delete) operations for managing data related to forests, wildlife, and habitats.

## Features
- User-friendly interface for managing forest-related data.
- CRUD operations for animals, birds, and home-related information.
- Django Admin Panel for easy database management.
- SQLite as the default database.
- Bootstrap for styling the frontend.

## Technologies Used
- **Backend:** Django, Python
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** SQLite (default), can be switched to PostgreSQL or MySQL
- **Version Control:** Git, GitHub

## Installation
### Prerequisites
Ensure you have Python and Django installed on your system.
```sh
python --version  # Check Python version
pip install django  # Install Django
```

### Clone the Repository
```sh
git clone https://github.com/ThejaswiniP17/Django_CRUD.git
cd Django_CRUD
```

### Create Virtual Environment (Optional but Recommended)
```sh
python -m venv env
source env/bin/activate  # On Windows, use 'env\Scripts\activate'
```

### Install Dependencies
```sh
pip install -r requirements.txt
```

### Apply Migrations
```sh
python manage.py makemigrations
python manage.py migrate
```

### Create Superuser (For Admin Panel)
```sh
python manage.py createsuperuser
```
Follow the instructions to create a superuser account.

### Run the Server
```sh
python manage.py runserver
```
Visit `http://127.0.0.1:8000/` in your browser to access the application.

## Usage
- Navigate to the **HomeApp** to explore the project.
- Use the **Animal** and **Bird** apps to add, view, update, or delete records.
- Access the Django Admin panel at `http://127.0.0.1:8000/admin/` for backend management.

## Project Structure
```
Django_CRUD/
│── Forest/            # Main Django project
│── Animal/            # Animal app
│── Bird/              # Bird app
│── HomeApp/           # Home application
│── db.sqlite3         # Database (default)
│── manage.py          # Django project manager
│── requirements.txt   # Dependencies
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is open-source and available under the [MIT License](LICENSE).

## Contact
For any queries, reach out via [GitHub Issues](https://github.com/ThejaswiniP17/Django_CRUD/issues).

