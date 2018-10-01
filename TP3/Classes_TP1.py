import datetime

class Date:

    def __init__(self, string_date):
        if(type(string_date) is not str):
            raise TypeError("type str required")
        self._set_date(string_date)

    def _get_date(self):
        return self.__date

    def _set_date(self, string_date):
        if(type(string_date) is not str):
            raise TypeError("type str required")
        self.__date = string_date

    string_date = property(_get_date, _set_date)

    def __repr__(self):
        return str(self)

    def __str__(self):
        return str(self.__date)

    def __eq__(self, obj):
        flag = True
        i = 0
        self_date = self.__date.split('/')
        obj_date = obj.__date.split('/')

        while i < 3 and flag:
            if self_date[i] != obj_date[i]:
                flag = False
            else:
                i += 1
        return flag

    def __lt__(self, obj):
        self_date = self.__date.split('/')
        obj_date = obj.__date.split('/')

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

    def get_year(self):
        return int(self.__date.split('/')[2])

    def get_month(self):
        return int(self.__date.split('/')[1])

    def get_day(self):
        return int(self.__date.split('/')[0])

class Etudiant:

    def __init__(self, firstName, lastName, birthday):
        if (type(birthday) is not Date):
            raise TypeError("type Date required")
        self._set_Birthday(birthday)
        self._set_FirstName(firstName)
        self._set_LastName(lastName)


    def _get_FirstName(self):
        return self.__FirstName

    def _set_FirstName(self, firstName):
            self.__FirstName = firstName

    firstName = property(_get_FirstName, _set_FirstName)

    def _get_LastName(self):
        return self.__LastName

    def _set_LastName(self, lastName):
            self.__LastName = lastName

    lastName = property(_get_LastName, _set_LastName)

    def _get_Birthday(self):
        return self.__Birthday

    def _set_Birthday(self, birthday):
            self.__Birthday = birthday

    birthday = property(_get_Birthday, _set_Birthday)

    def _get_MAdress(self):
        return self.firstName + "." + self.lastName + "@etu.univ-tours.fr"

    def _get_Age(self):
        date_now = datetime.datetime.now()
        date_birthday = self._get_Birthday()
        #ignore leap years
        return int(((date_now.year*365 + date_now.month*30 + date_now.day) - (date_birthday.get_year()*365 + date_birthday.get_month()*30 + date_birthday.get_day()))/365)

    def __repr__(self):
        return str(self)

    def __str__(self):
        return self.firstName + " " + self.lastName + " " + str(self._get_Age())

#date_ludi = Date("04/09/1999")
#date_rapha = Date("08/08/1994")
#ludi = Etudiant("ludivine", "thibault", date_ludi)
#rapha = Etudiant("raphael", "lazzaroni", date_rapha)
#print(rapha._get_MAdress())
#print(rapha._get_Age())
#print(ludi._get_MAdress())
#print(ludi._get_Age())
