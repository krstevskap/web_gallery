from django.contrib import admin
from .models import ArtPiece, Category


# Register your models here.

class ArtPieceAdmin(admin.ModelAdmin):
    list_display = ["name", "price"]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]


admin.site.register(Category, CategoryAdmin)
admin.site.register(ArtPiece, ArtPieceAdmin)
