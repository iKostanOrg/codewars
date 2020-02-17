#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# FUNDAMENTALS STRINGS REGULAR EXPRESSIONS DECLARATIVE PROGRAMMING ADVANCED LANGUAGE FEATURES

import unittest
import allure
import pytest
from utils.log_func import print_log
from kyu_6.string_subpattern_recognition_3.has_subpattern import has_subpattern


@allure.epic('6 kyu')
@allure.parent_suite('Novice')
@allure.suite("Advanced Language Features")
@allure.sub_suite("Unit Tests")
@allure.feature("String")
@allure.story('String subpattern recognition III')
@allure.tag()
@allure.link(url='',
             name='Source/Kata')
@pytest.mark.skip(reason="The solution is not ready")
class HasSubpatternTestCase(unittest.TestCase):
    """
    Testing 'has_subpattern' function
    """

    def test_has_subpattern(self):
        """
        Verify that 'has_subpattern' function

        Return a subpattern with sorted characters,
        otherwise return the base string with sorted
        characters (you might consider this case as
        an edge case, with the subpattern being repeated
        only once and thus equalling the original input string).
        :return:
        """

        allure.dynamic.title("Testing 'has_subpattern' (part 3) function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html('<h3>Codewars badge:</h3>'
                                        '<img src="https://www.codewars.com/users/myFirstCode'
                                        '/badges/large">'
                                        '<h3>Test Description:</h3>'
                                        "<p></p>")

        with allure.step("Pass the string and verify the output"):
            data_set = [
                ("a", "a"),
                ("aaaa", "a"),
                ("abcd", "abcd"),
                ("babababababababa", "ab"),
                ("bbabbaaabbaaaabb", "ab"),
                ("123a123a123a", "123a"),
                ("123A123a123a", "111222333Aaa"),
                ("12aa13a21233", "123a"),
                ("12aa13a21233A", "111222333Aaaa"),
                ("abcdabcaccd", "aaabbccccdd"),
                ('49OTbVT2Hu8EFdYrbYhCQ2hCFpOwq3bpzVuopQ1O4QTTby83J5k'
                 'vbVHw1T4OpuQyK1bnXU8azTyqumEGvQaFb8nEHY35yr0dOy1b49'
                 'pApQXmUF8YIUkrboEI8ovHOYHVGKdgbH3odYAsgyhUr0vYsYJh',
                 '0112334458889ACEEFFGHHHIJKOOOQQQTTTUUVVXYYYYabbbbb'
                 'ddghhkmnoopppqrrsuuvvwyyyz'),
                ('mTcL4El8ONERf60xgTmZcywggRHxmLyTxEtly6RhOLsRfXsdy0c'
                 'iOXRtljgZYfX43ZE20gLRJfROmw3Yd08sLFyXcJ0R2ccRgHg3s2'
                 'xygcHYy3ih4Jclye9igFLeixhwYfT2EN4sEdLLsiLx4HXyE49Om'
                 'L3f6hyHwLETYe4MHXt2t2RLj0lcM2Mcs43J4f2004gicEEwjNLY'
                 'gEJE0T3Eh8LRL23RRdcyixH2FTwJgiOlgM34EXZJLfcg26lLLtg'
                 '6mtegHFymFE42hcFR2gi26JRFJ90jsM9xmEj3TZx24diRmhlgZH'
                 'gXHYjgdFxEdO2tetREe6EmL36y4fi42ORwYf4m8clET3ics2469'
                 'NgMm3OMgTLTLw0gjELcLcxt893H9s4NZZgef2Ys4iJcFtd2w9iw'
                 'Fmte9Ml433MhjEFx2e2gyJig6gMOLjXYf2HY6gHNT0YggNxMLLg'
                 'fiwc4Nt0406tiiH0wtgm0yLgg44J4NLZXYitg02Jh8Rdf80602X'
                 'FNi0NimsMYTcHxj8Xlgmxx4sYeLhdOMh440hfRcElgt0hgceZ2l'
                 'FTw2YMXcsw4NhJfgJgEfFH2F60EZ3geHc6y04Mt29l0cfRLiggi'
                 'LhedOs0wlXfgtR8fRY2RT4wdl4F93xHggXOEyyJ4xMRtc0gREiL'
                 'ZMsE2L0MeMwTRTRlNYFTH3iJtmlyjg0gOO2jc2Ei204w2iidFLZ'
                 'sXHLX4j6iEeic6i0RZc0ix4wLcdds2JgRZgNOYh2Emg08XdlgNl'
                 'iMN0EH0JLFigcelmgOcN6jEeiLjR9688Fcjw0fd9EZ9ER8899E8'
                 'EEiJYhmJf99TZZZLLM0dTgxEZcmTlNXJH494sO2i6cOiYYg9thN'
                 'Rg3iXRijggiYRdhjdcc9c60cgiyje32wOLRLd89dFsg40eRRd4F'
                 'yte9H0c8hOcsjLNyX0wMcch8L228E4e0i4Xf3cgRZmZj08j8ggg'
                 'xsX0gNRs24OLRwEE2lOM3hL0TZEEFh2c4i0N68xRR4iRTe2m2tj'
                 'N48JeERERix6gyg',
                 '0022344689EEFHJLLMNORRTXYZccdefggghiijlmstwxy'),
                ('sZZpCWRNzSfvfZy5CMsRbdHeb85L3DmMB7dLMIM33pylSW6hHXp'
                 'dthSmvynxF7cSUtSVShx8vwSYaa7dg4jyCzHzJqnYHRGD0sTg5z'
                 'XOB42f9fuo47NhwV7fVZkzCyIfVzUvb90M5FOx3xXPo3fqFOqZk'
                 'rH5HZ59juv3SWPIJKG7VfWh1R6O3S42by54D0W5rHYtxTjLsP3I'
                 'PkR5WhsFNbYXMZwfIfcovPKfWzqD0ZTDWDdfMLkTyncVL3fODk9'
                 '5V3Jz6p0jRsCv8ahOky6BLgffzBfb9SMnq3spM8q9wVZbaLWPVk'
                 'ywWNypYC3MnCyQKxVd6Mvo1fq2I26uajR5aXMrrKX4MdyhfQfza'
                 'rK5Pm2nb8IMs8zgNKMDrwKfcD553Os8OZs5eHYyn415Zvy0RCd3'
                 'FyjFa3DGJs7IhSqnlvVJZYaKiFV45dtxkMsh2m5C2vvz2fyt24C'
                 'raMULMxJwjYMuGM7Cz65hdWJaNcWCjyguWMqrdMO02Nf8RInK7G'
                 'MVf2CWrR4RXiSv6yD29XBhIOkT5Cm7TfX8ZFk5FP4sKcWqHZGst'
                 'DdM0ZHkyNFjQWJZCFQe5h5rguha8COIZVdcH7x4oMRRWXJwTn5o'
                 'zzR8jYS54fFSwfoCgMkxXBhSjMWyk3PWnRW3vvkYW39vSjMo4bz'
                 'jdJD1Dq1j3gs5WavPxNfjC0j63Ca6pHt44D5MFCgXaC1rz346wH'
                 'ldbf89huLqOXg4WqByOW9SR8xXng9xC4CajsOC5HS2jzYuMdUXv'
                 'jPZuIfgusZDZbReZCJ2fn4mapgL6z0FS94S3HuMwIGwnyyafxQ8'
                 '84Y0T6kFFMcCknMcZ4uxowP7jzyWNO6SdPxZLZNqYC2roWSZxGN'
                 'rFKwzfVPZOxPyzzktkW8fQyyv9zCSzgbd3kCvzYFxmrR5CMLiq8'
                 'xz8cxWDCYWPN1WLNYsngLrCcdop0XDDgQXfXpZyRV56lZsRLZoa'
                 '6WfCap9B3wNx2k4Z1Cwr5NL8IMCpWmKSsxiQ9MHZ9c5fC8dZJFz'
                 'DxXXqIFI',
                 '000112222333333444444555555556666777888889999BBCCCC'
                 'CCCCCDDDDDFFFFFGGHHHHIIIIJJJKKKLLLLMMMMMMMMMNNNNOOO'
                 'OPPPPQQRRRRRSSSSSSTTUVVVVWWWWWWWWXXXXXYYYYZZZZZZZZa'
                 'aaaabbbcccdddddefffffffffgggghhhhijjjjjkkkkklmmnnnn'
                 'ooopppqqqqrrrrsssssttuuuvvvvvwwwwxxxxxxyyyyyyyzzzzzzz'),
                ('lcGPumgkSKgXDCAOuYEFfE2oDFCRrMzGoYupyfrDA3UxGGgnlix'
                 'KobXYNrRlMRIYnq1imYuIyoIrakSmCKq7XDRcDWcmXPuRl67MGi'
                 'q2g8CJUu0hfuXomi1OGUMIu6mpuJXfUPDzv7q0zN8zhlxoc7arm'
                 'RmuxvfP3WrfbrrKlY',
                 '01236778ACCDDDEFGGGIIJKKMMNOPPRRRSUUWXXXYYYabccfffgg'
                 'hiiklllmmmmnooopqqrrrruuuuuvxxyzz')
            ]

            for data in data_set:
                print_log(string=data[0], expected=data[1])
                self.assertEqual(data[1], has_subpattern(data[0]))
