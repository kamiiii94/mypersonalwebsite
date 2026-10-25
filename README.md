# Personal Portfolio Website

A personal portfolio website built with Django to showcase my CV, technical skills, projects, and learning experience.

## Features

- Personal CV and profile presentation
- Project portfolio
- Technology and skill sections
- Project image galleries
- Dynamic content managed through Django Admin
- Responsive web interface
- Media and static file management

## Technologies

- Python
- Django
- HTML
- CSS
- SQLite
- Pillow

## Project Structure

- `config/` — Django project configuration
- `portfolio/` — Main portfolio application
- `manage.py` — Django management command entry point
- `requirements.txt` — Python dependencies

## Installation

Clone the repository and install the dependencies:

```bash
pip install -r requirements.txt
```

Run database migrations:

```bash
python manage.py migrate
```

Start the development server:

```bash
python manage.py runserver
```

Then open:

```text
http://127.0.0.1:8000/
```

## Security

Sensitive configuration, local databases, environment files, uploaded media, and local data exports are excluded from the repository through `.gitignore`.

## Purpose

This project was created as my personal portfolio website to present my software development experience, technical skills, and selected projects.

## Future Improvements

- Improved deployment configuration
- PostgreSQL support
- Environment-based production settings
- Better responsive design
- Automated tests
- CI/CD integration
