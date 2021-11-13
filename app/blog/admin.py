from django.contrib import admin

from .models import Note, Comment

@admin.register(Note)
class NoteAdimn(admin.ModelAdmin):
    #Поля в списке
    list_display = ('title', 'public', 'date_add', 'author', 'id', )

    #Группировка пля в режиме редактирования
    fields = ('date_add', ('title', 'public'), 'message', 'author')

    #Поля только для чтения в режиме редактирования
    readonly_fields = ('date_add', )

    #Поиск по выбранным полям
    search_fields = ['title', 'message', ]

    #Фильтры справа
    list_filter = ['public', 'author']


    def save_model(self, request, obj, form, change):
        # Добавляем текущего пользователя (если не выбран) при сохранении модели
        # docs: https://docs.djangoproject.com/en/3.1/ref/contrib/admin/#django.contrib.admin.ModelAdmin.save_model
        if not hasattr(obj, 'author') or not obj.author:
            obj.author = request.user
        super().save_model(request, obj, form, change)


# admin.site.register(Note)
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass