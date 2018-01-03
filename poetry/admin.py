from django.contrib import admin
from . models import Author, Poem, UserProfile, Line
# Register your models here.
admin.site.register(Author)
admin.site.register(Poem)
admin.site.register(UserProfile)
admin.site.register(Line)
