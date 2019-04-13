from django.contrib.auth.models import User
from professor.models import Professor


def student_database(path, batch):
    f = open(path)
    for line in f:
        line = line.split(',')
        user = User.objects.create_user(line[0], password=line[1])
        user.first_name = line[2]
        user.last_name = line[3]
        user.save()
        user.profile.cpi = line[4]
        #user.profile.group_ID = line[5]
        user.profile.batch = batch
        user.teamformation.slot_no = line[6]
        user.profile.save()
        user.teamformation.save()
        # Alot Slot_no and groupID(to Leaders)


# user_name ; password; f_name; l_name; cpi; group_id; slot_no


def professor_database(path, batch):
    f = open(path)
    for line in f:
        line = line.split(',')
        professor = Professor.objects.create(first_name=line[1], last_name=line[2], max_group=line[3],area_of_interest=line[4])
        professor.save()
        batch.professor.add(professor)
    batch.professor_data_uploaded = True
    batch.save()
