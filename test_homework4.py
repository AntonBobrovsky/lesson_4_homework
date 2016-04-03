from unittest import TestCase
from homework4 import LionStates
import unittest


class LionStatesTest(TestCase):
    # Тест на перехват ошибки, при передаче конструктору некорректного значения
    def test_args(self):
        self.assertRaises(ValueError, LionStates, "asds2gda")
        self.assertRaises(ValueError, LionStates, "блаблабла")

    # Тесты на корректность поведения льва в зависимости от входных данных
    def test_LionStates(self):
        # набор тестовых символов
        symbols_set = ["антилопа", "охотник", "дерево"]

        # проверки, если лев "родился" сытым
        lion = LionStates("сытый")
        lion.implementation_fsm(symbols_set[0])
        self.assertEqual("голодный", lion.state, "wrong state, should be 'голодный'!")
        self.assertEqual("спать", lion.action, "wrong action, should be 'спать'!")
        lion.implementation_fsm(symbols_set[1])
        self.assertEqual("голодный", lion.state, "wrong state, should be 'голодный'!")
        self.assertEqual("убежать", lion.action, "wrong action, should be 'убежать'!")
        lion.implementation_fsm(symbols_set[2])
        self.assertEqual("голодный", lion.state, "wrong state, should be 'голодный'!")
        self.assertEqual("смотреть", lion.action, "wrong action, should be 'смотреть'!")

        # проверки, если лев "родился" голодным
        lion = LionStates("голодный")
        lion.implementation_fsm(symbols_set[0])
        self.assertEqual("сытый", lion.state, "wrong state, should be 'сытый'!")
        self.assertEqual("съесть", lion.action, "wrong action, should be 'съесть'!")
        lion.implementation_fsm(symbols_set[1])
        self.assertEqual("голодный", lion.state, "wrong state, should be 'голодный'!")
        self.assertEqual("убежать", lion.action, "wrong action, should be 'убежать'!")
        lion.implementation_fsm(symbols_set[2])
        self.assertEqual("голодный", lion.state, "wrong state, should be 'голодный'!")
        self.assertEqual("спать", lion.action, "wrong action, should be 'спать'!")

if __name__ == '__main__':
    unittest.main()
