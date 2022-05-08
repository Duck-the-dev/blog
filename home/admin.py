from django.contrib import admin
from .models import Post

# Register your models here.


# that adds new entry to the superuser
admin.site.register(Post)
