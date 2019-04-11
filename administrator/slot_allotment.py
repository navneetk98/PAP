def slot_allotment(batch):
    students = (batch.profile_set.all()).order_by("-cpi")
    batch_size = batch.group_size
    i = batch_size
    for s in students:
        s.user.teamformation.slot_no = int(i/batch_size)
        i = i+1
        s.user.teamformation.save()
