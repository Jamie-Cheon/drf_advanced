from django.contrib.auth.models import User
from munch import Munch
from rest_framework import status
from rest_framework.test import APITestCase
from model_bakery import baker


# Test suite has a 'client' attr of the APIClient type that can be used to simulate API class.
# It has methods for all standard HTTP calls: get, post, put, patch, delete, head, options.
# Also, client has methods to authenticate a user by the login credentials, token, or just the User objects.
# In this test, I am authenticating by the third way, just passing a user directly to the force_authenticate() method

class UserTestCase(APITestCase):
    def setUp(self) -> None:
        self.users = baker.make('auth.User', _quantity=3)   # Create random 3 users automatically

    def test_should_list(self):                             # Check GET: api/users running well
        print('List Test')

        self.client.force_authenticate(user=self.users[0])  # forcibly authenticates each request.
        response = self.client.get('/api/users')

        # response : <Response status_code=200, "application/json">
        # response.data : OrderedDict([('next', None), ('previous', None), ('results', [OrderedDict([('id', 3), ...])
        # response.data['results'] : user list that custom pagination has been applied

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for user_response, user in zip(response.data['results'], self.users[::-1]):
            self.assertEqual(user_response['id'], user.id)
            self.assertEqual(user_response['username'], user.username)

    def test_should_create(self):                           # Check POST: api/users running well
        print('Create Test')
        data = {'username': 'abc'}

        response = self.client.post('/api/users', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        user_response = response.data
        self.assertTrue(user_response['id'])
        self.assertEqual(user_response['username'], data['username'])

    def test_should_get(self):                              # Check GET: api/users/<int:pk> running well
        print('Get Test')

        for i, user in enumerate(self.users):
            if user.id:
                user = self.users[i]
                self.client.force_authenticate(user=user)
                response = self.client.get(f'/api/users/{user.id}')

                self.assertEqual(response.status_code, status.HTTP_200_OK)

                # A Munch is a Python dictionary that provides attribute-style access
                user_response = Munch(response.data)
                self.assertTrue(user_response.id)
                self.assertEqual(user_response.id, user.id)
                self.assertEqual(user_response.username, user.username)
            else:
                continue

    def test_should_update(self):                           # Check UPDATE: api/users/<int:pk> running well
        print('Update Test')

        for i, user in enumerate(self.users):
            if user.id:
                user = self.users[i]
                self.client.force_authenticate(user=user)
                prev_username = user.username

                data = {'username': 'new'+str(i)}
                response = self.client.put(f'/api/users/{user.id}', data=data)

                # A Munch is a Python dictionary that provides attribute-style access
                user_response = Munch(response.data)
                self.assertTrue(user_response.id)
                self.assertNotEqual(user_response.id, prev_username)
                self.assertEqual(user_response.username, data['username'])
            else:
                continue

    def test_should_delete(self):                           # Check DELETE: api/users/<int:pk> running well
        print('Delete Test')

        for i, user in enumerate(self.users):
            if user.id:
                user = self.users[i]
                self.client.force_authenticate(user=user)

                response = self.client.delete(f'/api/users/{user.id}')

                self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
                self.assertFalse(User.objects.filter(id=user.id).exists())

