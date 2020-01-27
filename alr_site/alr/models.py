from django.db import models

class User(models.Model):
    num_audio_files = models.IntegerField()
    last_login_date = models.DateTimeField()
    user_type = models.CharField(max_length = 15)
    password = models.CharField(max_length = 20)
    firstname = models.CharField(max_length = 20)
    lastname = models.CharField(max_length = 20)
    email = models.EmailField()
    id = models.IntegerField(primary_key = True)
    
class AudioTrim(models.Model): #Weak Entity
    original_text = models.TextField()
    english_text = models.TextField()
    phonetic_text = models.TextField()
    last_listened_date = models.DateTimeField()
    measurements = models.IntegerField() #Not sure what the data type for this should be
    score = models.IntegerField()
    word_count = models.IntegerField()
    length = models.IntegerField()
    start_time = models.TimeField() #Dashed underline
    
#Comment and Review are attributes to the relationship between BigAudio and User
class BigAudio(models.Model):
    id = models.IntegerField(primary_key = True)
    upload_date = models.DateField()
    length = models.TimeField()
    
class Class(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    id = models.IntegerField(primary_key = True)
    
class Speaker(models.Model):
    id = models.IntegerField(primary_key = True)
    firstname = models.CharField(max_length = 20)
    lastname = models.CharField(max_length = 20)

class Language(models.Model):
    id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 50)