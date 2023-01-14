from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from .models import User
from .forms import UserCreationForm, UserChangeForm
# Register your models here.

@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    Form = UserChangeForm
    add_Form = UserCreationForm
    model = User
    fieldsets = auth_admin.UserAdmin.fieldsets + (
        ("Campos Personalizados", {"fields":("Pacote","legal")}),
    )
    