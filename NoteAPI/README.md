Simple Note-Taking API
This project is a RESTful API for a simple note-taking application built using Django. The application allows for creating, fetching, querying, and updating notes without user management. Swagger UI is integrated for API documentation and testing.

Requirements
Python 3.8+
Django==4.2.16
djangorestframework==3.15.2
drf-yasg==1.21.7
PostgreSQL or any other supported database
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/simple-note-api.git
cd simple-note-api
Create a virtual environment:

bash
Copy code
python3 -m venv venv
source venv/bin/activate
Install the dependencies:

bash
Copy code
pip install -r requirements.txt
Set up the database:

Update NoteAPI/settings.py with your database credentials:

python
Copy code
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'your_db_host',
        'PORT': 'your_db_port',
    }
}
Apply the migrations:

bash
Copy code
python manage.py migrate
Run the development server:

bash
Copy code
python manage.py runserver
Access the Swagger documentation: Visit http://127.0.0.1:8000/swagger/ to view and test the API endpoints.

API Endpoints
POST /api/notes/: Create a new note.
GET /api/notes/int:pk/: Fetch a note by its primary key.
GET /api/notes/?title=<substring>: Query notes by a title substring.
PUT /api/notes/int:pk/: Update an existing note.
Testing
Run the integration tests to ensure the API works as expected:

bash
Copy code
python manage.py test