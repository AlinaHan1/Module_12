from runner2 import Runner, Tournament
import unittest


class TournamentTest(unittest.TestCase):
    is_frozen = True
    # @unittest.skipIf(is_frozen == True, тест не проходит. is_frozen == False, тест проходит)

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.run_1 = Runner('Усейн', 10)
        self.run_2 = Runner('Андрей', 9)
        self.run_3 = Runner('Ник', 3)

    @unittest.skipIf(True, 'Тесты в этом кейсе заморожены')
    def test_1(self):
        tournament1 = Tournament(90, self.run_1, self.run_3)
        result = tournament1.start()
        TournamentTest.all_results.append(result)
        self.assertTrue(result[2] == 'Ник')

    @unittest.skipIf(True, 'Тесты в этом кейсе заморожены')
    def test_2(self):
        tournament2 = Tournament(90, self.run_2, self.run_3)
        result = tournament2.start()
        TournamentTest.all_results.append(result)
        self.assertTrue(result[2] == 'Ник')

    @unittest.skipIf(True, 'Тесты в этом кейсе заморожены')
    def test_3(self):
        tournament3 = Tournament(90, self.run_1, self.run_2, self.run_3)
        result = tournament3.start()
        TournamentTest.all_results.append(result)
        self.assertTrue(result[3] == 'Ник')

    @classmethod
    def tearDownClass(cls):
        for i, elem in enumerate(cls.all_results):
            print(f'{i + 1}, {elem}')


if __name__ == '__main__':
    unittest.main()
