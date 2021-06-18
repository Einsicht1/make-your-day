from django.db import models
from django.contrib.auth.models import (AbstractBaseUser,
                                        AbstractUser,
                                        BaseUserManager,
                                        PermissionsMixin)


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Creates a new user"""
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Creates a new super user"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractUser):
# class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username"""
    email = models.EmailField(max_length=255, blank=True)
    username = models.CharField(max_length=255, blank=True)
    social_platform = models.CharField(max_length=255, blank=True)
    social_id = models.CharField(max_length=255, blank=True)
    thumbnail_image = models.URLField(blank=True)
    # is_active = models.BooleanField(default=True)
    # is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'id'
    REQUIRED_FIELDS = []

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'users'
        verbose_name_plural = '회원 관리'



# class UserProfile(models.Model):
#     """User profile model which contains thumbnail_image etc"""
#     thumbnail_image = models.URLField()


def get_posting_image_path(instance, filename):
    """return a posting image path"""
    # return f"{big_category}/{product.product_code}/{filename}"
    pass


class Posting(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, verbose_name="작성자")
    # image = models.ImageField(max_length=1000, upload_to=get_posting_image_path)
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=1000, blank=True)
    category = models.ManyToManyField("Category",
                                  through="core.PostingCategory"
                                  )

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'posting'
        verbose_name_plural = '포스팅'


class Category(models.Model):
    """category of posting model"""
    name = models.CharField(max_length=100, verbose_name="이름")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성일")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="갱신일")

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category'
        verbose_name_plural = '카테고리'


class PostingCategory(models.Model):
    """Middle model between posting and category"""
    posting = models.ForeignKey('Posting', on_delete=models.CASCADE, verbose_name='포스팅')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='카테고리')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성일")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="갱신일")

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category'
        verbose_name_plural = '카테고리'
