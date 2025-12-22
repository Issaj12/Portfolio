# Django Portfolio

A modern, feature-rich portfolio website built with Django 6.0. Showcase your skills, work experience, education, services, and manage contact inquiries with an intuitive admin dashboard.

## 🌟 Features

- **Landing Page** - Eye-catching main page to introduce yourself
- **About Section** - Display education history, services offered, testimonials, and CVs
- **Work Experience** - Showcase your professional background with company photos
- **Skills Showcase** - Display and manage your technical skills with images
- **CV Management** - Upload and manage multiple CVs with file downloads
- **Testimonials** - Showcase client testimonials with photos and ratings
- **Contact Form** - Allow visitors to get in touch with you
- **Admin Dashboard** - Comprehensive management system
  - Manage work experience, education, services, and CVs
  - Create, edit, and delete testimonials
  - Download contact submissions as CSV
  - Delete individual or all contact submissions
  - Full CRUD operations for all content types
- **Responsive Design** - Works on desktop and mobile devices
- **SQLite Database** - Lightweight database for data persistence

## 🛠️ Tech Stack

- **Backend**: Django 6.0
- **Database**: SQLite
- **Image Processing**: Pillow 12.0.0
- **Other**: asgiref, sqlparse, tzdata

## 📋 Prerequisites

- Python 3.8+
- pip (Python package manager)
- Virtual environment (recommended)

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd django_portfolio
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv env
   # On Windows:
   env\Scripts\activate
   # On macOS/Linux:
   source env/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r Portfolio/requirements.txt
   ```

4. **Run migrations**
   ```bash
   cd Portfolio
   python manage.py migrate
   ```

5. **Create a superuser (admin account)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Start the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Main page: `http://localhost:8000/`
   - Admin panel: `http://localhost:8000/admin/`
   - Admin Dashboard: `http://localhost:8000/adm/`
   - About page: `http://localhost:8000/about/`
   - Work Experience: `http://localhost:8000/work/`
   - Skills: `http://localhost:8000/skills/`
   - CVs: `http://localhost:8000/cv/`
   - Contact form: `http://localhost:8000/contact/`

## 📁 Project Structure

```
django_portfolio/
├── README.md
├── Portfolio/                    # Django project settings
│   ├── settings.py             # Project configuration
│   ├── urls.py                 # URL routing
│   ├── wsgi.py                 # WSGI configuration
│   ├── asgi.py                 # ASGI configuration
│   ├── requirements.txt         # Python dependencies
│   ├── manage.py               # Django management script
│   ├── db.sqlite3              # SQLite database
│   ├── Mainpage/               # Main app
│   │   ├── models.py
│   │   ├── views.py           # Landing page
│   │   ├── urls.py
│   │   ├── forms.py
│   │   ├── migrations/
│   │   └── templates/Main/
│   ├── about/                  # About app
│   │   ├── models.py          # Education & Service models
│   │   ├── views.py           # About page views
│   │   ├── urls.py
│   │   ├── forms.py
│   │   ├── migrations/
│   │   └── templates/about/
│   ├── work_experience/        # Work experience app
│   │   ├── models.py          # WorkExperience model with company photos
│   │   ├── views.py           # Work experience list & detail views
│   │   ├── urls.py
│   │   ├── forms.py
│   │   ├── migrations/
│   │   └── templates/work/
│   ├── skills/                 # Skills app
│   │   ├── models.py          # Skill model with image field
│   │   ├── views.py           # Skills list & detail views
│   │   ├── urls.py
│   │   ├── forms.py           # SkillForm
│   │   ├── migrations/
│   │   └── templates/skills/
   ├── contact/                # Contact app
│   │   ├── models.py          # Contact form submissions
│   │   ├── views.py           # Contact form handling
│   │   ├── urls.py
│   │   ├── forms.py           # ContactForm
│   │   ├── migrations/
│   │   └── templates/contact/
│   ├── CVs/                    # CVs app
│   │   ├── models.py          # CV model for file uploads
│   │   ├── views.py           # CV views
│   │   ├── urls.py
│   │   ├── forms.py           # CVForm
│   │   ├── migrations/
│   │   └── templates/CV/       # CV templates
│   ├── static/                 # Static files
│   │   ├── css/
│   │   │   ├── style.css
│   │   │   └── styles.css
│   │   └── images/
│   ├── media/                  # User uploads
│   │   ├── company_photos/    # Company photos for work experience
│   │   ├── skills/            # Skill images
│   │   ├── testimonials/       # Testimonial images
│   │   └── cvs/               # CV file uploads
│   └── templates/              # Base templates
│       ├── navbar.html
│       ├── navbar2.html
│       └── start.html
└── env/                        # Virtual environment
```

## 📊 Models

### Education Model
- **institution** (CharField) - School/University name
- **course** (CharField) - Course/degree name
- **start_year** (PositiveIntegerField) - Start year
- **end_year** (PositiveIntegerField, optional) - End year
- **description** (TextField, optional) - Additional details

