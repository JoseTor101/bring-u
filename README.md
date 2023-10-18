# Bring-U Project README

## Introduction

This README provides an overview of the Bring-U project, including installation instructions and a project description.

### Installed Apps

Before starting, make sure to install the following packages using `pip`:

- `channels`: Install using `pip install channels`.
- `daphne`: Install using `pip install daphne`.
 - Modify the `channels` installation with: `python -m pip install -U channels["daphne"]`.
- `twisted[http2,tls]`: Install using `pip install twisted[http2,tls]`.
- `whitenoise`: Install for serving static files using `pip install whitenoise`.
- `pytesseract`: Install using `pip install pytesseract`.
- `openai`: Install using  `pip install openai`.
### Starting the ASGI Server

To start the ASGI server, use the following commands:

- `daphne chat.asgi:application`
- `daphne -u /tmp/daphne.sock chat.asgi:application` (Linux only)
- `daphne -u 0.0.0.0:8000 chat.asgi:application`
- `daphne -u 0.0.0.0:8000 chat.asgi:application`

### Deployment

To deploy the project, follow these steps:

1. Collect static files: `python manage.py collectstatic`
2. Run the ASGI server: `daphne -u 0.0.0.0:8000 chat.asgi:application`
3. Access the application at `http://your-server-ip:8000` or the appropriate URL.

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


