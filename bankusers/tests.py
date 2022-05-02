from django.test import TestCase
from .models import Bankuser

# Create your tests here.
class ModelsTest(TestCase):
    def bankUser_test(self):
        bank_user_name = Bankuser.objects.create(user_name="Testinguser", user_surname="fromTheBanking" )
        self.assertEqual(str(bank_user_name.user_name), "Testinguser", "bank user names are not equal")
        self.assertEqual(str(bank_user_name.user_surname), "fromTheBanking", "bank user surnames are not equal")


ModelsTest().bankUser_test()