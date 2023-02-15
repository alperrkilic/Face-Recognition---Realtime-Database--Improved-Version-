import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://face-attendance-project-b984e-default-rtdb.firebaseio.com/"
})

print("Adding data to database...")

ref = db.reference('Students')

data = {
    "321654":
        {
            "name": "Murtaza Hassan",
            "major": "Robotics",
            "starting_year": 2017,
            "total_attendance": 6,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
        "852741":
        {
            "name": "Emily Blunt",
            "major": "Economics",
            "starting_year": 2018,
            "total_attendance": 12,
            "standing": "B",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
        "963852":
        {
            "name": "Elon Musk",
            "major": "Physics",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
        "786453":
        {
            "name": "Bayram Alper KILIC",
            "major": "AI",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
        "123456":
        {
            "name": "Ahmet Erturkmen",
            "major": "Medicine",
            "starting_year": 2020,
            "total_attendance": 12,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
        "198346":
        {
            "name": "Abdulkadir Sazli",
            "major": "Prep School",
            "starting_year": 2020,
            "total_attendance": 12,
            "standing": "G",
            "year": 1,
            "last_attendance_time": "2022-12-11 00:54:34"
        }
}


for key, value in data.items():
    ref.child(key).set(value)

print("Data added to database")
