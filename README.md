# Youtube-Clone

Youtube-Clone is a Django-based web application that aims to replicate the functionality of the popular video-sharing platform, YouTube. It allows users to upload videos, register, log in, watch videos, and search for specific content. This repository contains the source code and necessary files to run the Youtube-Clone application.

# Features
1. User Registration: Users can create an account to access additional features and personalize their experience.
2. User Login: Registered users can log in to their accounts securely.
3. Video Upload: Users can upload their own videos to share with others.
4. Video Search: Users can search for videos based on keywords or specific criteria.

# Installation
To run the Youtube-Clone application locally, follow these steps:

Clone the repository:

```bach
git clone https://github.com/your-username/youtube-clone.git
cd youtube-clone
```

Set up a virtual environment (optional but recommended):
```bach
python3 -m venv env
source env/bin/activate
```
Install the project dependencies:
```bach
pip install -r requirements.txt
```
Set up the database:
```bach
python manage.py migrate
```
Create a superuser (admin account) to manage the application:
```bach
python manage.py createsuperuser
```
Start the development server:
```bach
python manage.py runserver
```
Open your web browser and navigate to http://localhost:8000 to access the Youtube-Clone application.
