# OnlineShop2

OnlineShop2 is a Django-based web application for publishing and browsing private listings.

The project was created as a graduation qualification project in 2025 and represents an early stage of my development experience with Django and web technologies. It was developed as a working proof of concept rather than a production-ready commercial platform.

## About the Project

The goal of the project was to build a simple web platform where users can register, create listings, browse listings published by other users, and contact sellers.

The application was developed in less than two weeks as part of my graduation work. It was also my first practical experience with Django and SMTP-based email delivery.

The repository is preserved as a snapshot of my skills, development process, and project structure at that time.

## Features

### User Management

- User registration
- User authentication
- User logout
- User profiles
- Personal account functionality

### Listings

- Create listings
- Edit listings
- Delete listings
- View listings
- Upload listing images
- Browse listings published by other users

### Contact System

- Contact sellers through a form
- Send messages using SMTP email delivery
- Continue communication outside the platform

### Administration

- Django Admin interface
- User management
- Listing management

## Technologies

### Backend

- Python
- Django 5.2.1

### Frontend

- HTML
- CSS

### Database

- SQLite

### Additional Technologies

- SMTP — email delivery
- Pillow — image processing

The project uses a modular Django architecture consisting of several applications with separate areas of responsibility.

## Project Structure

The repository contains four custom Django applications together with the main Django project configuration:

```text
Diploma/
├── users/
│   └── User registration, authentication and profiles
│
├── listings/
│   └── Listing creation, editing, deletion and display
│
├── contact/
│   └── Contact forms and email communication
│
├── siteinfo/
│   └── Site information and related functionality
│
├── OnlineShop2/
│   └── Global project configuration and URL routing
│
├── templates/
│   └── Shared HTML templates
│
├── media/
│   └── Uploaded media files
│
├── manage.py
├── requirements.txt
└── db.sqlite3
```

### `users`

Handles user registration, authentication, logout, profile management, and personal account functionality.

### `listings`

Handles listing creation, editing, deletion, display, image upload, and browsing.

### `contact`

Handles contact forms and email communication between users.

### `siteinfo`

Contains site information and related supporting functionality.

### `OnlineShop2`

Contains the main Django project configuration, global settings, and URL routing.

## How It Works

```text
Register
   ↓
Log in
   ↓
Browse listings
   ↓
Create a listing
   ↓
Other users view the listing
   ↓
Contact the seller
   ↓
Continue communication outside the platform
```

The project does not include integrated payments, delivery services, or an internal transaction system.

Buying, selling, payment, and delivery arrangements are handled directly between users outside the platform.

## Application Interface & Project Documentation

The application interface is in Russian because the project was originally developed for a Russian-speaking market.

For GitHub, the project documentation is also available in English, while the original Russian documentation is preserved.

| Part of the project | Language |
| --- | --- |
| Application interface | Russian |
| Original graduation documentation | Russian |
| English project documentation | English |
| GitHub README | English |

## Documentation

### Graduation Qualification Work

The repository includes the full graduation qualification work that describes the project in detail.

Both versions are preserved:

- Original Russian documentation
- English translation

The documentation covers topics including:

- Project goals and technical requirements
- Software design and architecture
- Development tools and technologies
- Data model
- Software testing
- System programmer guidance
- Application operation
- Safety requirements
- Project development prospects
- Conclusions and appendices

The English version keeps the same general structure, formatting, and illustrations as the original document.

## Presentation

There is also a project presentation in the repository that was used during my graduation project.

An English translation is provided alongside the original presentation.

## Security

The project uses several security mechanisms provided by Django, including:

- CSRF protection
- Password hashing through Django authentication
- Input validation
- Restricted access to administrative functionality
- Django Admin for controlled user and listing management

Because this repository represents a development-stage project, it should not be treated as a production deployment.

## Testing

The project documentation includes testing of the main application components and typical user scenarios.

Testing covered areas such as:

- User registration
- Authentication
- Listing-related functionality
- Contact form behavior
- General application workflow

The purpose of testing was to verify that the core functionality of the prototype worked as expected.

## Project Status

OnlineShop2 is not a finished commercial product.

It is best described as a proof of concept or minimal working prototype created for a graduation project.

The application was developed in less than two weeks and will never be expanded into a fully finished production system.

This was my first project using Django and SMTP technology, so the repository is intentionally preserved as a snapshot of my progress, practical experience, and development skills at that time.

## Background

OnlineShop2 was created in 2025 as my graduation qualification project.

The project gave me practical experience with the full process of building a small web application, including:

- Planning the application structure
- Working with Django applications and routing
- Creating user authentication functionality
- Working with models and SQLite
- Handling image uploads
- Building listing management functionality
- Implementing email communication using SMTP
- Working with templates and frontend pages
- Testing application functionality
- Preparing technical documentation and a graduation presentation

The project reflects the stage of my development experience at the time it was created and is kept on GitHub as part of my learning and project history.
