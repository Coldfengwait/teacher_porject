import functools
from app import models, app, logger
from flask import request, g, abort
import jwt

def auth_login(*args, **kwargs):
    def decorator(method):
        @functools.wraps(method)
        def wrapper(*func_args, **func_kwargs):
            data = request.headers
            if "token" not in data:
                token = request.args.get('token', '')
            else:
                token = data['token']
            if not token:
                logger.error("没有token")
                abort(401)
            try:
                decode_data = jwt.decode(token, app.config['JWT_SECRET_KEY'], )
                id = decode_data['id']
                user = models.user.User.query.filter_by(id=id).first()
                redis_token = app.cache_redis.get("accsee_token_userid" + str(id))
                if redis_token:
                    redis_token = str(redis_token, encoding="utf-8")
                if not user or token !=redis_token:
                    abort(401)
            except Exception as e:
                logger.error(e)
                abort(401)
            g.user = user
            return method(*func_args, **func_kwargs)
        return wrapper
    return decorator