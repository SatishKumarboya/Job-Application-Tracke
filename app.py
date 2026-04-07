from flask import Flask, render_template, request, redirect, url_for
from db import get_db_connection, create_table, seed_sample_data

app = Flask(__name__)

# Create table if not exists
with app.app_context():
    create_table()
    seed_sample_data()

@app.route('/')
def index():
    conn = get_db_connection()
    jobs = conn.execute('SELECT * FROM jobs').fetchall()
    conn.close()
    return render_template('index.html', jobs=jobs)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        company = request.form['company']
        role = request.form['role']
        status = request.form['status']
        conn = get_db_connection()
        conn.execute('INSERT INTO jobs (company, role, status) VALUES (?, ?, ?)',
                     (company, role, status))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    conn = get_db_connection()
    job = conn.execute('SELECT * FROM jobs WHERE id = ?', (id,)).fetchone()
    if request.method == 'POST':
        company = request.form['company']
        role = request.form['role']
        status = request.form['status']
        conn.execute('UPDATE jobs SET company = ?, role = ?, status = ? WHERE id = ?',
                     (company, role, status, id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    conn.close()
    return render_template('edit.html', job=job)

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM jobs WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)