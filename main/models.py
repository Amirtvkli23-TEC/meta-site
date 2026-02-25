from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='projects/')  # عکس اصلی
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.name

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='additional_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='projects/')
    caption = models.CharField(max_length=200, blank=True)

    def str(self):
        return f"{self.project.name} - {self.caption or 'Image'}"