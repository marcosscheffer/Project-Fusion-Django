import uuid
from django.test import TestCase
from model_mommy import mommy

from core.models import gen_file_path


class GetFilePathTestCase(TestCase):
    def setUp(self):
        self.filename = f'{uuid.uuid4()}.png'
        
    def test_get_file_path(self):
        file = gen_file_path(None, 'test.png')
        self.assertTrue(len(file), len(self.filename))
        

class ServiceTestCase(TestCase):
    def setUp(self):
        self.service = mommy.make('Services')

    def test_str(self):
        self.assertEqual(str(self.service), self.service.service)


class PositionTestCase(TestCase):
    def setUp(self):
        self.position = mommy.make('Position')
        
    def test_str(self):
        self.assertEqual(str(self.position), self.position.title)
        
        
class FeatureTestCase(TestCase):
    def setUp(self):
        self.feature = mommy.make('Features')
        
    def test_str(self):
        self.assertEqual(str(self.feature), self.feature.title)


class TeamTestCase(TestCase):
    def setUp(self):
        self.team = mommy.make('Team')
        
    def test_str(self):
        self.assertEqual(str(self.team), self.team.name)
