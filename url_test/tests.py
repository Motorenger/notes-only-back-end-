from django.test import TestCase
from django.urls import reverse


class TestsViewTests(TestCase):

    def test_int_input_with_int(self):
        response = self.client.get(reverse('url_test:int', args=(1,)))
        self.assertEqual(response.status_code, 200)

    def test_int_input_with_str(self):
        response = self.client.get(reverse('url_test:str', args=('hello',)))
        self.assertEqual(response.status_code, 200)

    def test_int_input_with_path(self):
        response = self.client.get(reverse('url_test:path', args=('hello',)))
        self.assertEqual(response.status_code, 200)

    def test_int_input_with_uuid(self):
        response = self.client.get(reverse('url_test:uuid', args=('075194d3-6885-417e-a8a8-6c931e272f00',)))
        self.assertEqual(response.status_code, 200)

    def test_int_input_with_slug(self):
        response = self.client.get(reverse('url_test:slug', args=('just-a-slug',)))
        self.assertEqual(response.status_code, 200)

    def test_int_input_with_converter(self):
        response = self.client.get(reverse('url_test:converter', args=(2000,)))
        self.assertEqual(response.status_code, 200)

    def test_int_input_with_reg_exp(self):
        response = self.client.get(reverse('url_test:reg_exp', args=(2000,)))
        self.assertEqual(response.status_code, 200)

    def test_int_input_with_nested(self):
        response = self.client.get(reverse('url_test:nested', args=(21,)))
        self.assertEqual(response.status_code, 200)