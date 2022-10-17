# what do we need to import?
from stuff import do_maths, add_fruit, find_cat_by_id, how_many_sweets, fetch_stuff
import pytest
import stuff
from unittest import mock
import requests

# do_maths test with multiple cases
def test_maths(): assert 2 + 4 == 6

# def test_do_maths(): assert do_maths(3,4) == 7
@pytest.mark.parametrize("x, y, expected", [(2, 3, 5), (4, -1, 3), (0, 0, 0)])
def test_do_maths(x, y, expected): assert do_maths(x, y) == expected

# add_fruit test with reusable data fixture - is new fruit in the salad?
def test_add_fruit(fruits_test_data):
    salad = add_fruit('grape', fruits_test_data)
    assert "grape" in salad
    assert salad[-1] == 'grape'
# how_many_sweets test throws StuffError when no people
def test_how_many_sweets():
    with pytest.raises(Exception, match="We need some people to share sweets with!"):
        assert how_many_sweets(['rowntrees fruit pastels'], [])
# find_cat_by_id monkeypatching fake cats data
def test_find_cat_by_id(monkeypatch):
    mock_cats = [{'id': 1, 'name': 'Zelda'}, {'id': 2, 'name': 'Brian'}]
    monkeypatch.setattr(stuff, "cats", mock_cats)
    result = find_cat_by_id(2)
    assert result['name'] == 'Brian'
    assert result == {'id': 2, 'name': 'Brian'}

# test fetch stuff function using unit test
def test_fetch_stuff():
    mock_response = mock.Mock() #this creates a mock response
    mock_response.json.return_value = {'email': 'test@testing.com'}
    mock_response_get = mock.Mock(return_value = mock_response)
    requests.get = mock_response_get
    #call the function
    fetch_stuff()
    mock_response_get.assert_called_with('https://api.github.com/users/getfutureproof')