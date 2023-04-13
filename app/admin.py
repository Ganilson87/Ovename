from django.contrib import admin
from .models import *
# Register your models here.

admin.site.site_header = "OVENAME BENFLOR"
admin.site.site_title = "Gerenciador"
admin.site.index_title = "Ovename"


admin.site.register(produto)
admin.site.register(serie)
admin.site.register(categoria)
admin.site.register(acesso)
