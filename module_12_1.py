import runner2
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = False
    # Если @unittest.skipUnless(is_frozen == False, тест не проходит. is_frozen == True, тест проходит)

    @unittest.skipUnless(True, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        run = runner2.Runner(name='Bob')
        for _ in range(10):
            run.walk()
        self.assertEqual(run.distance, 50)

    @unittest.skipUnless(True, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        run = runner2.Runner(name='Sam')
        for _ in range(10):
            run.run()
        self.assertEqual(run.distance, 100)

    @unittest.skipUnless(True, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        run_1 = runner2.Runner(name='Bob')
        run_2 = runner2.Runner(name='Sam')
        for _ in range(10):
            run_1.walk()
            run_2.run()
        self.assertNotEqual(run_1.distance, run_2.distance)


if __name__ == '__main__':
    unittest.main()
