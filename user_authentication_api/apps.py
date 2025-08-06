from django.apps import AppConfig


class UserAuthenticationApiConfig(AppConfig): #change 2
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_authentication_api'
    def ready(self):
        from django.contrib.auth.models import Group
        for group_name in ("administration", "user"):
            Group.objects.get_or_create(name=group_name)