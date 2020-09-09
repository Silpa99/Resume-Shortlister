from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


from .models import Profile

def candidate_profile(sender, instance, created, **kwargs):
	if created:
		group = Group.objects.get(name='candidate')
		instance.groups.add(group)
		Profile.objects.create(
			username=instance,
			)
		print('Profile created!')

post_save.connect(candidate_profile, sender=User)