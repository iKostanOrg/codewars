"""
Solution for -> String transformer.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# FUNDAMENTALS

import unittest
import allure
from parameterized import parameterized
from utils.log_func import print_log
from kyu_6.string_transformer.string_transformer \
    import string_transformer


@allure.epic('6 kyu')
@allure.parent_suite('Novice')
@allure.suite("Data Structures")
@allure.sub_suite("Unit Tests")
@allure.feature("String")
@allure.story('String transformer')
@allure.tag('FUNDAMENTALS')
@allure.link(
    url='https://www.codewars.com/kata/5878520d52628a092f0002d0',
    name='Source/Kata')
class StringTransformerTestCase(unittest.TestCase):
    """Testing string_transformer function."""

    @parameterized.expand([
        ("Example string", "STRING eXAMPLE"),
        ("Example Input", "iNPUT eXAMPLE"),
        ("To be OR not to be That is the Question",
         "qUESTION THE IS tHAT BE TO NOT or BE tO"),
        ("", ""),
        ("You Know When  THAT  Hotline Bling",
         "bLING hOTLINE  that  wHEN kNOW yOU"),
        (" A b C d E f G ", " g F e D c B a "),
        ("Alc   Rl VLEE      k xLU c c",
         "C C Xlu K      vlee rL   aLC"),
        ("J VVmviAdpIAFzh zs oMHsx  HPvN  xt sN PlW u K Q \
XnV mR  Betg  ox E   j cIiQ  Fa GJdk  ECYzH  BkuU ",
         " bKUu  ecyZh  gjDK fA  CiIq J   e OX  bETG  Mr \
xNv q k U pLw Sn XT  hpVn  OmhSX ZS vvMVIaDPiafZH j"),
        ("LXOP QmsZs R   i jUor SWDkkhh P  X Q H vz  gD \
KSpv hGCOSB  e e r piw pXB OqkIbb ",
         " oQKiBB Pxb PIW R E E  Hgcosb ksPV Gd  VZ h q \
x  p swdKKHH JuOR I   r qMSzS lxop"),
        ("V Ots Ev k Q bC  jK Db cezl YdmzzYbK iu   JdJu P  \
qeAwqZYewoHk YnGdGQa LoDorPaUom cSJo s",
         "S CsjO lOdORpAuOM yNgDgqA QEaWQzyEWOhK  p jDjU   \
IU yDMZZyBk CEZL dB Jk  Bc q K eV oTS v"),
        ("KYjBc SgkXrFIDq  MYv XAEzh RX fkSPCF tMtYN ewyhq \
EFSgia  DUH u vXizIYb u oZ OMw YjaqzJ  BJGjfOc  s",
         "S  bjgJFoC  yJAQZj omW Oz U VxIZiyB U duh  efsGIA \
EWYHQ TmTyn FKspcf rx xaeZH myV  sGKxRfidQ kyJbC"),
        ("ncE  ZpQ O y  A  fBNbw R v rCg n yhpvx BMn tk \
ubCZrHJl   GiEyCjZcRk   kheNwWj PA ZAGpsZamNHb",
         "zagPSzAMnhB pa KHEnWwJ   gIeYcJzCrK   UBczRhjL TK \
bmN YHPVX N RcG V r FbnBW  a  Y o zPq  NCe"),
        ("UOtfi  erH kCk KXzg Io  Y  I TYAf \
EGXVSvASIyJ p Zf p kV g RI  V",
         "v  ri G Kv P zF P egxvsVasiYj tyaF \
i  y  iO kxZG KcK ERh  uoTFI")])
    def test_string_transformer(self, s, expected):
        """
        Testing string_transformer function with multiple test data.

        Given a string, return a new string that has
        transformed based on the input:

        1. Change case of every character, ie. lower
        case to upper case, upper case to lower case.

        2. Reverse the order of words from the input.
        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title("Testing string_transformer function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p></p>")
        # pylint: enable-msg=R0801
        with allure.step(f"Enter test string: {s} "
                         f"and verify the output: {expected}."):
            print_log(s=s, expected=expected)
            self.assertEqual(expected, string_transformer(s))
