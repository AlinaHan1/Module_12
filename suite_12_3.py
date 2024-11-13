from runner2 import Runner, Tournament
import unittest
import module_12_2
import module_12_1

all_tests = unittest.TestSuite()
all_tests.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_1.RunnerTest))
all_tests.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_2.TournamentTest))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(all_tests)