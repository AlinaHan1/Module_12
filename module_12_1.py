import runner
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        run = runner.Runner(name='Bob')
        for _ in range(10):
            run.walk()
        self.assertEqual(run.distance, 50)

    def test_run(self):
        run = runner.Runner(name='Sam')
        for _ in range(10):
            run.run()
        self.assertEqual(run.distance, 100)

    def test_challenge(self):
        run_1 = runner.Runner(name='Bob')
        run_2 = runner.Runner(name='Sam')
        for _ in range(10):
            run_1.walk()
            run_2.run()
        self.assertNotEqual(run_1.distance, run_2.distance)


if __name__ == '__main__':
    unittest.main()
