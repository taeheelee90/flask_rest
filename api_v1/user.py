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