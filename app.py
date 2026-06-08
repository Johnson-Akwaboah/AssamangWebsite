from flask import Flask, render_template
import os
import sys
# import webbrowser
# from threading import Timer

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

app = Flask(
    __name__,
    template_folder=resource_path('templates'),
    static_folder=resource_path('static')
)

# ==========================================
# HOME PAGE
# ==========================================
@app.route('/')
def home():

    latest_events = [
        (
            1,
            "Community Clean-Up Exercise",
            "Residents joined together to clean the community and improve sanitation.",
            "2026-06-01",
            "08:00 AM",
            "Domi Assamang",
            "cleanup.jpg",
            None
        )
    ]

    gallery = [
        (1, "Community Meeting", "gallery1.jpg"),
        (2, "School Support Program", "gallery2.jpg"),
        (3, "Health Outreach", "gallery3.jpg"),
        (4, "Youth Development Workshop", "gallery4.jpg")
    ]

    projects = [
        (
            1,
            "School Renovation",
            "Renovation of classroom blocks to improve education.",
            "project1.jpg"
        ),
        (
            2,
            "Community Health Program",
            "Free health screening and awareness campaign.",
            "project2.jpg"
        )
    ]

    return render_template(
        'index.html',
        latest_events=latest_events,
        gallery=gallery,
        projects=projects
    )
    
# ==========================================
# DASHBOARD
# ==========================================
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/events')
def events():
    return render_template('events.html')


@app.route('/projects')
def projects():
    return render_template('projects.html')


@app.route('/gallery')
def gallery():
    return render_template('gallery.html')


@app.route('/announcements')
def announcements():
    return render_template('announcement.html')


@app.route('/leadership')
def leadership():
    return render_template('leadership.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')

# ==========================================
# RUN APP
# ==========================================
if __name__ == '__main__':

    app.run(debug=True)