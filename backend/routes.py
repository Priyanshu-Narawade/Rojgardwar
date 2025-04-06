from flask import Blueprint, request, jsonify
from models import connect_db, init_db
from utils import hash_password, check_password

auth_routes = Blueprint('auth', _name_)
job_routes = Blueprint('jobs', _name_)

init_db()

@auth_routes.route('/signup', methods=['POST'])
def signup():
    data = request.json
    try:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute('''
            INSERT INTO users (name, phone, village, education, interests, job_type, password)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            data['name'], data['phone'], data['village'], data['education'],
            ','.join(data['interests']), data['job_type'], hash_password(data['password'])
        ))
        conn.commit()
        return jsonify({"status": "success"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@auth_routes.route('/login', methods=['POST'])
def login():
    data = request.json
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE phone = ?", (data['phone'],))
    user = cur.fetchone()
    if user and check_password(data['password'], user[7]):
        return jsonify({"status": "success", "user": user[1]}), 200
    return jsonify({"error": "Invalid credentials"}), 401

@job_routes.route('/jobs', methods=['GET'])
def get_jobs():
    # You can replace this with actual DB entries later
    jobs = [
        {"title": "Carpenter Assistant", "company": "Sharma Furniture", "location": "Rajpur Village", "salary": 12000, "match": "90%"},
        {"title": "Farm Helper", "company": "Green Fields Farm", "location": "Anandpur", "salary": 10000, "match": "85%"},
        {"title": "Construction Worker", "company": "Patel Builders", "location": "Chandpur", "salary": 15000, "match": "75%"}
    ]
    return jsonify(jobs)

@job_routes.route('/courses', methods=['GET'])
def get_courses():
    courses = ["Basic Carpentry", "Organic Farming", "Digital Marketing", "Poultry Management"]
    return jsonify(courses)
