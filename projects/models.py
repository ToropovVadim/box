from django.db import models


class Publication(models.Model):
    pub_name = models.CharField('Автор', max_length=50)
    pub_title = models.CharField('Название публткацыи', max_length=80)
    pub_text = models.TextField('Текст')
    pub_date = models.DateTimeField('Дата')
    pub_image = models.ImageField('Картинка', upload_to="image/")

    class Meta:
        verbose_name = 'Публикацыя'
        verbose_name_plural = 'Публикацыи'

    def __str__(self):
        return '%s:%s' %(self.pub_title, self.pub_name)


class Comment(models.Model):
    Publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    author = models.CharField('Автор кометария', max_length=50)
    comment_text = models.CharField('Коментарий', max_length=300)

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'

    def __str__(self):
        return self.author
