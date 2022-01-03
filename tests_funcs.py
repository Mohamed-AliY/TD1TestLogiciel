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

    def test_ecartType(self):
        self.assertEqual(funcs.ecart_type([1,3,9,4]),2.947456530637899)
        self.assertEqual(funcs.ecart_type([1,1,1,1]),0)

    def test_estGeo(self):
        self.assertTrue(funcs.estGeo([1,2,4,8,16]))
        self.assertFalse(funcs.estGeo([4,2,6,2,9]))

    def test_estArith(self):
        self.assertTrue(funcs.estArith([3,6,9,12,15]))
        self.assertFalse(funcs.estArith([7,2,3,5,16]))
    
    def test_suiteGeo(self):
        _,val=funcs.suiteGeo(3,[1,2,4,8,16])
        self.assertEqual(val,[32,64,128])
    def test_suiteArith(self):
        _,val=funcs.suiteArith(3,[3,6,9,12,15])
        self.assertEqual(val,[18,21,24])
if __name__ == '__main__':
    unittest.main()