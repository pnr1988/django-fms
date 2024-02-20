from django import forms
from .models import Address, BankDetails, EducationalDocument, Timesheet, IdentityCard

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['street_address','city','state','postal_code']

class BankDetailsForm(forms.ModelForm):
    class Meta:
        model = BankDetails
        fields = ['account_holder_name','account_number','bank_name','branch_name','ifsc_code']

class EducationalDocumentForm(forms.ModelForm):
    class Meta:
        model = EducationalDocument
        fields = ['ssc','inter','graduation','post_graduation']

class TimesheetForm(forms.ModelForm):
    class Meta:
        model = Timesheet
        fields = ['month', 'timesheet']

class IdentityCardForm(forms.ModelForm):
    class Meta:
        model = IdentityCard
        fields = ['aadhar', 'pan']