import unittest
import volpiano

obtainGT = [
    "1---h--h--h---3",
    "1---h--h--h77---3",
    "1---h---gh--h--h---3",
    "1---g--g--g7---3",
    "1---g--g--g---3",
    "1---g--g--g7---3",
    "1---lmnml7---3",
    "1---d---e--f---3",
    "1---g---hij--hgf---3",
    "1---f--f--e---3",
    "1---e7---g--h7---3",
    "1---f--fe---g7---3",
    "1---e---g--h7---3",
    "1---h--h--h7---3",
    "1---ghg-gf---fg7---3",
    "1---e---g--h7---3",
    "1---j---l--m7---3",
    "1---e---g--h---3",
    "1---j---l--m7---3",
    "1---e---g--h777---3",
    "1---ffe---d--c---3",
    "1---f--g--gh--gf---3",
    "1---e---g--h7---3",
    "1---f--f--e---g7---3",
    "1---f--f--e7---3",
    "1---j--l--m7---3",
    "1---j---l--m7---3",
    "1---e---g--h7---3",
    "1---f--f--e7---3",
    "1---fgf---e--g7---3",
    "1---e---g--h7---3",
    "1---e---g--h7---3",
    "1---e---g--h7---3",
    "1---e---g--h7---3",
    "1---e---g--h7---3",
    "1---e---g--h7---3",
    "1---e---g--h7---3",
    "1---h---g--h7---3",
    "1---j---l--m7---3",
    "1---h---g--h---3",
    "1---e---g--h7---3",
    "1---e---g--h7---3",
    "1---e---g--h7---3",
    "1---e---g--h7---3",
    "1---e---g--h7---3",
    "1---e---g--h---3",
    "1---h--h--hghgf7---3",
    "1---g---h7---3",
    "1---h--h--h7---3",
]

validateFakeGT = [
    "---w-OB--4K--KB-kW-v",
    "-H--w---o-a-D-HFR-9-",
    "--4-E--Su-zc5--X-G-1",
    "-[uC-----D--kO-5----",
    "--e-pf]a----5E-5-6w-",
    "---Y--)--5v-(-W--Z-y",
    "1----au--2-----z,---",
    "-1---[------.----X--",
    "-U--0]O-qT--A-QVV--u",
    "WC-f-6---xO4-p,-----",
]


class TestVolpiano(unittest.TestCase):
    def test_volpiano_obtain(self):
        volpianos = volpiano.obtain(maxLength=20)
        self.assertEqual(set(volpianos), set(obtainGT))

    def test_volpiano_validate(self):
        pass

    def test_volpiano_compare(self):
        pass