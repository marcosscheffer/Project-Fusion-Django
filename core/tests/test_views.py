from django.test import TestCase
from django.test import Client
from django.urls import reverse_lazy
from ..models import Services, Features, Team, Position

class IndexViewTestCase(TestCase):
    def setUp(self):
        self.data = {
            'name': 'test',
            'email': 'test@example.com',
            'subject': 'Test',
            'message': 'Test message'
        }
        self.client = Client()
        
        position = Position.objects.create(title="test")
        for i in range(10):
            Services.objects.create(service=f"services {i}")
            Team.objects.create(name=f"team {i}", position=position)
            Features.objects.create(title=f"features {i}")
        
    def test_form_valid(self):
        request = self.client.post(reverse_lazy('index'), data=self.data)
        self.assertEqual(request.status_code, 302)
        
    def test_form_invalid(self):
        data = {
            'name': 'test',
            'email': 'test@example.com',
        }
        request = self.client.post(reverse_lazy('index'), data=data)
        self.assertEqual(request.status_code, 200)
        
    def test_get_context_data(self):
        request = self.client.get(reverse_lazy('index'))
        
        self.assertEqual(request.status_code, 200)
        self.assertTrue('services' in request.context)
        self.assertTrue('team' in request.context)
        self.assertTrue('right_features' in request.context)
        self.assertTrue('left_features' in request.context)
        
        services = request.context['services']
        team = request.context['team']
        right_features = request.context['right_features']
        left_features = request.context['left_features']
        
        self.assertEqual(len(services), 10)
        self.assertEqual(len(team), 10)
        self.assertGreaterEqual(len(right_features), 0)
        self.assertGreaterEqual(len(left_features), 0)
        self.assertEqual(len(right_features) + len(left_features), 10)
        