import sqlite3

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def create_table():
    conn = get_db_connection()
    conn.execute('''
CREATE TABLE IF NOT EXISTS jobs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company TEXT NOT NULL,
    role TEXT NOT NULL,
    status TEXT NOT NULL
)
''')
    conn.commit()
    conn.close()

def seed_sample_data():
    """Add sample job applications for demonstration"""
    conn = get_db_connection()
    sample_jobs = [
        ('Google', 'Software Engineer', 'Applied'),
        ('Microsoft', 'Product Manager', 'Interview'),
        ('Amazon', 'Data Scientist', 'Rejected'),
        ('Apple', 'UX Designer', 'Applied'),
        ('Meta', 'Frontend Developer', 'Interview'),
        ('Netflix', 'DevOps Engineer', 'Applied'),
        ('Tesla', 'Machine Learning Engineer', 'Rejected'),
        ('Spotify', 'Backend Developer', 'Interview')
    ]

    # Check if data already exists
    existing_count = conn.execute('SELECT COUNT(*) FROM jobs').fetchone()[0]
    if existing_count == 0:
        conn.executemany('INSERT INTO jobs (company, role, status) VALUES (?, ?, ?)', sample_jobs)
        conn.commit()
        print(f"Added {len(sample_jobs)} sample job applications")

    conn.close()