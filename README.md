# My Portfolio Website

This is a Django-based portfolio website where you can showcase your projects, skills, and experience.

## Getting Started

These instructions will help you set up and run the project on your local machine for development and testing purposes.

### Prerequisites

- Python (version 3.6 or later)
- pip (Python package installer)

### Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Tirumala2824/Dynamic-Portfolio-Website.git
    cd myportfolio
    ```

2. **Create a virtual environment:**
    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment:**
    - On Windows:
      ```bash
      venv\Scripts\activate
      ```
    - On macOS and Linux:
      ```bash
      source venv/bin/activate
      ```

4. **Install the project dependencies:**
    ```bash
    pip install django
    ```

### Running the Project

1. **Apply migrations:**
    ```bash
    python manage.py migrate
    ```

2. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

3. Open your web browser and navigate to `http://127.0.0.1:8000/` to see the website.

### Project Structure

- `myportfolio/`: Main project directory.
  - `settings.py`: Configuration for the Django project.
  - `urls.py`: URL configuration for the project.
  - `wsgi.py`: WSGI configuration for the project.

- `portfolio/`: Application directory.
  - `migrations/`: Database migration files.
  - `templates/portfolio/`: HTML templates for the application.
  - `views.py`: Views for the application.
  - `urls.py`: URL configuration for the application.

### Deployment

To deploy the project to a production environment, you can use platforms like Heroku, AWS, or DigitalOcean. Make sure to update the `settings.py` file with the appropriate settings for production, such as `DEBUG=False` and configuring a production database.

### Built With

- [Django](https://www.djangoproject.com/) - The web framework used

### Contributing

Feel free to fork the repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Acknowledgments

- Django documentation
- Other open-source projects that served as inspiration

