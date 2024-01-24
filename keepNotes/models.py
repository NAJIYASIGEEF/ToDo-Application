from django.db import models

class Notes(models.Model):
    title=models.CharField(max_length=200)
    created_date=models.DateTimeField()
    user=models.CharField(max_length=200)
    options=(
        ("pending","pending"),
        ("update","update"),
        ("complete","complete")
    )
    status=models.CharField(max_length=200,choices=options,default="pending")