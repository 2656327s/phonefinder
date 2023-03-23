from django.test import TestCase
from models import UserProfile,Favourite,Review
from views import *
# Create your tests here.
class Modeltest(TestCase):

    def setUp(self)-> None:
        UserProfile.objects.create(
            user="Adam",
            website="http://127.0.0.1:8000/phonefinder/individual/Apple/iPhone-12-Pro",
            picture="null"
        )
        Favourite.objects.create(
            user="Charlie",
            phone_id="666777"
        )
        Review.objects.create(
            rating=9.0,
            model="iphone",
            title="The best website I have ever seen",
            comments="I love the phone",
            user="fcooper222",
            pub_date="2023/3/23"
        )

    def test_UserProfile_models(self):
        result_User=UserProfile.objects.get(user="Adam")
        result_website=UserProfile.objects.get(website="http://127.0.0.1:8000/phonefinder/individual/Apple/iPhone-12-Pro")
        result_picture=UserProfile.objects.get(picture="null")
        self.assertEqual(result_User.address,"Adam")
        self.assertTrue(result_User.status)
        self.assertEqual(result_website.address,"http://127.0.0.1:8000/phonefinder/individual/Apple/iPhone-12-Pro")
        self.assertTrue(result_website.status)
        self.assertEqual(result_picture.address,"null")
        self.assertTrue(result_picture.status)
    def test_Favourite_models(self):
        result_User=Favourite.objects.get(user="Charlie")
        result_phone_id=Favourite.objects.get(phone_id="666777")
        self.assertEqual(result_User.address, "Charlie")
        self.assertTrue(result_User.status)
        self.assertEqual(result_phone_id.address, "666777")
        self.assertTrue(result_phone_id.status)
    def test_Review_models(self):
        result_rating=Review.objects.get(rating=5.0)
        result_model=Review.objects.get(model="iphone")
        result_title=Review.objects.get(title="The best website I have ever seen")
        result_comments=Review.objects.get(comments="I love the phone")
        result_user=Review.objects.get(user="fcooper222")
        result_pub_date=Review.objects.get(pub_date="2023/3/23")
        self.assertEqual(result_rating.address, 5.0)
        self.assertTrue(result_rating.status)
        self.assertEqual(result_model.address, "iphone")
        self.assertTrue(result_model.status)
        self.assertEqual(result_title.address, "The best website I have ever seen")
        self.assertTrue(result_title.status)
        self.assertEqual(result_comments.address, "I love the phone")
        self.assertTrue(result_comments.status)
        self.assertEqual(result_user.address, "fcooper222")
        self.assertTrue(result_user.status)
        self.assertEqual(result_pub_date.address, "2023/3/23")
        self.assertTrue(result_pub_date.status)
class Indextest(TestCase):

    def test_index_page(self):
        response= self.client.get('app/index.html')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/index.html')
class Registertest(TestCase):
    def setUp(self) -> None:
        register('POST')
    #def Registertest(self):
        #UserForm=register.objects.get


