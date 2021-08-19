from django.contrib import admin

# Register your models here.
from .models import Art
admin.site.register(Art)

from .models import Artist
admin.site.register(Artist)

from .models import User
admin.site.register(User)
