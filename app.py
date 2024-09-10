from flask import Flask, render_template, request, redirect, url_for
from models import db, Incident
from notifications import send_notification

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///incidents.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def index():
    incidents = Incident.query.all()
    return render_template('dashboard.html', incidents=incidents)

@app.route('/report', methods=['POST'])
def report_incident():
    title = request.form['title']
    description = request.form['description']
    location = request.form['location']
    severity = request.form['severity']
    
    new_incident = Incident(title=title, description=description, location=location, severity=severity)
    db.session.add(new_incident)
    db.session.commit()
    
    # Notify administrators
    send_notification('admin@example.com', 'New Incident Reported', f'Incident {title} reported.')
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
