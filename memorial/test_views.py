from django.test import TestCase
from django.urls import reverse
from .models import Memorial
from .forms import MemorialForm

class ObtuarioTestCase(TestCase):
    def test_obtuario_view(self):
        # Create a test Memorial object
        memorial = Memorial.objects.create(
            obtuario='123',
            falecido='John Doe',
            data_nascimento='1990-01-01',
            sexo='M',
            idade=30,
            cor='White',
            mae='Jane Doe',
            data_falecimento='2020-01-01',
            data_sepultamento='2020-01-02',
            localizacao='Cemetery',
            quadra='A',
            conjunto='1',
            sepultura='10',
            previsao_exumacao='2021-01-01',
        )

        # Prepare the form data
        form_data = {
            'obtuario': '123',
            'falecido': 'John Doe',
            'data_nascimento': '1990-01-01',
            'sexo': 'M',
            'idade': 30,
            'cor': 'White',
            'mae': 'Jane Doe',
            'data_falecimento': '2020-01-01',
            'data_sepultamento': '2020-01-02',
            'localizacao': 'Cemetery',
            'quadra': 'A',
            'conjunto': '1',
            'sepultura': '10',
            'previsao_exumacao': '2021-01-01',
        }

        # Send a POST request to the obtuario view with the form data
        response = self.client.post(reverse('obtuario'), data=form_data)

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check that the form in the response context is an instance of MemorialForm
        self.assertIsInstance(response.context['form'], MemorialForm)

        # Check that the results in the response context match the created Memorial object
        self.assertQuerysetEqual(response.context['results'], [memorial], transform=lambda x: x)

    def test_obtuario_view_get(self):
        # Send a GET request to the obtuario view
        response = self.client.get(reverse('obtuario'))

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check that the form in the response context is an instance of MemorialForm
        self.assertIsInstance(response.context['form'], MemorialForm)

        # Check that the results in the response context is None
        self.assertIsNone(response.context['results'])