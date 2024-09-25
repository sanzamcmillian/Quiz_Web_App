from django.urls import reverse, resolve
from django.test import SimpleTestCase
from quiz.views import landing_view
from quiz import views as quiz_views

class TestUrls(SimpleTestCase):

    def test_home_url_is_resolved(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, landing_view)