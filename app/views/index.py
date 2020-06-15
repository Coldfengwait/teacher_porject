from flask import Blueprint, jsonify
from app.helper import auth_login
from worker import celery_worker
from app.models import User

index = Blueprint('index', __name__, template_folder='templates', static_folder='static')


@index.route('/self', methods=['POST', 'GET'])
# @auth_login()
def self():
    """个人用户信息"""
    user = User.query.filter_by(id=1).first()
    # user = g.user
    data = {
        "id": user.id,
        "nick_name": user.nick_name,
        "avatar_url": user.avatar_url,
        "level": user.level
    }
    my_data = {
        "user_id": user.id,
        "msg": "hello"
    }
    # 5秒后执行任务
    celery_worker.send_msg.apply_async((), my_data, countdown=5)
    return jsonify({'code': 0, "success": True, 'data': data})
