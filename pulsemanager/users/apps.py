from django.apps import AppConfig
from django.db.models.signals import post_save
import uuid
from django.core.signals import request_finished

#request_finished.connect(my_callback, dispatch_uid="my_unique_identifier")


class UsersConfig(AppConfig):
    name = 'pulsemanager.users'
    verbose_name = "Users"

    def ready(self):
        from .signals                 import post_save_User_receiver
        post_save.connect(post_save_User_receiver, sender='users.User', dispatch_uid=str(uuid.uuid4()))
