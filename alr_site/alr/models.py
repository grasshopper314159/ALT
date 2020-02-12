from django.db import models
from django.contrib.auth.models import User as user_account

class User(models.Model):
    id = models.OneToOneField(user_account, primary_key=True, on_delete=models.CASCADE)
    #id = models.AudtoField(unique=True, primary_key=True)
    #first_name = models.CharField(default=None, max_length=20)
    #last_name = models.CharField(default=None, max_length=20)
    #email = models.EmailField(default=None)
    #password = models.CharField(default=None, max_length=20)
    type = models.CharField(max_length=15)
    last_login_date = models.DateTimeField(auto_now=True)
    num_audio_files = models.IntegerField(default=None, blank=True, null=True)
    classes = models.ManyToManyField("Class", default=None, blank=True) #User and class 'part of' relationship
    assignments = models.ManyToManyField("Assignment", default=None, blank=True) #User and assignment 'are assigned' relationship
    audio_trims = models.ManyToManyField("AudioTrim", default=None, blank=True) #User and audio trim 'can rate' relationship
    languages = models.ManyToManyField('Language', default=None, blank=True) #User and language 'studies' relationship
    
    def __str__(self):
        return (self.id.first_name + ', ' + self.id.last_name)

class AudioTrim(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    big_audio_id = models.ForeignKey("BigAudio", on_delete=models.CASCADE, default=None)
    original_text = models.TextField()
    english_text = models.TextField()
    phonetic_text = models.TextField(default=None, blank=True, null=True)
    last_listened_date = models.DateTimeField(default=None, blank=True, null=True) 
    score = models.IntegerField(default=None, blank=True, null=True)
    word_count = models.IntegerField(default=None, blank=True, null=True)
    length = models.IntegerField(default=None, blank=True, null=True)
    start_time = models.TimeField()
    
    class Meta:
        unique_together = (("big_audio_id", "start_time")) #AudioTrim has a composite key.

    def __str__(self):
        return (self.english_text + ': ' + str(self.id))


class BigAudio(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    upload_date = models.DateField(auto_now_add=True)
    sound_file = models.FileField(upload_to="")
    length = models.TimeField()
    owner_id = models.ForeignKey("User", on_delete=models.CASCADE, default=None) #Big audio and user 'owns' relationship
    speaker_id = models.ForeignKey("Speaker", on_delete=models.CASCADE, default=None) #Big audio and speaker 'spoken by' relationship
    language_id = models.ForeignKey("Language", on_delete=models.CASCADE, default=None) #Big and language 'spoken in' relationship
    reviews = models.ManyToManyField("User", through="Review", related_name="big_audio_reviews") #User and big audio 'can review' relationship
    comments = models.ManyToManyField("User", through="Comment", related_name="big_audio_comments") # User and big audio 'can comment' relationship
    private = models.BooleanField(default=True)

    def __str__(self):
        return (self.owner.id.first_name + ', ' + self.owner.id.last_name + ': ' + str(self.id))

class Review(models.Model):
    user_id = models.ForeignKey("User", on_delete=models.CASCADE)
    big_audio_id = models.ForeignKey("BigAudio", on_delete=models.CASCADE, default=None)
    review = models.TextField()

    def __str__(self):
        return (self.user.id.first_name + ', ' + self.user.id.last_name + ': ' + str(self.big_audio.id))


class Comment(models.Model):
    user_id = models.ForeignKey("User", on_delete=models.CASCADE)
    big_audio_id = models.ForeignKey("BigAudio", on_delete=models.CASCADE, default=None)
    comment = models.TextField()

    def __str__(self):
        return (self.user.id.first_name + ', ' + self.user.id.last_name + ': ' + str(self.big_audio.id))

#Need input from Miyashita for this one:
class Measurements(models.Model):
    audio_trim_id = models.ForeignKey("AudioTrim", on_delete=models.CASCADE, default=None)
    set_number = models.IntegerField(unique=True)
    wavelength = models.IntegerField(default=None, blank=True, null=True)
    frequency = models.IntegerField(default=None, blank=True, null=True)
    
    class Meta:
        unique_together = (("audio_trim_id", "set_number")) #Measurements has a composite key.

class Speaker(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    user_id = models.OneToOneField("User", on_delete=models.CASCADE, default=None, blank=True, null=True) #User and speaker 'can be' relationship.  This gives speaker a foreign key to user.
    languages = models.ManyToManyField("Language") #Speaker and language 'speaks' relationship

    def __str__(self):
        return (self.first_name + ', ' + self.last_name + ': ' + str(self.id))

class Language(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return (self.name + ': ' + str(self.id))


class Class(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()
    teacher_id = models.ForeignKey("User", on_delete=models.CASCADE, default=None) #Class and user 'teaches' relationship
    language_id = models.ForeignKey("Language", on_delete=models.CASCADE, default=None) #Class and language 'focuses on' relationship
    
    assignments = models.ForeignKey('Assignment', on_delete = models.CASCADE, default=None, blank=True, null=True) #Class and assignment 'assigns' relationship
    

    def __str__(self):
        return (self.teacher.id.first_name + ', ' + self.teacher.id.last_name + ': ' + str(self.id))

class Assignment(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    description = models.TextField()
    due_date = models.DateTimeField()
    comment = models.TextField(default=None, blank=True, null=True)
    grade = models.CharField(max_length=1)
    submission = models.BooleanField(default=False)
    class_id = models.ForeignKey("Class", on_delete=models.CASCADE, default=None)
    big_audio_files = models.ManyToManyField("BigAudio") #Assignment and big audio 'can involve' relationship

    def __str__(self):
        return (str(self.id))
