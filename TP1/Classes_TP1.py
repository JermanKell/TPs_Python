import datetime

class Date:

    def __init__(self, date):
        split_date = date.split('/')
        self.date = split_date

    def __eq__(self, obj):
        flag = True
        i = 0
        while i < 3 and flag:
            if self.date[i] != obj.date[i]:
                flag = False
            else: i += 1
        if flag:
            print('Les dates sont les memes')
        else: print('Les dates sont differentes')

    def __lt__(self, obj):
        flag = True
        i = 0

        while i < 3 and flag:
            if self.date[i] >= obj.date[i]:
                flag = False
            else: i += 1

        if flag:
            print('True')
        else: print('False')

    def set_dates(self, date):
        split_date = date.split('/')
        self.date = split_date

    def get_dates(self):
        return self.date

    date = property(get_dates, set_dates)


class Etudiant:

    def __init__(self, firstName, lastName, Birthday):
        self.MAddress = None
        self.Age = 0
        self.FirstName = firstName
        self.LastName = lastName
        self.Birthday = Birthday

    def setmailaddress(self):
        self.MAddress = self.FirstName + "." + self.LastName + "@etu.univ-tours.fr"

    def getmailaddress(self):
        return self.MAddress

    def setage(self, AgeArray):
        now = datetime.datetime.now()
        self.Age = now.year - AgeArray[2]

        for i in range

    MAddress = property(getmailaddress, setmailaddress)
