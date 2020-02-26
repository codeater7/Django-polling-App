from django.db import models
# import the base model class





# Question Table and Choice Table
# class will inherit the models.Model // will inherit all the methdos from it
class Question(models.Model):
    # Models will allow to create an id automatically
    # models field had tons of fields 
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    # we want to display the question text and choice text so,  here and below

    def __str__(self):
        return self.question_text

# Relationship between choices and Questions?????????How how how??

    


class Choice(models.Model):
    
     # Relationship
    # we want to link this Foreign key to the primary key of Question,
    # what happens if question is deleted?? 
    # in models, also they will be deleted.
    question = models.ForeignKey(Question, on_delete=models.CASCADE)


    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    

    def __str__(self):
        return self.choice_text




de