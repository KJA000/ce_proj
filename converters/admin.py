from django.contrib import admin
from .models import Document

class DocumentAdmin(admin.ModelAdmin):
    list_display = [ 'converted_text','converted']
    


admin.site.register(Document, DocumentAdmin)