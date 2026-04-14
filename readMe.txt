# Tech Store

A simple e-commerce web application built with Django.
The project includes a web interface for browsing products and a REST API for accessing product data.

## Features
* Product listing and filtering by category
* Product detail page
* Shopping cart (session-based)
* Add / remove / update cart items
* Checkout system (reduces stock)
* REST API endpoint for products
* Dark / light theme
* UI using Bootstrap

## Technologies Used

Backend:
* Django 6
* Django REST Framework

Frontend:
* HTML
* CSS
* Bootstrap 5 (via CDN)

Database:
* SQLite (default Django database)

## Installation & Setup
1. Clone the repository:
   - git clone <your-repo-url>
   - cd techStore

2. Create virtual environment:
   - python -m venv venv

3. Activate virtual environment:
   - venv\Scripts\activate

4. Install dependencies:
   - pip install -r requirements.txt

5. Apply migrations:
   - python manage.py migrate

6. Load the predefined products.json
    - cd <Project Folder>\techStore\store\fixtures\
    - python .\script.py loaddata .\products.json

7. Create admin user:
    - python manage.py createsuperuser

8. Run the server:
   - python manage.py runserver

9. Open in browser:
   http://127.0.0.1:8000/

## Notes
* The cart is stored in session (not persistent)
* No authentication system implemented
* Designed for educational purposes

## Author
Peter Bozov (кнз-239)
