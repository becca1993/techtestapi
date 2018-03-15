from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions
from app import *
from models import Person



@app.route('app/people', methods = ['GET'])
def get_all_people():
    """This function will return the total number of people records"""
    all_people = Person.query.all()
    return jsonify(all_people)

@app.route('app/people', methods = ['GET'])
def sort_by_name(name):
    """function will return person by particular name"""
    return jsonify(Person.query.get(name))


"""function will return person by particualr email"""
@app.route('/app/people', method = ['GET'])
def sort_by_mail(email):
   return jsonify(Person.query.get(email))


@app.route('app/people', method = ['POST'])
def create_new_person():
    """function will create new person with parameters name, age, balance, email, and adress and add to the db"""
    name = request.json['name']
    age = request.json['age']
    balance = request.json['balance']
    email = request.json['email']
    address = request.json['address']

    new_person = Person(name, age, balance, email, address)

    db.session.add(new_person)
    db.session.commit()

    return jsonify(new_person)


@app.route('app/people', method = ['PUT'])
def edit_person(person_id):
    """this function will edit user"""
    edit = Person.query.get(person_id)

    name = request.json['name']
    age = request.json['age']
    balance = request.json['balance']
    email = request.json['email']
    address = request.json['address']

    edit.name = name
    edit.age = age
    edit.balance = balance
    edit.email = email
    edit.address = address

    db.session.commit()
    return jsonify(edit)

@app.route('app/people', method = ['DELETE'])
def delete_person(person_id):
    """this function will delete users"""
    delete = Person.query.get(person_id)
    db.session.delete(delete)
    db.session.commit

    return jsonify(delete)







