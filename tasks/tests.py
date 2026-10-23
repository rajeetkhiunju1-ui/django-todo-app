from django.test import TestCase
from django.urls import reverse

from .models import Task


class TaskViewsTests(TestCase):
    def test_task_list_displays_created_tasks(self):
        task = Task.objects.create(
            title="Buy groceries",
            description="Get milk",
        )

        response = self.client.get(reverse("task_list"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, task.title)
        self.assertContains(response, task.description)

    def test_add_task_creates_task_and_returns_to_task_list(self):
        response = self.client.post(
            reverse("add_task"),
            {"title": "Finish homework", "description": "Math worksheet"},
        )

        self.assertRedirects(response, reverse("task_list"))
        self.assertTrue(
            Task.objects.filter(
                title="Finish homework",
                description="Math worksheet",
            ).exists()
        )
        self.assertContains(
            self.client.get(reverse("task_list")),
            "Finish homework",
        )
