from django.contrib import admin

from .models import Question, Choice

# yo page ma admin lee k garna milxa vanera garako ho, admin functionality use garako

# steps
#  1. model lerauna paryo
#  2. Register garna paryo  ( )

admin.site.site_header = "Pollster Admin"
admin.site.site_title = "Pollster Admin Area"
admin.site.index_title = "Welcome to the Pollster admin area"


class ChoiceInline(admin.TabularInline):
    # yesma kun model ho tyo specify garnee ho! hamro case ma choice!!
    #extra vanako chai, kati ota extra field hamlai chainee ho?? 3 ota garem
    model = Choice
    extra = 3



#  yo main jsto ho so, yesma chai admin.ModelAdmin garnee
class QuestionAdmin(admin.ModelAdmin):
    # below is the tuple
    # we need object, equivalent to dictonary 

    # (Name =none ) dictionary  with field with question text, 
    # pub_date == published date
    # classes vanako how it  is going to behave
    # tala ko tuple ho, 2 ota 6, hanging comma hunxa

    # tala ko basically ksto look hunxa vanera ho

    # question text: what is your favourite Python Framework ?
    # date information (show vanera 6) tyo collapse lee garako hola

    fieldsets = [(None, {'fields': ['question_text']}), ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}), ]
    inlines = [ChoiceInline]


# admin.site.register(Question)
# admin.site.register(Choice)

#  yo mathi ko lee k garxa vanee it will be like two places, Question ekatira, Choice Arko tira k kaam??

# choice question muni vayo vani po nice!!!  tsko lagi tablular inline use garnee

#  classuse garnee mathi ko jsto ani

admin.site.register(Question, QuestionAdmin)
