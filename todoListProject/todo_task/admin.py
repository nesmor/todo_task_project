from django.contrib import admin
from todo_task.models import User
from todo_task.models import TodoListTask

class UserAdmin(admin.ModelAdmin):
        list_display = ('name','email','phone','status')
        list_editable = ['status']

class TodoListTaskAdmin(admin.ModelAdmin):
        list_display = ('task','status','updated_date','user')
        list_editable = ['status']

admin.site.register(User,UserAdmin)
admin.site.register(TodoListTask,TodoListTaskAdmin)


# Register your models here.
