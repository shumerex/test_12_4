from rt_with_exceptions import Runner
import unittest
import logging

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            runner = Runner(name="Алиса", speed=-10)
            for _ in range(10):
                runner.walk()
            self.assertEqual(runner.distance, 50)
        except ValueError:
            logging.warning("Неверная скорость для Runner", exc_info=True)
        else:
            logging.info('"test_walk" выполнен успешно')



    def test_run(self):
        try:
            runner = Runner(name=123, speed=10)
            for _ in range(10):
                runner.run()
            self.assertEqual(runner.distance, 100)
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)
        else:
            logging.info('"test_run" выполнен успешно')


    def test_challenge(self):
        runner1 = Runner("Михаил")
        runner2 = Runner("Алексей")
        for _ in range(10):
            runner1.walk()
            runner2.run()
        self.assertNotEqual(runner1.distance, runner2.distance)


if __name__ == '__main__':
    unittest.main()
logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='utf-8',
                    format="%(asctime)s | %(levelname)s | %(message)s")

