
from datetime import date

backend = {
    "aadekunle@afexnigeria.com": {
        "firstname": "abraham",
        "lastname": "adekunle",
        "attendance": 12,
        "day of birth": [13, 1],
        "height": 180,
        "weight": 75,
        "age": 25,
        "e-mail": "aadekunle@afexnigeria.com"
    },

    "yoyedele@afexnigeria.com": {
        "firstname": "yussuff",
        "lastname": "oyedele",
        "attendance": 10,
        "day of birth": [22, 12],
        "height": 130,
        "weight": 65,
        "age": 28,
        "e-mail": "yoyedele@afexnigeria.com"
    },

    "aadeleke@afexnigeria.com": {
        "firstname": "awwal",
        "lastname": "adeleke",
        "attendance": 9,
        "day of birth": [3, 7],
        "height": 240,
        "weight": 78,
        "age": 27,
        "e-mail": "aadeleke@afexnigeria.com"
    },

    "aadeyeye@afexnigeria.com": {
        "firstname": "adebusola",
        "lastname": "adeyeye",
        "attendance": 12,
        "day of birth": [29, 6],
        "height": 200,
        "weight": 98,
        "age": 29,
        "e-mail": "aadeyeye@afexnigeria.com"
    },

    "bbalogun@afexnigeria.com": {
        "firstname": "bashir",
        "lastname": "balogun",
        "attendance": 8,
        "day of birth": [17, 5],
        "height": 170,
        "weight": 72,
        "age": 24,
        "e-mail": "bbalogun@afexnigeria.com"
    },

    "asalaam@afexnigeria.com": {
        "firstname": "abdullahi",
        "lastname": "salaam",
        "attendance": 9,
        "day of birth": [27, 8],
        "height": 180,
        "weight": 75,
        "age": 27,
        "e-mail": "asalaam@afexnigeria.com"
    },

    "fadeosun@afexnigeria.com": {
        "firstname": "faith",
        "lastname": "adeosun",
        "attendance": 11,
        "day of birth": [17, 2],
        "height": 15,
        "weight": 67,
        "age": 28,
        "e-mail": "fadeosun@afexnigeria.com"
    },

    "asharaufdeen@afexnigeria.com": {
        "firstname": "ahmad",
        "lastname": "sharaufdeen",
        "attendance": 10,
        "day of birth": [10, 7],
        "height": 189,
        "weight": 79,
        "age": 34,
        "e-mail": "asharaufdeen@afexnigeria.com"
    },

    "labisoye@afexnigeria.com": {
        "firstname": "lukman",
        "lastname": "abisoye",
        "attendance": 11,
        "day of birth": [5, 6],
        "height": 190,
        "weight": 87,
        "age": 28,
        "e-mail": "labisoye@afexnigeria.com"
    },

    "togunbiyi@afexnigeria.com": {
        "firstname": "Toluwanimi",
        "lastname": "ogunbiyi",
        "attendance": 11,
        "day of birth": [21, 4],
        "month of birth": "november",
        "height": 180,
        "weight": 75,
        "age": 24,
        "e-mail": "togunbiyi@afexnigeria.com"
    },

    "atajudeen@afexnigeria.com": {
        "firstname": "Abdulwalii",
        "lastname": "Tajudeen",
        "attendance": 7,
        "day of birth": [13, 11],
        "height": 198,
        "weight": 75,
        "age": 45,
        "e-mail": "atajudeen@afexnigeria.com"
    }
}


class ClassProfile:
    # global backend

    def __init__(self, **b_end):
        self.data = b_end
        # self.firstname = b_end["firstname"]
        # self.lastname = b_end["lastname"]
        # self.attendance = b_end["attendance"]
        # self.date_of_birth = b_end["day of birth"]
        # self.height = b_end["height"]
        # self.weight = b_end['weight']
        # self.age = b_end['age']
        # self.email = b_end['e-mail']

    def attendance_alterator(self, email, increment):
        if email in self.data:
            self.data[email]["attendance"] += increment
            return self.data[email]
        return "Error!,Invalid e_mail"

    def update_firstname_lastname(self, email, new_firstname, new_lastname):
        if email in self.data:
            self.data[email]["firstname"] = new_firstname
            self.data[email]["lastname"] = new_lastname
            return self.data[email]
        return "Error!,Invalid e_mail"

    def get_birthmonth(self, email):
        month = {1: "january", 2: 'february', 3: "march", 4: "april", 5: "may", 6: "june", 7: "july",
                 8: "august", 9: "september", 10: "october", 11: "november", 12: "december"}
        if email in self.data:
            return month[(self.data[email]["day of birth"])[1]]
        return "Error!,Invalid e_mail"

    def get_fullname(self, email):
        if email in self.data:
            f_name = str(self.data[email]['firstname']).title()
            l_name = str(self.data[email]['lastname']).title()
            return f"{f_name} {l_name}"
        return "Error!,Invalid e_mail"

    def calculate_birth_year(self, email):
        if email in self.data:
            return date.today().year - self.data[email]["age"]
        return "Error!,Invalid e_mail"

    def bmi(self, email):
        if email in self.data:
            return self.data[email]["weight"] / ((self.data[email]["height"] / 100) ** 2)
        return "Error!,Invalid e_mail"

    def initials(self, email):
        if email in self.data:
            return f"{str((self.data[email]['firstname'])[0]).title()} . {str((self.data[email]['lastname'])[0]).title()}"
        return "Error!,Invalid e_mail"

    def average_of_class(self):
        age = []
        for x in self.data:
            age.append(self.data[x]["age"])
        return sum(age) / len(age)

    def minimum_age(self):
        age = []
        for x in self.data:
            age.append(self.data[x]["age"])
        age.sort()
        return age[0]

    def maximum_age(self):
        age = []
        for x in self.data:
            age.append(self.data[x]["age"])
        age.sort()
        return age[-1]

    def population(self):
        return len(self.data)

    def remove_profile(self, email):
        if email in self.data:
            del self.data[email]
            return self.data
        return "Error!,Invalid e_mail"

    def add_profile(self):
        n_data = {}
        firstname = input("what is your firstname ? ")
        lastname = input("what is your lastname  ?")
        atten_dance = int(input("input the number of times you were present"))
        day_ob = list(input("what is your date of birth ?.....input day and month "))
        h_ight = int(input("what is your height ? "))
        w_ight = int(input("what is your weight ? "))
        age = int(input("what is your age ? "))
        email = input("what is your e_mail ?")

        n_data['firstname'] = firstname
        n_data['lastname'] = lastname
        n_data['attendance'] = atten_dance
        n_data['day of birth'] = day_ob
        n_data['height'] = h_ight
        n_data['weight'] = w_ight
        n_data['age'] = age
        n_data["e-mail"] = email

        self.data.update(n_data)
        return self.data

    def group_by_month(self):
        grouping = []
        for x in self.data:
            grouping.append(((self.data[x]["day of birth"])[1]))

        grouping.sort()

        for x in self.data:
            for y in grouping:
                if ((self.data[x]["day of birth"])[1]) == y:
                    grouping[grouping.index(y)] = self.data[x]

        return grouping


c = ClassProfile(**backend).group_by_month()
print(c)
