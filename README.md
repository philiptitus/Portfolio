# Portfolio Project

## Project Overview

This project is a personal portfolio web application built using Django. It serves as an online resume and showcase for professional experience, skills, projects, blog posts, and more. The application is designed to be deployed easily and includes features such as a chatbot, downloadable CV, testimonials, and a blog. The site is styled with custom CSS and JavaScript, and supports media uploads for images, avatars, and other files.

## Features
- Personal profile and resume display
- Blog section for articles and updates
- Portfolio section to showcase projects
- Testimonials and skills sections
- Downloadable CV
- Chatbot integration
- Admin interface for content management
- Media file uploads (images, avatars, APKs, etc.)
- Responsive design with custom CSS and JS

## Technical Details

### Framework & Structure
- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite (default, can be changed)
- **Directory Structure:**
  - `main/`: Main Django app with models, views, forms, and utilities
  - `resume_app/`: Django project settings and configuration
  - `static/` and `mediafiles/`: Static and media file storage
  - `templates/`: HTML templates for rendering views
  - `backups/`: Data backup files
  - `env/`: Python virtual environment

### Key Files
- `manage.py`: Django management script
- `requirements.txt` / `reqs.txt`: Python dependencies
- `main.html`: Main template file
- `vercel.json`: Configuration for Vercel deployment
- `build.sh`: Build script (for deployment)

### Deployment
- The project is ready for deployment on platforms like Vercel or any standard web server supporting Django.
- Static and media files are managed for production use.

### Customization
- Add or update content via the Django admin interface.
- Extend functionality by adding new Django apps or templates.
- Update styles in `static/css/` and scripts in `static/js/`.

### Getting Started
1. **Clone the repository**
2. **Set up a Python virtual environment** (see `env/` or create a new one)
3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
4. **Apply migrations:**
   ```sh
   python manage.py migrate
   ```
5. **Run the development server:**
   ```sh
   python manage.py runserver
   ```
6. **Access the site at** `http://127.0.0.1:8000/`

---

For more details, see the code and comments in each app and module.
