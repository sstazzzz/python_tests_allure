import allure
import pytest


@pytest.mark.parametrize('first_value, second_value', [("453543543545343", "111111111111111111")])
def test_fail_check(first_value, second_value):
    """this test fails"""
    assert first_value == second_value


@pytest.mark.parametrize('first_value, second_value', [("gfdgfdgfdgfdgdfg", "aaaaaaaaaaafffffffff")])
def test_fail_checking(first_value, second_value):
    """this test fails"""
    assert first_value == second_value


@pytest.mark.parametrize('first_value, second_value', [("gfdgfdgfdgfdgdfg", "aaaaaaaaaaafffffffff")])
def test_fail_attach(first_value, second_value):
    """this test fails and attach"""
    allure.attach('Текстовые логи', 'Логи Error 500', allure.attachment_type.TEXT)
    allure.attach.file('./Screenshot_fail.jpg', attachment_type=allure.attachment_type.JPG)
    assert first_value == second_value
