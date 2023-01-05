from django.forms import model_to_dict
from django.test import TestCase
from django.urls import resolve, reverse

from core.models import Contact


# Create your tests here.
class ContactModelTest(TestCase):
    def test_create_contact(self):
        new_contact = Contact.objects.create(
            fullname='Jhon Doe',
            phone_number='555-0199'
        )

        self.assertEqual(
            Contact.objects.count(), 1
        )

        contact = Contact.objects.first()
        self.assertEqual(
            contact,
            new_contact
        )

    def test_delete_contact(self):
        contact = Contact.objects.create(
            fullname='Jhon Doe',
            phone_number='555-0199'
        )

        Contact.objects.create(
            fullname='Kathleen J. Warren',
            phone_number='555-1011'
        )

        self.assertEqual(
            Contact.objects.count(),
            2
        )

        Contact.objects.filter(
            id=contact.id
        ).delete()

        self.assertEqual(
            Contact.objects.count(),
            1
        )

    def test_update_contact(self):
        Contact.objects.create(
            fullname='Jhon Doe',
            phone_number='555-0199'
        )

        Contact.objects.filter(
            phone_number='555-0199'
        ).update(
            fullname='New Name'
        )

        contact = Contact.objects.first()

        self.assertEqual(
            contact.fullname,
            'New Name'
        )


class ContactListViewTest(TestCase):
    def setUp(self) -> None:
        self.url = reverse('contact_list')

        self.contact = Contact.objects.create(
            fullname='Jhon Doe',
            phone_number='555-0199'
        )

    def test_url_view(self):
        self.assertEqual(
            resolve(self.url).view_name,
            'contact_list'
        )

    def test_list_view(self):
        response = self.client.get(
            self.url
        )

        data = response.json()
        self.assertTrue(
            isinstance(data, list)
        )

    def test_list_view_content(self):
        response = self.client.get(
            self.url
        )
        data = response.json()

        self.assertEqual(
            data[0],
            model_to_dict(
                self.contact
            )
        )
