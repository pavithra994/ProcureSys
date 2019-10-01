from accounts.models import User

STAFF = User.objects.get(email="staff@email.com").staff