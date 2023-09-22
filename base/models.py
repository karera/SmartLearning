from django.db import models
from datetime import datetime
from custom_accounts.models import  User

class Course(models.Model):
    CATEGORY_CHOICES = (
        ('computer-science', 'Computer Science'),
        ('data-science', 'Data science'),
        ('engineering', 'Engineering'),
        ('web-development', 'Web Development'),
        ('architecture', 'Architecture'),
        # Add more choices as needed
    )
    SUB_CATEGORY_CHOICES = (
        ('ml', 'Machine Learning'),
        ('data_science', 'Data Science'),
        ('python', 'Python'),
        ('javascript', 'JavaScript'),
        ('php', 'PHP'),
        ('django', 'Django'),
        ('html', 'HTML'),
        ('reactjs', 'React JS'),
        ('front-end', 'Front-End'),
        ('back-end', 'Back-End'),

        # Add more choices as needed
    )
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 50 , null = False)
    slug = models.CharField(max_length = 50 , null = False , unique = True)
    description = models.TextField( null = True)
    price = models.IntegerField(null=False,default = 0, blank=True)
    discount = models.IntegerField(null=False ,blank=True, default = 0) 

    active = models.BooleanField(default = False)
    
    category = models.CharField(max_length=255, choices=CATEGORY_CHOICES, default='',  blank=True)
    sub_category = models.CharField(max_length=255, choices=SUB_CATEGORY_CHOICES, default='', null=True, blank=True)
    thumbnail = models.ImageField(upload_to = "files/thumbnail") 
    date = models.DateTimeField(auto_now_add= True) 
    resource = models.FileField(upload_to = "files/resource")
    length = models.IntegerField(null=False)

    instructor_name = models.CharField(max_length=50, null=True)
    enroll_now_status = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class CourseProperty(models.Model):
    description  = models.CharField(max_length = 300 , null = False)
    course = models.ForeignKey(Course , null = False , on_delete=models.CASCADE)

    class Meta : 
        abstract = True


class Tag(CourseProperty):
    pass
    
class Prerequisite(CourseProperty):
    pass

class Learning(CourseProperty):
    pass


class Video(models.Model):
    title  = models.CharField(max_length = 100 , null = False)
    course = models.ForeignKey(Course , null = False , on_delete=models.CASCADE)
    serial_number = models.IntegerField(null=False)
    video_id = models.CharField(max_length = 100 , null = False)
    is_preview = models.BooleanField(default = False)

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # OneToOneField instead of ForeignKey
    course = models.ManyToManyField(Course ,  blank=True)
    date = models.DateTimeField(auto_now_add=True)
    credits = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    free_credits = models.DecimalField(max_digits=8, decimal_places=2, default=18000)  # 5 hours in seconds

    def deduct_credits(self, duration):
        if self.free_credits >= duration:
            self.free_credits -= duration
        else:
            remaining_duration = duration - self.free_credits
            self.free_credits = 0
            self.credits = max(0, self.credits - remaining_duration)

        self.save()

    def start_of_month(self):
        # Reset free_credits to 18000 (5 hours) at the start of the month
        now = datetime.now()
        start_of_month = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        if now == start_of_month:
            self.free_credits = 18000
            self.save()

    def save(self, *args, **kwargs):
        # Call the start_of_month method before saving the object
        self.start_of_month()
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.user)





# #Payment Code
# class EnrollCourse(models.Model):
#     order_id = models.CharField(max_length = 50 , null = False)
#     user_course = models.ForeignKey(UserProfile , null = True , blank = True ,  on_delete=models.CASCADE)

#     user = models.ForeignKey(User ,  on_delete=models.CASCADE)
#     course = models.ForeignKey(Course , on_delete=models.CASCADE)

#     date = models.DateTimeField(auto_now_add=True)
#     status = models.BooleanField(default=False)