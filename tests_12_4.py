import logging
import unittest
from runner3 import Runner

logging.basicConfig(level=logging.INFO,
                    filemode='w',
                    encoding='utf-8',
                    filename='runner_tests.log',
                    format='%(asctime)s | %(levelname)s |%(message)s')


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            run = Runner('Вася', -10)
            for _ in range(10):
                run.walk()
            self.assertEqual(run.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    def test_run(self):
        try:
            run = Runner(5, 5)
            for _ in range(10):
                run.run()
            self.assertEqual(run.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning('Не верный тип данных для объекта Runner', exc_info=True)

    def test_challenge(self):
        pass


if __name__ == '__main__':
    unittest.main()
