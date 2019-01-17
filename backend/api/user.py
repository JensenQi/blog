# -*- coding: utf-8 -*-
from flask import Blueprint
from flask import jsonify, request, g
from flask.ext.login import login_required, login_user, logout_user
from models import User

user = Blueprint('user', __name__)


@user.route('/login', methods=['POST'])
def login():
    u = g.session.query(User).filter_by(user_name=request.form.get('user_name')).first()
    if u is not None and u.verify_password(request.form.get('passwd')):
        login_user(u)
        return jsonify({'status': 'success', 'data': {}})
    return jsonify({'status': 'failed', 'data': {}, 'error': '账号密码有误'})


@user.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({'status': 'success', 'data': []})
