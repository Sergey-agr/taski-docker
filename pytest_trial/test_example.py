import pytest


def one_more(x):
    return x + 1

@pytest.mark.parametrize(
    'input_arg, expected_result',
    [
        (4, 5), 
        pytest.param(3, 5, marks=pytest.mark.xfail)  # Ожидается падение теста.
    ],
    ids=['First parameter', 'Second parameter',]
)
def test_one_more(input_arg, expected_result):  # Те же параметры, что и в декораторе.
    assert one_more(input_arg) == expected_result

def get_sort_list(string):
    new_list = sorted(string.split(', '))  # Сортируем список.
    return new_list 

def test_sort():
    """Тестируем функцию get_sort_list()."""
    result = get_sort_list('Яша, Саша, Маша, Даша')
    assert result == ['Даша', 'Маша', 'Саша', 'Яша']

def test_type():
    """Тестируем тип данных, возвращаемых из get_sort_list()."""
    result = get_sort_list('Яша, Саша, Маша, Даша')
    # Провальный тест:
    # ожидаем число, но вернётся список.
    assert isinstance(result, int)

