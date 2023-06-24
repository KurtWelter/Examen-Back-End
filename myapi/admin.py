from django.contrib import admin
from .models import Usuario
from .models import Sesion
from .models import AlimentoMascota
from .models import AlimentoPerro
from .models import AlimentoGato

admin.site.register(Usuario)
admin.site.register(Sesion)
admin.site.register(AlimentoMascota)
admin.site.register(AlimentoPerro)
admin.site.register(AlimentoGato)
