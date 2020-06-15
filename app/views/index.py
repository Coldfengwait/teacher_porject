from flask import Blueprint, jsonify
from app.helper import auth_login


index = Blueprint('index', __name__, template_folder='templates', static_folder='static')

@index.route('/self')
@auth_login()
def self():
    """个人用户信息"""
    user = g.user
    data = {
        "id": user.id,
        "nick_name": user.nick_name,
        "avatar_url": user.avatar_url,
        "level": user.level
    }
    return jsonify({'code': 0, "success": True, 'data': data})
