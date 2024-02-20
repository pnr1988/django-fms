from django.contrib import admin
from .models import Address, BankDetails, EducationalDocument

admin.site.register(Address)
admin.site.register(BankDetails)
admin.site.register(EducationalDocument)
