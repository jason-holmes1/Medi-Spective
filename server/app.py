from flask import request, session
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
# Local imports
from config import app, db, api
from models import  JournalEntry, User

from flask_cors import CORS
from flask import request, jsonify



@app.before_request
def check_if_logged_in():
    open_access_list = [
        'signup',
        'login',
        'check_session'
    ]

    if (request.endpoint) not in open_access_list and (not session.get('user_id')):
        return {'error': '401 Unauthorized'}, 401


class Signup(Resource):
    
    def post(self):

        request_json = request.get_json()

        username = request_json.get('username')
        password = request_json.get('password')
        image_url = request_json.get('image_url')
        bio = request_json.get('bio')

        user = User(
            username=username,
            image_url=image_url,
            bio=bio
        ) 
        user.password_hash = password
        try:
            db.session.add(user)
            db.session.commit()

            session['user_id'] = user.id

            return user.to_dict(), 201

        except IntegrityError:

            return {'error': '422 Unprocessable Entity'}, 422

class CheckSession(Resource):

    def get(self):
        
        user_id = session['user_id']
        if user_id:
            user = User.query.filter(User.id == user_id).first()
            return user.to_dict(), 200
        
        return {}, 401


class Login(Resource):
    
    def post(self):

        request_json = request.get_json()

        username = request_json.get('username')
        password = request_json.get('password')

        user = User.query.filter(User.username == username).first()

        if user:
            if user.authenticate(password):

                session['user_id'] = user.id
                return user.to_dict(), 200

        return {'error': '401 Unauthorized'}, 401

class Logout(Resource):

    def delete(self):

        session['user_id'] = None
        
        return {}, 204
        

@app.route('/')
def index():
    return '<h1>Medi-Spective</h1>'

@app.route('/journal-entries', methods=['GET'])
def get_journal_entries():
    journal_entries = JournalEntry.query.all()
    journal_entry_list = [journal_entry.to_dict() for journal_entry in journal_entries]
    return jsonify(journal_entry_list),200

@app.route('/journal-entries', methods=['POST'])
def create_journal_entry():
    data = request.get_json()
    if not data:
        return jsonify({'error': '422 Unprocessable Entity'}), 400
    new_journal_entry = JournalEntry(
        title=data.get('title'),
        content=data.get('content'),
        date=data.get('date'),
        user_id=data.get('user_id')
    )
    try:
        db.session.add(new_journal_entry)
        db.session.commit()
        return jsonify(new_journal_entry.to_dict()),201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
    

@app.route('/journal-entries/<int:id>', methods=['GET'])
def get_journal_entry(id):
    journal_entry = JournalEntry.query.filter(JournalEntry.id==id).first()
    return journal_entry.to_dict()

@app.route('/journal-entries/<int:id>', methods=['PUT'])
def update_journal_entry(id):
    journal_entry = JournalEntry.query.get(id)
    journal_entry.title = request.form['title']
    journal_entry.content = request.form['content']
    journal_entry.date = request.form['date']
    journal_entry.user_id = request.form['user_id']
    db.session.commit()
    return journal_entry

@app.route('/journal-entries/<int:id>', methods=['DELETE'])
def delete_journal_entry(id):
    journal_entry = JournalEntry.query.get(id)
    db.session.delete(journal_entry)
    db.session.commit()
    return journal_entry


if __name__ == '__main__':
    app.run(port=5555, debug=True)
