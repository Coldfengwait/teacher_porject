from app import db


class User(db.Model):
    """用户基本信息"""
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    nick_name = db.Column(db.String(64), default='', comment="用户昵称")
    avatar_url = db.Column(db.String(255), default='', comment="用户头像")
    sex = db.Column(db.SmallInteger, default=0, comment="用户性别")
    level = db.Column(db.Integer, default=1, comment="用户等级")
