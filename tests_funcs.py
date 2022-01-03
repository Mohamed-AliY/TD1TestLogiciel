import funcs
import unittest

class TestFuncs(unittest.TestCase):

    def test_min_int(self):
        self.assertEqual(funcs.min_int(0,2),0)
        self.assertEqual(funcs.min_int(-1,-5),-5)
        self.assertEqual(funcs.min_int(-1,2),-1)
        self.assertEqual(funcs.min_int(0,0),0)



    def test_mediane(self):
        self.assertEqual(funcs.mediane([0,1,2,3]),1.5)
        self.assertEqual(funcs.mediane([8,15,20,4,11]),11)
        # self.assertEqual(funcs.mediane())

if __name__ == '__main__':
    unittest.main()