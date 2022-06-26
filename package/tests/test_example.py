""""
example unit test
"""
import pytest

from ${project_name} import example

@pytest.fixture()
def fixture_example():
    """fixture example"""
    return 10

@pytest.fixture()
def fixture_expected_example():
    """fixture expected example"""
    return 11

class TestExample():
    """example test"""
    def test_exeample(self):  # pylint: disable = redefined-outer-name
        """test example"""
        assert example.add_one(1) == 2
        assert example.add_one(0) == 1
        assert example.add_one(-1) == 0

    @pytest.mark.usefixtures('fixture_example', 'fixture_expected_example')
    def test_exeample_fixture_example(self, fixture_example, fixture_expected_example):  # pylint: disable = redefined-outer-name
        """test with example fixtures"""
        assert example.add_one(fixture_example) == fixture_expected_example
