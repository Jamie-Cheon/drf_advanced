from rest_framework.test import APITestCase
from rest_framework import status
from model_bakery import baker
from cards.models import Card


class CardTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = baker.make('auth.User', _quantity=1)
        self.cards = baker.make(Card, _quantity=3)

    def list_test(self):
        print('List Test')

        self.client.force_authenticate(user=self.user[0])
        response = self.client.get('/api/cards')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for card_response, card in zip(response.data['results'], self.cards[::-1]):
            self.assertEqual(card_response['id'], card.id)
            self.assertEqual(card_response['name'], card.name)




