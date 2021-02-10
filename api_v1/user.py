from flask import jsonify
from flask import request
from model import WebUser, db
from . import api

@api.route('/users', methods=['GET','POST'])
def users():
    if request.method == 'POST':
        userid = request.form.get('/api/v1/userid')
        username = request.form.get('username')
        password = request.form.get('password')
        re_password = request.form.get('re-password')       

        if not (userid and username and password and re_password):
            return jsonify({'error': 'No arguments'}), 400

        webuser = WebUser()
        webuser.userid = userid
        webuser.username = username
        webuser.password = password

        db.session.add(webuser)
        db.session.commit()

        return jsonify(), 201

    # GET
    users = WebUser.query.all()
    return jsonify([user.serialize for user in users])

@api.route('/users/<uid>', methods=['GET','PUT','DELETE'])
def user_detail(uid):
    if request.method == 'GET':
        user = WebUser.query.filter(WebUser.id == uid).first()
        return jsonify(user.serialize)

    elif request.method == 'DELETE':        
        user = WebUser.query.filter(WebUser.id == uid).first()
        db.session.delete(user)
        db.session.commit()
        return jsonify(), 204
     
    # method == 'PUT'
    data = request.get_json()    
    WebUser.query.filter(WebUser.id == uid).update(data)
    user = WebUser.query.filter(WebUser.id == uid).first()
    db.session.add(user)
    db.session.commit()
    return jsonify(user.serialize)