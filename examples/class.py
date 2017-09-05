class TrainingGroup:
    # class members
    date = ''
    participants = []

    # class methods
    def __init__(self, date, participants):
        self.date = date
        self.participants = participants

    def __str__(self):
        return '{0} participants on {1}'.format(len(self.participants), self.date)

    def kick_member(self, idiot):
        new_members = []
        for member in self.participants:
            if idiot != member:
                new_members.append(member)
            else:
                print('kicking {0}'.format(idiot))
        self.participants = new_members


group = TrainingGroup('2015-08-10', ['Tom', 'Dick', 'Harry'])
print(group)
print(group.participants)
group.kick_member('Dick')
print(group)
print(group.participants)
