import datetime

class Date:

    def __init__(self, date):
        self.date = date

    def __eq__(self, obj):
        flag = True
        i = 0

        self_date = self.date.split('/')
        obj_date = obj.date.split('/')

        while i < 3 and flag:
            if self_date[i] != obj_date[i]:
                flag = False
            else: i += 1
        #if flag:
        #    print('Les dates sont les memes')
        #else: print('Les dates sont differentes')
        return flag

    def __lt__(self, obj):
        self_date = self.date.split('/')
        obj_date = obj.date.split('/')

        if self_date[2] < obj_date[2]:
            return True
        elif self_date[2] > obj_date[2]:
            return False
        else:
            if self_date[1] < obj_date[1]:
                return True
            if self_date[1] > obj_date[1]:
                return False
            else:
                if self_date[0] < obj_date[0]:
                    return True
                elif self_date[0] > obj_date[0]:
                    return False
                else:
                    return False
        #if flag:
        #   print('True')
        #else: print('False')

    def get_dates(self):
        return self.date

    date = property(get_dates)


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
