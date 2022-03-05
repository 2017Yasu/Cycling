from django.db import models

# Create your models here.

class Team(models.Model):
    team_id = models.CharField(primary_key=True, max_length=16)
    name = models.CharField(verbose_name="team_name", max_length=32)
    leader_id = models.CharField(max_length=16)

    @property
    def leader(self):
        return Cyclist.objects.get(user_id=self.leader_id)

class Cyclist(models.Model):
    user_id = models.CharField(primary_key=True, max_length=16)
    name = models.CharField(verbose_name="cyclist_name", max_length=32)
    team_id = models.CharField(max_length=16, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    @property
    def team(self):
        return Team.objects.get(team_id=self.team_id)

class CycleResults(models.Model):
    date = models.DateField()
    cyclist_id = models.ForeignKey(Cyclist, on_delete=models.CASCADE)
    duration = models.DurationField()
    distance = models.FloatField()
    average = models.FloatField(blank=True, null=False)
    max_velocity = models.FloatField(blank=True, null=True)
    route_url = models.URLField(blank=True, null=True)
