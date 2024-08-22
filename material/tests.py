from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from material.models import Course, Lesson, Subscription
from users.models import User


class TestLessons(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(email="test@mail.ru")
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(title="Test", description="Описание Test")
        self.lesson = Lesson.objects.create(
            course=self.course,
            title="Test урок",
            description="Test описание",
            owner=self.user,
            url_video="https://www.youtube.com/watch",
        )

    def test_create_lesson(self):
        """ Тестирование создания урока """

        url = reverse("material:lesson_create")
        data = {
            "title": "Test урок",
            "description": "Test описание",
            "course": self.lesson.course.id,
            "url_video": "https://www.youtube.com/watch",
        }

        response = self.client.post(url, data=data)
        data = response.json()
        print(data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json(),
                         {'id': 2, 'title': 'Test урок', 'description': 'Test описание', 'preview': None,
                          'url_video': 'https://www.youtube.com/watch', 'course': 3, 'owner': 3})

    def test_edit_lesson(self):
        """ Тестирование изменения урока """

        url = reverse("material:lesson_update", args=(self.lesson.pk,))
        data = {
            "title": "Test Lesson",
            "description": "Test1",
            "course": self.lesson.course.id,
            "url_video": "https://www.youtube.com/watch1",
        }

        response = self.client.put(url, data=data)
        data = response.json()
        print(data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {'id': 4, 'title': 'Test Lesson', 'description': 'Test1', 'preview': None,
                                           'url_video': 'https://www.youtube.com/watch1', 'course': 5, 'owner': 5})

    def test_list_lesson(self):
        """ Тестирование списка урока """

        url = reverse("material:lesson_list")

        response = self.client.get(url)
        data = response.json()
        print(data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("count"), 1)

    def test_retrieve_lesson(self):
        """ Тестирование просмотра одного урока """

        url = reverse("material:lesson_retrieve", args=(self.lesson.pk,))

        response = self.client.get(url)
        data = response.json()
        print(data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(),
                         {'id': 6, 'title': 'Test урок', 'description': 'Test описание', 'preview': None,
                          'url_video': 'https://www.youtube.com/watch', 'course': 7, 'owner': 7})

    def test_delete_lesson(self):
        """ Тестирование удаления урока """

        url = reverse("material:lesson_delete", args=(self.lesson.pk,))
        data = {
            "title": "Test Lesson",
            "description": "Test",
            "course": self.lesson.course.id,
            "url_video": "https://www.youtube.com/watch",
        }

        response = self.client.delete(url, data=data)
        data = response.json()
        print(data)


class SubscriptionTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email='test777@localhost')
        self.course = Course.objects.create(title='Програмное обеспечение')
        self.client.force_authenticate(user=self.user)
        self.url = reverse('material:subscription_create')

    def test_subscription_activate(self):
        """Тест подписки на курс"""
        data = {
            "user": self.user.id,
            "course": self.course.id,
        }
        response = self.client.post(self.url, data=data)
        data_res = response.json()
        print(data_res)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {
                "message": "Подписка добавлена",
            },
        )
        self.assertTrue(
            Subscription.objects.all().exists(),
        )

    def test_sub_deactivate(self):
        """Тест отписки с курса"""
        Subscription.objects.create(user=self.user, course=self.course)
        data = {
            "user": self.user.id,
            "course": self.course.id,
        }
        response = self.client.post(self.url, data=data)
        data_res = response.json()
        print(data_res)
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )
        self.assertEqual(
            response.json(),
            {
                "message": "Подписка удалена",
            },
        )
        self.assertFalse(
            Subscription.objects.all().exists(),
        )
