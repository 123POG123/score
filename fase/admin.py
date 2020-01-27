from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Brand
from .models import Mixer
from .models import Ty_pe

# Register your models here.
admin.site.register(Mixer)
admin.site.register(Brand)
admin.site.register(Ty_pe)


