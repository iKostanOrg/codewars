"""
Test for 'Most frequently used words in a text'

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# ALGORITHMS STRINGS PARSING RANKING FILTERING

import unittest
import allure
from utils.log_func import print_log
from kyu_4.most_frequently_used_words.solution import top_3_words


@allure.epic('4 kyu')
@allure.parent_suite('Competent')
@allure.suite("Algorithms")
@allure.sub_suite("Unit Tests")
@allure.feature("String")
@allure.story('Most frequently used words in a text')
@allure.tag('ALGORITHMS',
            'STRINGS',
            'PARSING',
            'RANKING',
            'FILTERING')
@allure.link(
    url='https://www.codewars.com/kata/51e056fe544cf36c410000fb/train/python',
    name='Source/Kata')
class Top3WordsTestCase(unittest.TestCase):
    """
    Testing top_3_words
    """

    def test_top_3_words(self):
        """
        Test top_3_words function
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title("Testing top_3_words function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>Given a string of text (possibly with punctuation and line-breaks), "
            "the function should return an array of the top-3 most occurring words, "
            "in descending order of the number of occurrences.</p>")
        # pylint: disable-msg=R0801
        test_data = (
            ("a a a  b  c c  d d d d  e e e e e", ["e", "d", "a"]),
            ("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e", ["e", "ddd", "aa"]),
            ("  //wont won't won't ", ["won't", "wont"]),
            ("  , e   .. ", ["e"]),
            ("  ...  ", []),
            ("  '  ", []),
            ("  '''  ", []),
            ('AqyWZhe /ubx,,/!VCDeGux,uYVx -/-;CUQhpOptV/xoiIHRwI-!-xoiIHRwI!CUQhpOptV /;'
             'aqNSrVD--//VCDeGux_!AqyWZhe? uYVx,-/:ubx?aqNSrVD_.PVDdpw,;!AqyWZhe/aqNSrVD_A'
             'nZnlq:/ubx_!-wWHf;:,rKlP/VCDeGux; !_:xoiIHRwI;-AqyWZhe !KdAFZ!:;;PVDdpw!_.;x'
             'oiIHRwI!KdAFZ/??!QsF_?/?!PVDdpw;.-_-aqNSrVD:?uYVx._AnZnlq-,,wWHf; ;AqyWZhe ? '
             '_,uYVx_uYVx?KdAFZ?AqyWZhe:?;/rKlP.aqNSrVD,!-/QsF/??uYVx.PVDdpw . ._xoiIHRwI/?'
             '/;!GLU-? aqNSrVD/. ?aqNSrVD.?AqyWZhe !FdalHwCCUr wWHf_:-?rKlP,.?/ PVDdpw?!Fda'
             'lHwCCUr.!wWHf :QsF?KdAFZ-::::AnZnlq_QsF/.qyd,/VCDeGux:_;wWHf.!/uYVx!;KdAFZ??_'
             ':?QsF:,AqyWZhe:::;ubx: ?QsF;;KdAFZ;; _-ubx./_;,rKlP? :?_CUQhpOptV/-KdAFZ?:uYV'
             'x??.ecMq\'CMuEx_ecMq\'CMuEx;,-/ qyd., CUQhpOptV:::wWHf-__QsF:/-.VCDeGux?/:-uY'
             'Vx-_,-QsF;xoiIHRwI;._AqyWZhe-;-.VCDeGux.aqNSrVD/.AqyWZhe;aqNSrVD:KdAFZ-; .Aqy'
             'WZhe!/_;?KdAFZ;;/,KdAFZ-GLU,,.KdAFZ!AqyWZhe//?-rKlP/ ://QsF.!!QsF!;:,ubx:/-?P'
             'VDdpw?!AqyWZhe,;!?/xoiIHRwI..  ubx:aqNSrVD/,_:.AnZnlq /_;xoiIHRwI.- .aqNSrVD-'
             '  , ubx_-?VCDeGux;:rKlP;VCDeGux ?.AnZnlq,PVDdpw-., KdAFZ_QsF/QsF_; uYVx_?;?wW'
             'Hf/-,;/GLU_;rKlP -_,wWHf?:QsF!!_rKlP-;aqNSrVD  ? KdAFZ?::. AqyWZhe_AnZnlq, ub'
             'x,? !GLU_:aqNSrVD.!;AqyWZhe_?,uYVx-CUQhpOptV/..AnZnlq;QsF?rKlP!QsF,_!AnZnlq!-'
             '/,uYVx.uYVx ?uYVx-ubx,.,_FdalHwCCUr !/QsF.AqyWZhe./:_KdAFZ ,KdAFZ._ _ ubx?CUQ'
             'hpOptV :.KdAFZ;!;:,KdAFZ,_!-?PVDdpw.!CUQhpOptV;.;;KdAFZ,,-VCDeGux_-,ubx ;uYVx'
             ':;! :VCDeGux/.;_uYVx.!FdalHwCCUr!:,uYVx:!;_uYVx:!CUQhpOptV?!.KdAFZ!-:-uYVx_?w'
             'WHf:uYVx.?-.:rKlP?.VCDeGux:?:?uYVx:wWHf?,AnZnlq::FdalHwCCUr.-,_,VCDeGux.;rKlP'
             ',rKlP. VCDeGux,/_aqNSrVD? AqyWZhe.. /:AqyWZhe_.CUQhpOptV ?;- AqyWZhe! ;/qyd !'
             ',:AqyWZhe:!?.CUQhpOptV / _uYVx-_:!CUQhpOptV_/AqyWZhe;VCDeGux__?PVDdpw.,_?,VCD'
             'eGux wWHf;,_PVDdpw;,-!?AqyWZhe,??AqyWZhe:?/!VCDeGux :;.KdAFZ ?/GLU- AqyWZhe,_'
             '?_:FdalHwCCUr.:AqyWZhe. ,,xoiIHRwI;;.;AnZnlq;!;aqNSrVD:.;_/ubx;-,qyd ?uYVx qy'
             'd-;wWHf ;! VCDeGux -rKlP:! KdAFZ/??.?rKlP,//:VCDeGux!,ecMq\'CMuEx:VCDeGux.QsF'
             '_VCDeGux;?-aqNSrVD,.- uYVx?:KdAFZ;VCDeGux.wWHf_:-/QsF!_.VCDeGux. xoiIHRwI,-An'
             'Znlq/aqNSrVD!? -AnZnlq_!qyd _?,.FdalHwCCUr!?!wWHf- ;:rKlP--:AqyWZhe -:/wWHf-K'
             'dAFZ_!?;VCDeGux:_?/qyd:uYVx;;FdalHwCCUr .! uYVx?;.,rKlP,AqyWZhe?-!,AnZnlq! ?V'
             'CDeGux, ;,aqNSrVD;/::/QsF__.QsF!rKlP?.;AqyWZhe;-?uYVx/_rKlP::ubx!!_PVDdpw._/,'
             'AnZnlq!/?. rKlP.;rKlP-,,/:CUQhpOptV; ubx;:-;KdAFZ:AqyWZhe/_GLU!!/PVDdpw,_QsF '
             '_ _QsF!;/CUQhpOptV ;-,PVDdpw?aqNSrVD_;?,AqyWZhe;.CUQhpOptV_;!-aqNSrVD!KdAFZ;!'
             'KdAFZ/KdAFZ-!_.:aqNSrVD._;VCDeGux_!QsF PVDdpw_,KdAFZ/ ;_/CUQhpOptV;.PVDdpw?/ '
             ',rKlP:,uYVx? _-QsF-.VCDeGux-;;.wWHf,- QsF_rKlP:?.,/PVDdpw!,VCDeGux-:wWHf __;Q'
             'sF,_.QsF:VCDeGux:',
             ['aqywzhe', 'vcdegux', 'uyvx'])
        )

        for text, expected in test_data:
            actual_result: list = top_3_words(text)
            with allure.step("Enter a test string and verify the output"):
                print_log(text=text,
                          expected=expected,
                          result=actual_result)

                self.assertListEqual(expected, actual_result)
