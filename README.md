# Job Application Tracker

A simple Flask web application to track job applications using SQLite database.

## Features

- View all job applications in a responsive table
- Add new job applications with form validation
- Edit existing job applications
- Delete job applications with confirmation
- Status tracking with colored badges: Applied (blue), Interview (yellow), Rejected (red)
- Search jobs by company name
- Filter jobs by status
- Dynamic UI with JavaScript enhancements (confirmations, validation, auto-focus, filtering)
- Modern, responsive design using Bootstrap 5
- Sample data included for demonstration

## Project Structure

```
job-tracker-app/
├── app.py                 # Main Flask application
├── db.py                  # Database connection and utilities
├── templates/             # HTML templates
│   ├── index.html
│   ├── add.html
│   └── edit.html
├── static/                # Static files (CSS, JS, images)
│   ├── style.css
│   └── script.js
├── database.db            # SQLite database file
└── requirements.txt       # Python dependencies
```

## Installation

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run the application:
   ```
   python app.py
   ```

3. Open your browser and go to `http://localhost:5000`

## Deployment

This application is ready for deployment on platforms like Heroku, Railway, Render, or Vercel:

- **Procfile**: Included for Heroku deployment (`web: python app.py`)
- **Requirements**: All dependencies listed in `requirements.txt`
- **Database**: SQLite database (created automatically)
- **Port Configuration**: Configured to run on `0.0.0.0:10000` for containerized deployments

### Local Development
```bash
python app.py
```
*Note: For local development, the app runs on `127.0.0.1:5000` by default. The deployment configuration uses `0.0.0.0:10000`.*

### Deployment Steps
1. **Heroku**: Push to Heroku (Procfile will be used automatically)
2. **Railway/Render**: Deploy from GitHub repository
3. **Docker**: The app is container-ready with the host/port configuration

## Routes

- `/` - Home page showing all jobs
- `/add` - Add a new job
- `/edit/<id>` - Edit a job by ID
- `/delete/<id>` - Delete a job by ID