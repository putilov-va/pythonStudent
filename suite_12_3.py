import unittest
import tests_12_1
import tests_12_2
import tests_12_3
# check_test
testTS =unittest.TestSuite()

                    #  TextTestRunner для остановки тестовой среды / loadTestsFromTestCase(путь к файлу))
testTS.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
testTS.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

result_tests = unittest.TextTestRunner(verbosity=2)
result_tests.run(testTS)