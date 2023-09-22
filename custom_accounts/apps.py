from django.apps import AppConfig

class Custom_accountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'custom_accounts'
    
    def ready(self):
        import custom_accounts.signals