### Service Model
- **title** (CharField) - Service name
- **description** (TextField) - Detailed description
- **location** (CharField, optional) - Service location
- **is_active** (BooleanField) - Whether service is currently offered

### WorkExperience Model
- **company_name** (CharField) - Name of the company
- **position** (CharField) - Job position/title
- **company_photo** (ImageField, optional) - Company logo or photo
- **start_date** (DateField) - Employment start date
- **end_date** (DateField, optional) - Employment end date
- **description** (TextField) - Job responsibilities and achievements

### Skill Model
- **name** (CharField) - Skill name
- **description** (TextField) - Detailed description
- **picture** (ImageField) - Skill image
- **acquired_from** (CharField) - Source/where learned

### Contact Model
- **name** (CharField) - Visitor's name
- **email** (EmailField) - Contact email
- **phone** (CharField, optional) - Phone number
- **message** (TextField) - Message content
- **submitted_at** (DateTimeField) - Auto timestamp

### CV Model
- **name** (CharField) - CV title/name
- **content** (TextField) - CV description
- **file** (FileField) - PDF or document file
- **created_at** (DateTimeField) - Auto timestamp when created

### Testimonial Model
- **client_name** (CharField) - Name of the client
- **content** (TextField) - Testimonial text
- **client_photo** (ImageField, optional) - Client photo
- **rating** (IntegerField, optional) - Star rating
- **contact_info** (CharField, optional) - Client contact information
- **email** (EmailField, optional) - Client email

## 🎯 Usage

### Adding Work Experience
1. Navigate to `/admin/` and log in
2. Go to Work Experience section
3. Click "Add Work Experience"
4. Fill in company name, position, dates, and description
5. Optionally upload a company photo
6. Work experience appears on `/work/`

### Managing Education & Services
1. Navigate to `/admin/` and log in
2. Go to Education or Services section
3. Add, edit, or delete entries as needed
4. Changes reflect on `/about/` page

### Adding Skills
1. Navigate to `/admin/` and log in
2. Go to Skills section
3. Use the skill creation form
4. Upload an image and fill in details
5. Skills appear on `/skills/`

### Managing CVs
1. Navigate to Admin Dashboard (`/adm/`)
2. Go to CVs section
3. Click "Add New" to upload a new CV
4. Fill in CV name, description, and upload file
5. CVs appear on `/cv/` and in about section
6. Edit or delete CVs as needed

### Managing Testimonials
1. Navigate to Admin Dashboard (`/adm/`)
2. Go to Testimonials section
3. Click "Add New" to create a testimonial
4. Add client name, photo, content, and rating
5. Testimonials display on `/about/testimonials/`

### Viewing Contact Submissions
1. Go to `/admin/` and log in
2. Navigate to Contact section
3. View all submitted contact forms
4. Download as CSV for records
5. Delete individual or all submissions

### Contact Form
Visitors can submit contact forms at `/contact/` which are saved to the database and accessible in the admin panel.

## 🔧 Configuration

Key settings in `Portfolio/settings.py`:
- `DEBUG = True` (change to `False` for production)
- `ALLOWED_HOSTS = []` (add your domain for production)
- Media files configured for skill image uploads
- Static files configuration included

## 📦 Dependencies

```
asgiref==3.11.0
Django==6.0
pillow==12.0.0
sqlparse==0.5.5
tzdata==2025.3
```

## 🆕 Recent Updates (December 22, 2025)

### New Features Added:
- **CV Management Module** - New `CVs` app for managing multiple CVs
  - Upload CV files (PDF, documents)
  - Create, read, update, delete CV entries
  - Download CVs from detail page
  - CV management in admin dashboard

- **Enhanced About Section**
  - Added CV tab to about page navigation
  - Integrated CV display with testimonials and services
  - Better organization with tabbed interface

- **Improved Admin Dashboard**
  - CV management section added
  - Quick stats for all content types
  - Dedicated CV upload and management interface
  - File download functionality

### New Routes:
- `/cv/` - View all CVs
- `/cv/<id>/` - View individual CV
- `/adm/add/` - Add new CV (admin)
- `/adm/<id>/edit/` - Edit CV (admin)
- `/adm/<id>/delete/` - Delete CV (admin)

## 🚨 Production Deployment Checklist

Before deploying to production:
- [ ] Set `DEBUG = False` in settings.py
- [ ] Update `SECRET_KEY` to a secure random value
- [ ] Add your domain to `ALLOWED_HOSTS`
- [ ] Configure proper database (PostgreSQL recommended)
- [ ] Set up static/media file serving (AWS S3, etc.)
- [ ] Use environment variables for sensitive settings
- [ ] Enable HTTPS/SSL
- [ ] Set up proper logging

## 🤝 Contributing

Contributions are welcome! Feel free to:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

Josiah Mwangi - Portfolio Website

---

**Last Updated**: December 22, 2025

### Latest Changes:
- ✅ Added CV Management app (CVs)
- ✅ Enhanced admin dashboard with CV section
- ✅ Integrated CVs into about page
- ✅ Added file upload and download functionality
- ✅ Updated URL routing for CV module
# Portfolio
# Portfolio
# Portfolio
