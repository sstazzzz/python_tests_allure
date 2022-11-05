import allure
import pytest


@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize('first_value, second_value', [('order', 'order')])
def test_good_check_regress(first_value, second_value):
    assert first_value == second_value


@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize('first_value, second_value', [('order/api', 'order/api')])
def test_good_checking_api_regress(first_value, second_value):
    assert first_value == second_value


@pytest.mark.skip('TASK-555456 Error 500')
@pytest.mark.parametrize('first_value, second_value', [('order/api', 'order/api')])
def test_good_checking_api_critical(first_value, second_value):
    assert first_value == second_value


@pytest.mark.parametrize('first_value, second_value', [('login', 'login')])
def test_good_checking_create_order_regress(first_value, second_value):
    """Оформление заказа"""
    with allure.step('Авторизация'):
        assert first_value == second_value

    with allure.step('Создание заказа'):
        assert True

    with allure.step('Добавление товара'):
        assert True

    with allure.step('Оформление заказа'):
        assert True







