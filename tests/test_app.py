import pytest

from myapp.app import multiply_by_two, divide_by_two

#save in excel  pytest -l --tb=long  --capture sys -rP -rF --excelreport=report%Y-%m-%dT%H%M.xlsx
#save report in html pytest -l --tb=long  --capture sys -rP -rF --html=test.html   


@pytest.fixture()
def numbers():
    print("login with daetails ")
    a = 10
    b = 20
    yield [a,b]
    print("logout")



class TestApp:
    def test_multiplication(self, numbers):
        print("multiple")
        res = multiply_by_two(numbers[0])
        assert res == numbers[1]

    def test_division(self, numbers):
        print("divide")
        res = divide_by_two(numbers[1])
        assert res == numbers[0]
