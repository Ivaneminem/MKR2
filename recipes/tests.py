from django.test import TestCase
from django.urls import reverse
from .models import Recipe
from django.utils import timezone

class RecipeViewTests(TestCase):

    def setUp(self):
        self.recipe = Recipe.objects.create(
            title="Test Recipe",
            description="Test Description",
            created_at=timezone.now()
        )

    def test_main_view(self):
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Recipe")

    def test_recipe_detail_view(self):
        response = self.client.get(reverse('recipe_detail', args=[self.recipe.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Description")
