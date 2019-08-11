from django.db import models
from django.contrib.auth.models import User

class botany(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='images/')
    body = models.TextField()
    votes_total = models.IntegerField(default=0)
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    def summary(self):
        return self.body[:100]

    def pub_dated(self):
        return self.pub_date.strftime( '%A %e, %Y' )

    def __str__(self):
        return self.title


class commerce(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='images/')
    body = models.TextField()
    votes_total = models.IntegerField(default=0)
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    def summary(self):
        return self.body[:100]

    def pub_dated(self):
        return self.pub_date.strftime( '%A %e, %Y' )

    def __str__(self):
        return self.title


class cs(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='images/')
    body = models.TextField()
    votes_total = models.IntegerField(default=0)
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    def summary(self):
        return self.body[:100]

    def pub_dated(self):
        return self.pub_date.strftime( '%A %e, %Y' )

    def __str__(self):
        return self.title

class geography(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='images/')
    body = models.TextField()
    votes_total = models.IntegerField(default=0)
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    def summary(self):
        return self.body[:100]

    def pub_dated(self):
        return self.pub_date.strftime( '%A %e, %Y' )

    def __str__(self):
        return self.title


class history(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='images/')
    body = models.TextField()
    votes_total = models.IntegerField(default=0)
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    def summary(self):
        return self.body[:100]

    def pub_dated(self):
        return self.pub_date.strftime( '%A %e, %Y' )

    def __str__(self):
        return self.title


class math(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='images/')
    body = models.TextField()
    votes_total = models.IntegerField(default=0)
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    def summary(self):
        return self.body[:100]

    def pub_dated(self):
        return self.pub_date.strftime( '%A %e, %Y' )

    def __str__(self):
        return self.title


class physics(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='images/')
    body = models.TextField()
    votes_total = models.IntegerField(default=0)
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    def summary(self):
        return self.body[:100]

    def pub_dated(self):
        return self.pub_date.strftime( '%A %e, %Y' )

    def __str__(self):
        return self.title

class yoga(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='images/')
    body = models.TextField()
    votes_total = models.IntegerField(default=0)
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    def summary(self):
        return self.body[:100]

    def pub_dated(self):
        return self.pub_date.strftime( '%A %e, %Y' )

    def __str__(self):
        return self.title


class zoology(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='images/')
    body = models.TextField()
    votes_total = models.IntegerField(default=0)
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    def summary(self):
        return self.body[:100]

    def pub_dated(self):
        return self.pub_date.strftime( '%A %e, %Y' )

    def __str__(self):
        return self.title


