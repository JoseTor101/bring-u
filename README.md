# Bring-U Project README

## Introduction

This README provides an overview of the Bring-U project, including installation instructions and a project description.

### Installed Apps

Before starting,  make sure you have installed `python`, `pip`, `django`and `git`:

In linux follow this steps:
1. `sudo apt install -y git`
2. `sudo apt install -y python3-pip`
3. `sudo su pip3 install django`
4. `python3 -m pip install --upgrade pip`
5. Install requirements: `pip install -r requirements.txt`

For other OS look for custom tutorials

### Set project

1. Make sure to clone the repository using: `git clone https://github.com/JoseTor101/bring-u`
2. Move to root folder: `cd BRING_U_PROJECT`
3. Run migrations: `python3 manage.py makemigrations`
4. `python3 manage.py migrate`

### Deployment

To deploy the project, follow these steps:

1. Collect static files: `python manage.py collectstatic`
2. Run the ASGI server: `daphne -b 0.0.0.0 -p 8000 config.asgi:application`
3. Access the application at `GCP - custom URL` or the appropriate URL.

If not pretending to use realtime communication(Chat system), just use:
1. Execute in root folder: `python manage.py runserver`

## Project Description

### Overview

Bring-U is an independent web-based project aimed at enhancing the student experience on campus. It provides a platform for food deliveries from local restaurants and carpooling services. The goal is to optimize mobility, reduce waiting times for orders, and allow students to generate additional income. With Bring-U, we envision a university environment where students can meet their on-campus needs more efficiently.

### Features

- **User Access**: Any user within the campus can create an account on this platform.
- **Local Business Interaction**: Users can view local businesses and their products, place orders, and establish contact with service providers.
- **Delivery Services**: Users can take delivery requests and complete deliveries, which is a unique feature aimed at reducing wait times.
- **Additional Income**: The platform not only streamlines university life but also provides students with an opportunity to earn extra income while pursuing their academic activities.

### Integration and Compatibility

Bring-U is a standalone project and is not intended to be part of a larger system. All integrations are locally implemented. The web application is designed to run on popular web browsers such as Chrome and Brave. Additionally, it will be deployed on a chosen cloud server. If the carpooling system is included, we plan to integrate the Google Maps API for location-based features.

### User Base

There is no specific distinction among users of our app. However, we anticipate that the primary user group will be college students, typically aged between seventeen and forty. This age group is more familiar with such platforms and uses them frequently.


