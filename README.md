# TAM
Agile Monkeys Technical test

## Getting started

### Local development
    - Install dependencies: pip install -r requirements.txt
    - Add .env file for environment variables
    - Run migrations to create/update database: python3 manage.py migrate
    - Create an admin user: python3 manage.py createsuperuser
    - Run the server: python3 manage.py runserver
    - Access the API: On your browser visit http://127.0.0.1:8000/api/

### Local development DOCKER
    - Add .env file for environment variables
    - Set USE_DOCKER='True' in .env file
    - Build project: docker compose up --build
    - Access django container and run migrations: python3 manage.py migrate
    - Access the API: On your browser visit http://127.0.0.1:8000/api/

### Run the tests
    - From you local or docker instance run: python3 manage.py test

## Rationale for using Django:

    - Provides basic security measures  out the box: Authentication, Authorisation, SQL injection and XSS prevention ...
    - Is designed to help developers take applications from concept to completion quickly.
    - Is DRY and KISS compliant
    - Is highly scalable and can handle large amounts of traffic and data. Its architecture allows for horizontal scaling, making it suitable for applications with unpredictable traffic patterns
    - Promotes loose coupling between components, making it easier to develop and maintain large applications.
    - Has an extensive and well-maintained documentation, as well as a large collection of third-party libraries and frameworks, making it easier to find help and resources when needed.