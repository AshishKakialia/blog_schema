# blog_schema

# Django Blog Application

A simple Django blog application with user authentication, blog creation, listing, and comments system.

## Features

- User Authentication: Users can sign up and log in.
- Create and Manage Blogs: Authenticated users can write and manage their blogs.
- Blog Listing: Blogs are listed with pagination, displaying 5 blogs per page.
- Comment System: Users can comment on blogs, and comments can be liked.
- Share via Email: Share blogs with friends via email.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/AshishKakialia/blog_schema.git

## Create a virtual environment and install dependencies:

python -m venv venv
source venv/bin/activate  # On Windows, use "venv\Scripts\activate"
pip install -r requirements.txt

## Set up the database and apply migrations:

python manage.py migrate

## Create a superuser for admin access:

python manage.py createsuperuser

## Start the development server:

python manage.py runserver

## Access the application at http://localhost:8000/

Visit the admin panel at http://localhost:8000/admin/ and log in with the superuser account to manage blogs and comments.
Users can sign up, log in, create blogs, comment on blogs, and like comments.
Configuration
### Configure email settings in settings.py for sharing blogs via email.

Create .env file and create 'DJANGO_SECRET_KEY', 'EMAIL_HOST_USER' and 'EMAIL_HOST_PASSWORD' variables where 'EMAIL_HOST_USER' set your email id  and 'EMAIL_HOST_PASSWORD' enter your app password, needs to be defined.

