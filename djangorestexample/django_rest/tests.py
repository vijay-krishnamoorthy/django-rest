from django.test import TestCase
from django_rest.models import Plan
# Create your tests here.
class PlanTest(TestCase):
    
    def setUp(self):
        Plan.objects.create(
            name="699",
            price=699,
            validity=74,
            description="Unlimited data and call plan for the premium users"
        )
        
    def test_plan_price(self):
        plan = Plan.objects.get(name="699")
        
        self.assertEqual(plan.price, 699)