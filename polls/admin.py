from django.contrib import admin

from.models import Choice, Question


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['question_text'] # 添加一个搜索框
    list_filter = ['pub_date'] # 添加一个过滤器
    list_display = ('question_text', 'pub_date', 'was_published_recently') # 更改显示问题的列表页
    fieldsets = [
        (None,              {'fields':['question_text']}),
        ('Date information',{'fields':['pub_date'],'classes':['collapse']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question,QuestionAdmin)