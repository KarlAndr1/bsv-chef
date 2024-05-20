import pytest
from unittest.mock import Mock
from unittest.mock import patch

from src.controllers.recipecontroller import RecipeController

# add your test case implementation here
@pytest.mark.unit
@pytest.mark.parametrize(
	"take_best, get_readiness_of_recipes_return, randint_return, expect",
	[
		(True, {}, None, None),
		(True, { "r1": 0, "r2": 1 }, None, "r2"),
		(False, {}, None, None),
		(False, { "r1": 0, "r2": 1 }, 0, "r1")
	]
)

def test(take_best, get_readiness_of_recipes_return, randint_return, expect):
	mock_rc = Mock()
	mock_rc.recipes = {}
	mock_rc.get_readiness_of_recipes.return_value = get_readiness_of_recipes_return
	with patch("random.randint") as rand_mock:
		rand_mock.return_value = randint_return
		assert RecipeController.get_recipe(mock_rc, None, take_best) == expect
		
