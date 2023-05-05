# My Awesome Cart

## Project Description

This project is a simple blog app built with Django, a high-level Python web framework. The blog allows users to create an account, write and publish posts, and comment on posts written by others. It also features an admin dashboard where administrators can manage posts, comments, and user accounts.

## Features

- User authentication and authorization
- Create, edit, and delete posts
- Comment on posts
- Admin dashboard for managing posts, comments, and users
- Responsive design

## Technologies Used

- Django 3.2.3
- Python 3.9.5
- SQLite3
- HTML5
- CSS3
- Bootstrap 5.0.0

## Installation

To run this project on your local machine, follow these steps:

1. Clone the repository to your local machine.
2. Install Python 3.9.5 or higher on your system.
3. Install the required Python packages using pip:

   ```
   pip install -r requirements.txt
   ```

4. Run the following command to create the SQLite3 database:

   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Start the development server using the following command:

   ```
   python manage.py runserver
   ```

6. Open your web browser and go to http://127.0.0.1:8000/.

## Usage

To use the blog app, follow these steps:

1. Create a new account by clicking the "Register" link in the top navigation menu.
2. Log in to your account by clicking the "Log in" link in the top navigation menu.
3. Create a new post by clicking the "New post" button on the home page.
4. View all posts by clicking the "All posts" link in the top navigation menu.
5. Comment on a post by clicking the "Comment" button below the post.
6. Log out of your account by clicking the "Log out" link in the top navigation menu.

## Credits

This project was developed by me and inspired by CodeWithHarry.com
