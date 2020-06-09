from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import *
# Register your models here.


User = get_user_model()
class UserAdmin(admin.ModelAdmin):
    list_display = ['cpf', 'nome', 'categoria', 'is_staff', 'vinculo']
    search_fields = ['cpf', 'nome']
admin.site.register(User, UserAdmin)
admin.site.register(CategoriaProfissional)
admin.site.register(Estabelecimento)
