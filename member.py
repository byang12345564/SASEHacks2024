class Member:
    def __init__(self, name, age, gender, score):
        self.name = name
        self.age = age
        self.gender = gender
        self.score = score

    def __str__(self):
        string = "Name: " + self.name + "\nAge: " + self.age + "\nGender: " + self.gender + "\nHealth Score: " + str(self.score) + "\n"
        return string
