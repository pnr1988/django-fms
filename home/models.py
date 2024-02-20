from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

def _upload_path(instance, filename):
    return instance.get_upload_path(filename)

class Address(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.user.username}'s Address"
    
class BankDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_holder_name = models.CharField(max_length=255)
    account_number = models.CharField(max_length=20)
    bank_name = models.CharField(max_length=100)
    branch_name = models.CharField(max_length=100)
    ifsc_code = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.user.username}'s Bank Details"
    
class EducationalDocument(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # title = models.CharField(max_length=255)
    # description = models.TextField(blank=True)
    ssc = models.FileField(null=True, upload_to=_upload_path, validators=[FileExtensionValidator( ['pdf'] ) ])
    inter = models.FileField(null=True, upload_to=_upload_path, validators=[FileExtensionValidator( ['pdf'] ) ])
    graduation = models.FileField(upload_to=_upload_path, validators=[FileExtensionValidator( ['pdf'] ) ])
    post_graduation = models.FileField(blank=True,upload_to=_upload_path, validators=[FileExtensionValidator( ['pdf'] ) ])
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Educational Documents"
    
    def get_upload_path(self, filename):
        return "uploads/"+str(self.user.username)+"/"+filename
    
class Timesheet(models.Model):
    MONTH_CHOICES = [
        ('January', 'January'),
        ('February', 'February'),
        ('March', 'March'),
        ('April', 'April'),
        ('May', 'May'),
        ('June', 'June'),
        ('July', 'July'),
        ('August', 'August'),
        ('September', 'September'),
        ('October', 'October'),
        ('November', 'November'),
        ('December', 'December'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    month = models.CharField(max_length=20, choices=MONTH_CHOICES)
    timesheet = models.FileField(upload_to=_upload_path, validators=[FileExtensionValidator( ['xls','xlsx'] ) ])
    submit_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Timesheets"
    
    def get_upload_path(self, filename):
        return "uploads/"+str(self.user.username)+"/timesheets/"+filename
    
class IdentityCard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    aadhar = models.FileField(upload_to=_upload_path, validators=[FileExtensionValidator( ['pdf'] ) ])
    pan = models.FileField(upload_to=_upload_path, validators=[FileExtensionValidator( ['pdf'] ) ])
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Identity Cards"
    
    def get_upload_path(self, filename):
        return "uploads/"+str(self.user.username)+"/"+filename


