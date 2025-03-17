from django.contrib import admin
from .models import Bird

# Register your models here.
class BirdAdmin(admin.ModelAdmin):
    list_display=[
    'bname','bfood','bScientificName','bHabitat','bMigrationPattern','bimg',
    ]


admin.site.register(Bird)

