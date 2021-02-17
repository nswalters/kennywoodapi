import json
from rest_framework import status
from rest_framework.test import APITestCase

from kennywoodapi.models import ParkArea, TargetPopulation


class ParkAreaTests(APITestCase):
    def setUp(self) -> None:
        """
        Initialize a couple of park areas and assign a couple
        of target population types
        """

        # Initialize user
        url = "/register"
        data = {
            "username": "test@test.com",
            "email": "test@test.com",
            "password": "password",
            "first_name": "test_firstname",
            "last_name": "test_lastname",
            "phone_number": "123-456-7890",
            "special_requirements": "wheelchair",
            "number_family_members": 3
        }
        response = self.client.post(url, data, format='json')
        json_response = json.loads(response.content)
        self.token = json_response["token"]

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Create target population records
        pop_kids = TargetPopulation.objects.create(
            name="Kids"
        )
        pop_kids.save()

        pop_adults = TargetPopulation.objects.create(
            name="Adults"
        )
        pop_adults.save()

        # Create park areas
        adult_parkarea = ParkArea.objects.create(
            name="Adult Park Area",
            target_population=pop_adults
        )
        adult_parkarea.save()

        kids_parkarea = ParkArea.objects.create(
            name="Kids Park Area",
            target_population=pop_kids
        )
        kids_parkarea.save()

    def test_list_park_areas(self):
        """
        Get list of park areas
        """

        url = "/areas"
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        response = self.client.get(url, None, format='json')
        json_response = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(json_response), 2)

    def test_retrieve_single_park_area(self):
        """
        Get a specific park area
        """

        url = "/areas/1"
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        response = self.client.get(url, None, format='json')
        json_response = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json_response["id"], 1)
        self.assertEqual(json_response["name"], "Adult Park Area")
        self.assertEqual(json_response["target_population"]["name"], "Adults")
