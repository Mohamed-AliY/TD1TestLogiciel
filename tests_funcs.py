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
        self.assertIsNone(funcs.mediane([]))

    def test_moyenne(self):
        self.assertEqual(funcs.moyenne([0,1,2,3]),1.5)
        self.assertEqual(funcs.moyenne([8,15,20,4,11]),11.6)
        self.assertEqual(funcs.moyenne([5,5,5,5,5]),5)

    def test_moyenne(self):
        self.assertEqual(funcs.ecart_type([1,3,9,4]),2.947456530637899)
        self.assertEqual(funcs.ecart_type([1,1,1,1]),0)

if __name__ == '__main__':
    unittest.main()