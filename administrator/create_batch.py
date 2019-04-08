from django.contrib.auth.models import User


def create_database(path):
    f = open(path)
    for line in f:
        line = line.split(',')
        user = User.objects.create_user(line[0], password=line[1])
        user.first_name = line[2]
        user.last_name = line[3]
        user.save()
        user.profile.cpi = line[4]
        user.profile.group_ID = line[5]
        user.teamformation.slot_no = line[6]
        user.profile.save()
        user.teamformation.save()

#user_name ; password; f_name; l_name; cpi; group_id; slot_no
