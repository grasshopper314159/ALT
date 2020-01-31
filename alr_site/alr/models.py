from django.db import models

class User(models.Model):
    num_audio_files = models.IntegerField(default=None, null=True)
    last_login_date = models.DateTimeField(auto_now=True)
    user_type = models.CharField(max_length = 15)
    password = models.CharField(max_length = 20)
    firstname = models.CharField(max_length = 20)
    lastname = models.CharField(max_length = 20)
    email = models.EmailField()
    id = models.AutoField(unique=True, primary_key = True)
    classes = models.ManyToManyField('Class', default=None, blank=True, null=True) #User and class 'part of' relationship
    audio_trims = models.ManyToManyField('AudioTrim', default=None, blank=True, null=True) #User and audio trim 'can rate' relationship
    assignments = models.ManyToManyField('Assignment', default=None, blank=True, null=True) #User and assignment 'are assigned' relationship
    languages = models.ManyToManyField('Language', default=None, blank=True, null=True) #User and language 'studies' relationship
    reviews = models.ManyToManyField('BigAudio', through = 'Review', related_name = 'big_audio_reviews') #User and big audio 'can review' relationship
    comments = models.ManyToManyField('BigAudio', through = 'Comment', related_name = 'big_audio_comments') # User and big audio 'can comment' relationship

class Review(models.Model): #Sub-class
    user = models.ForeignKey('User', on_delete = models.CASCADE)
    big_audio = models.ForeignKey('BigAudio', on_delete = models.CASCADE, default = None)
    review = models.TextField() #Not sure what the data type for this should be

class Comment(models.Model): #Sub-class
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    big_audio = models.ForeignKey('BigAudio', on_delete = models.CASCADE, default = None)
    comment = models.TextField()

class AudioTrim(models.Model): #Weak entity (No primary key), BigAudio is the owner entity
    original_text = models.TextField()
    english_text = models.TextField()
    phonetic_text = models.TextField(default=None, blank=True, null=True)
    last_listened_date = models.DateTimeField(default=None, null=True)
    measurements = models.IntegerField(default=None, blank=True, null=True) #Not sure what the data type for this should be (might need to convert this into an entity)
    score = models.IntegerField(default=None, blank=True, null=True)
    word_count = models.IntegerField(default=None, blank=True, null=True)
    length = models.IntegerField(default=None, blank=True, null=True)
    start_time = models.TimeField() #Partial key

class BigAudio(models.Model):
    id = models.AutoField(unique=True, primary_key = True)
    upload_date = models.DateField(auto_now_add=True)
    length = models.TimeField()
    owner = models.ForeignKey('User', on_delete = models.CASCADE, default = None) #Big audio and user 'owns' relationship
    audio_trims = models.ForeignKey('AudioTrim', on_delete = models.CASCADE, default=None, blank=True, null=True) #Big audio and audio trim 'section of' relationship, this is an indetifying relationship
    speaker = models.ForeignKey('Speaker', on_delete = models.CASCADE, default = None) #Big audio and speaker 'spoken by' relationship
    language = models.ForeignKey('Language', on_delete = models.CASCADE, default = None) #Big and language 'spoken in' relationship
    private = models.BooleanField(default=True)

class Speaker(models.Model):
    id = models.AutoField(unique=True, primary_key = True)
    firstname = models.CharField(max_length = 20)
    lastname = models.CharField(max_length = 20)
    languages = models.ManyToManyField('Language') #Speaker and language 'speaks' relationship
    user = models.OneToOneField('User', on_delete = models.CASCADE, default=None, blank=True, null=True) #User and speaker 'can be' relationship

class Language(models.Model):
    id = models.AutoField(unique=True, primary_key = True)
    name = models.CharField(max_length = 50)

class Class(models.Model):
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()
    id = models.AutoField(unique=True, primary_key=True)
    teacher = models.ForeignKey('User', on_delete = models.CASCADE, default = None) #Class and user 'teaches' relationship
    assignments = models.ForeignKey('Assignment', on_delete = models.CASCADE, default=None, blank=True, null=True) #Class and assignment 'assigns' relationship
    language = models.ForeignKey('Language', on_delete = models.CASCADE, default = None) #Class and language 'focuses on' relationship

class Assignment(models.Model):
    id = models.AutoField(unique=True, primary_key = True)
    description = models.TextField()
    due_date = models.DateTimeField()
    comments = models.TextField(default=None, blank=True, null=True)
    grade = models.CharField(max_length = 1)
    submission = models.BooleanField(default=False) #Not sure what the data type for this should be
    big_audio_files = models.ManyToManyField('BigAudio') #Assignment and big audio 'can involve' relationship
