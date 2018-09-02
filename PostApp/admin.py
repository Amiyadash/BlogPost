from django.contrib import admin
from .models import *
# Register your models here.
class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title","timestamp","updated"]
    list_display_links = ["updated"]   #Able The Link To The Update Field
    list_editable = ["title"]
    list_filter = ["updated","timestamp"]
    search_fields = ["title"]
    class Meta:

        model = Post
admin.site.register(Post,PostModelAdmin)