# Intro to Testing Python _(45 mins)_

## Objectives
_These objectives are crafted using [Bloom's Taxonomy](https://tips.uark.edu/using-blooms-taxonomy/) \
Please refer to [this action verb list](https://tips.uark.edu/blooms-taxonomy-verb-chart/) when adding or updating objectives_
- Identify testing options in Python
- Write basic tests using pytest
- Use pytest fixtures to enhance test functionality

## Overview _(5 mins)_
:grey_question: **Why test?** \
**A**: All the reasons! This should feel like a ridiculous question to them by now. Why wouldn't we test?

**Testing Tools**
- [ ] :speaking_head: Tell students that just like for other languages, many options are avaliable for testing python
- [ ] :speaking_head: Tell students that the built-in `unittest` module is quite popular
- [ ] :speaking_head: Tell students one of the most popular options is `pytest` which is what we will use today

---

## Setup _(5 mins)_

**Install** 
- [ ] :speaking_head: Tell students we will install pytest as a dev dependency 
- [ ] :computer: Run `pipenv install --dev pytest` and note its presence in the Pipfile

**Test Files** 
- [ ] :speaking_head: Tell students that pytest will scan the codebase for files named `test_<something>.py`
- [ ] :speaking_head: Tell students we can customise this behaviour if we want but for now this is fine
- [ ] :computer: Create a `test_stuff.py` file

**Test Functions** 
- [ ] :speaking_head: Tell students that within the test files, by default only tests called `test_<something>` will be run
- [ ] :computer: Change name of "test.py" file to "test_stuff.py" and explain that otherwise we will see "no tests ran" error
- [ ] :speaking_head: Tell students we again can customise this behaviour if we want but for now this is fine
- [ ] :speaking_head: Tell students we can also group tests into a class but we will start with individual tests

**Scripts & Coverage**
- [ ] :speaking_head: Tell students we can start a test run with `pytest`, optionally telling it where to look
- [ ] :speaking_head: Tell students we can also create a script for this
- [ ] :computer: In Pipfile add a scripts of `test="pytest ."`
- [ ] :speaking_head: Tell students we will install `pytest-cov` as our coverage reporter
- [ ] :computer: `pipenv install --dev pytest-cov` and create a script `coverage = "pytest --cov-report term-missing --cov=."` briefly explaining each part

---

## Testing Techniques _(30 mins)_
_**NB: Use [student demo repo](https://github.com/getfutureproof/fp_study_notes_testing_with_pytest/blob/master/essentials/test_stuff.py) for inspiration**_

**Basic Assertions** _(5 mins)_
- [ ] :computer: Create a basic assertion eg. `def test_maths(): assert 2 + 2 == 4` and run the test suite with `pipenv run test` noting the `.` for the running test
- [ ] :computer: Change the test to fail eg. `assert 2 + 2 == 5` and run the test again noting how a failed test presents
- [ ] :computer: Import `stuff` and create a test for `do_maths` with `from stuff import do_maths` with a basic assertion eg. `assert do_maths(2, 2) == 4`

**Multiple Cases with parameterize** _(5 mins)_
- [ ] :speaking_head: Tell students it would be good to reuse this test but with different numbers
- [ ] :speaking_head: Tell students that pytest has some built in tools to help improve our testing
- [ ] :computer: Pass `test_do_maths` `x, y, expected` and update the body to `assert stuff.do_maths(x, y) == expected`
- [ ] :speaking_head: Tell students we will use pytest's `parametrize` tool to yield multiple sets of data in one at a time
- [ ] :computer: Add the decorator `@pytest.mark.parametrize('x, y, expected', [(2, 4, 6), (3, 4, 7), (9, 2, 11)])` and ask students how many tests will be run using this function _(3, one for each tuple in the list passed to parametrize)_
- [ ] :computer: Run the tests and note that we need to `import pytest` to access this feature

**Reusable data with fixtures** _(5 mins)_
- [ ] :speaking_head: Tell students that we might need to repeat logic and/or data in multiple test functions
- [ ] :speaking_head: Tell students we can use pytest to create 'fixtures' that can be passed to any test function
- [ ] :exclamation: Advise students that this will be a very contrived demo but soon we will make good use of these when testing APIs!
- [ ] :computer: Create a `conftest.py` file and `import pytest`
- [ ] :speaking_head: Tell students this is a setup file which will be run before the tests
- [ ] :computer: Add a function that returns some data eg. `fruits_test_data(): return ['banana', 'apple']`
- [ ] :computer: Add the `@pytest.fixture` decorator
- [ ] :computer: Return to the test file and pass `fruits_test_data` to a new `test_add_fruit` test and complete the test

**Testing that an error is thrown** _(5 mins)_
- [ ] :computer: Create a `test_how_many_sweets` function and show students the original
- [ ] :speaking_head: Tell students we want to check that an error is thrown when an empty list is passed as the second argument
- [ ] :computer: Add the test body and ask students what they think this is doing
- [ ] :computer: Run the test

**Monkeypatching data** _(5 mins)_
- [ ] :computer: Show students the `find_cat_by_id` function and point out that it references a variable 'cats'
- [ ] :speaking_head: Tell students we want to take control of this 'cats' variable during test for consistent results
- [ ] :speaking_head: Tell students we will use pytest's monkeypatch feature for this
- [ ] :computer: Create `test_find_cat_by_id` and pass it `(monkeypatch)`
- [ ] :speaking_head: Tell students that monkeypatch can `set` an `attr`ibute by receiving a module, a method name and a value to `setattr`
- [ ] :computer: Add `monkeypatch.setattr(stuff, "cats", mock_cats)` and ask what each part is
- [ ] :computer: Create mock_cats (either as fixture or just local) and complete the test
- [ ] :computer: Run the test noting the benefit here of the fake data

**Checking system output** _(5 mins)_
- [ ] :computer: Show students the `greeting` function and point out that it prints out to the console
- [ ] :speaking_head: Tell students we will use pytest's caysys feature to scan the console output for content
- [ ] :computer: Create `test_greeting` and pass it `(capsys)`
- [ ] :speaking_head: Tell students that capsys offers access to the standard output and error logs
- [ ] :computer: Add `out, err = capsys.readouterr()` and complete the test
- [ ] :computer: Run the test

**Mocking**
- [ ] :speaking_head: Tell students that monkeypatch is great but sometimes we need more robust mocking
- [ ] :speaking_head: Tell students we will borrow from the inbuilt `unittest` module for this
- [ ] :computer: Add `from unittest import mock`
- [ ] :computer: Create a `test_fetch_stuff` test
- [ ] :computer: Create a mock response with `mock_response = mock.Mock()`
- [ ] :computer: Set the return value of a fake `json` method with `mock_response.json.return_value = { 'email': 'test@testing.com' }`
- [ ] :computer: Create a mock requests.get with `mock_requests_get = mock.Mock(return_value=mock_response)`
- [ ] :computer: Re-assign requests.get with `requests.get = mock_requests_get`
- [ ] :computer: Call the function
- [ ] :computer: Assert that requests.get was called with eg. `mock_requests_get.assert_called_with('https://api.github.com/users/getfutureproof')`
- [ ] :computer: Show students where to find more options at the [unittest mock object docs](https://docs.python.org/3/library/unittest.mock.html)

---

## Questions _(5 mins)_
- [ ] :exclamation: Advise students that the demo repo also has some Flask API testing examples that will be useful tomorrow but not to worry about today!
- [ ] :exclamation: Advise students that the Prodedural & OO demo repos from today also have test suites with more complex examples including using unittest's `mock` for when `monkeypatch` can't quite do everything we need
