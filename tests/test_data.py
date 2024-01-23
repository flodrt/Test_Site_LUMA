from faker import Faker
fake = Faker()


class TestData:
    def __init__(self):
        self.lastname = fake.last_name()
        print ("                                      Données a utiliser pour les test")
        print ("lastname                  :   ",self.lastname)
        self.firstname = fake.first_name()
        print ("firstname                 :   ",self.firstname)
        self.email = fake.ascii_email()
        print ("Email                     :   ",self.email)
        self.password = fake.password(length=8, special_chars=True, digits=True, upper_case=True, lower_case=True)
        print ("Password                  :   ",self.password)
        self.too_short_password = fake.password(length=5, special_chars=True, digits=True, upper_case=True, lower_case=True)
        print ("Option mpd trop court     :   ", self.too_short_password)
        self.only_two_char_type_password = fake.password(length=8, special_chars=False, digits=True, upper_case=False, lower_case=True)
        print ("Option mdp sans majuscule :   ", self.only_two_char_type_password)
    
data = TestData()