from app import celery
from app import models


@celery.task(bind=True)
def send_msg(self, *args, **kwargs):
    msg = kwargs['msg']
    user_id = kwargs['user_id']
    user = models.user.BaseUser.query.filter_by(id=user_id).first()
    print("向%s发送%s" % (user.nick_name, msg))
