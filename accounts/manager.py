from django.contrib.auth.base_user import BaseUserManager


class Usermanager(BaseUserManager):
    def create_user(self,phone_num,password = None, **extra_fields):
        if not phone_num:
            raise ValueError("Phone number is required")
        
        extra_fields['email']=self.normalize_email('email')
        user = self.model(phone_num = phone_num,**extra_fields)
        user.set_password(password)
        user.save(using = self.db)

        return user
    
    def create_superuser(self,phone_num,password = None, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

        return self.create_user(phone_num,password,**extra_fields)