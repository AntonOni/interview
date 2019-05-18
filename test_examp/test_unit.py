
st = "aaabbcdddda"


def zanogo(st):
    res = []
    n = 1
    res.append(st[0])
    for i in range(0, len(st)-1):
        if st[i] == st[i+1]:
            n += 1
        else:
            res.append(str(n))
            res.append(st[i+1])
            n = 1
    res.append(str(n))
    return "".join(res)



assert zanogo("aaabbcdddda") == "a3b2c1d4a1"
assert zanogo("aaabbcdd") != "a3b2c1d4a1"
assert isinstance(zanogo("aaabbcdddda"), str)
assert zanogo("aaabbcdddda") is not None
assert len(zanogo("aaabbcdddda")) % 2 == 0


import unittest


class TestZanogo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.fixt = "aaabbcdddda"
        cls.res = "a3b2c1d4a1"

    def setUp(self):
        print("Test started")

    def tearDown(self):
        print("Test finished")

    @classmethod
    def tearDownClass(cls):
        del cls.fixt
        del cls.res

    def test_equal(self):
        self.assertEqual(zanogo(self.fixt), self.res)

    def test_is_not_none(self):
        self.assertIsNotNone(zanogo(self.fixt))

    def test_is_res_str(self):
        self.assertIsInstance(zanogo(self.fixt), str)

    def test_not_equal(self):
        self.assertNotEqual(zanogo("rtyqrw"), self.res)


if __name__ == "__main__":
    unittest.main()

