from django.db import models
import uuid
#rom shortuuid.django_fields import ShortUUIDField
from shortuuid.django_fields import ShortUUIDField 
from userauths.models import User
from django.db.models.signals import post_save


ACCOUNT_STATUS=(
    ("active","Active"),
    ("in_active","In-active"),
    ("pending","Pending")
)

MARTIAL_STATUS=(
    ("married","Married"),
    ("single","Single"),
    ("other","Other")
)
GENDER=(
    ("male","Male"),
    ("female","Female"),
    ("other","Other")
)

IDENTITY_TYPE=(
    ("national_id_card","Natioanal ID Card"),
    ("drivers_license","Drivers License"),
    ("international_passport","International Passport")
)

def user_directory_path(instance,filename):
    ext=filename.split(".")[-1]
    filename="%s_%s" % (instance.id,ext)
    return "user_{0}/{1}".format(instance.user.id,filename)

class Account(models.Model):
    id=models.UUIDField(primary_key=True,unique=True,default=uuid.uuid4,editable=False)
    user=models.OneToOneField(User,on_delete=models.CASCADE)    
    account_balance=models.DecimalField(max_digits=12,decimal_places=2,default=0.00)#123
    account_number=ShortUUIDField(unique=True,length=10,max_length=25,prefix="217",alphabet="1234567890")#2174567181
    account_id=ShortUUIDField(unique=True,length=7,max_length=25,prefix="DEX",alphabet="1234567890")      
    pin_number=ShortUUIDField(unique=True,length=4,max_length=25,alphabet="1234567890")#2727
    ref_code=ShortUUIDField(length=10,max_length=15,alphabet="abcdefg1234567890")
    account_status=models.CharField(max_length=100,choices=ACCOUNT_STATUS,default="in_active")
    date=models.DateTimeField(auto_now_add=True)
    kyc_submitted=models.BooleanField(default=False)
    kyc_confirmed=models.BooleanField(default=False)
    recommended_by=models.ForeignKey(User,on_delete=models.DO_NOTHING,null=True,blank=True,related_name="recommended_by")

    class Meta:
        ordering=['-date']

    def __str__(self):
        return f"{self.user}"
    
class KYC(models.Model):
    id=models.UUIDField(primary_key=True,unique=True,default=uuid.uuid4,editable=False)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    account=models.OneToOneField(Account,on_delete=models.CASCADE,null=True,blank=True)
    full_name=models.CharField(max_length=1000)
    image=models.ImageField(upload_to="kyc",default="default.jpg")
    marrital_status=models.CharField(max_length=100,choices=MARTIAL_STATUS,default="married")
    gender=models.CharField(max_length=100,choices=GENDER,default="male")
    identity_type=models.CharField(max_length=100,choices=IDENTITY_TYPE,default="drivers_license",null=True,blank=True)
    identity_image=models.ImageField(upload_to="kyc",null=True,blank=True)
    date_of_birth=models.DateTimeField(auto_now_add=False)
    #date_of_birth=models.DateTimeField(auto_now_add=False)
    signature=models.ImageField(upload_to="kyc")

    #Address
    country=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    city=models.CharField(max_length=100)


    #contact detail
    mobile=models.CharField(max_length=1000)
    fax=models.CharField(max_length=1000)
    date=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.user}"



         
        
    
def create_account(sender,instance,created,**kwargs):   #heh django signals basically account create kela na aapla tar toh swataun aapla naav,pin number,vagere sagla gheto aaplya la manually create karayla nahi lagat admin madhe heh sagla hota
    if created:
        Account.objects.create(user=instance)

def save_account(sender,instance,**kwargs):
    instance.account.save()

post_save.connect(create_account,sender=User)
post_save.connect(save_account,sender=User)           