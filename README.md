# Hospital-Management-System
A Django-based web application that allows hospital administrators to manage doctors, patients, and appointments.
--
## Screenshots
### Admin login
![Admin Login](screenshots/hms1.png)
### Admin page
![Admin Page](screenshots/hms2.png)
### Doctors list
![View Doctors](screenshots/hms3.png)
### Add apointments
![Add appointments](screenshots/hms5.png)
--
## Features
- Add, view, and delete:
  - Doctors
  - Patients
  - Appointments
- Export records to:
  - PDF
  - CSV
  - Excel
- Clean and responsive Bootstrap UI
---
## Tech Stack
- Django 5.2
- HTML, CSS, Bootstrap
- SQLite
---
## How to Run
Clone the repo and set up the project:

```bash
# Step1: clone the repo
git clone https://github.com/IshitaParira/Hospital-Management-System.git
# Step2: move to project folder
cd Hospital-Management-System
# Step3: Install required python packages
pip install -r requirements.txt

# Step4: Django setup
python manage.py makemigrations
python manage.py migrate

# Step5:Create an admin user
python manage.py createsuperuser

# Step 6:Run the development server
python manage.py runserver
