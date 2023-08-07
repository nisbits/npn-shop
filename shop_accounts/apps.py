from django.apps import AppConfig


class ShopAccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shop_accounts'

    # def ready(self):
    #   import shop_accounts.signals
