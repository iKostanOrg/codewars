"""
Test for -> String subpattern recognition I
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# FUNDAMENTALS STRINGS REGULAR EXPRESSIONS
# DECLARATIVE PROGRAMMING ADVANCED LANGUAGE FEATURES

import unittest
import allure
from utils.log_func import print_log
from kyu_6.string_subpattern_recognition_1.has_subpattern import has_subpattern


# pylint: disable-msg=R0801
@allure.epic('6 kyu')
@allure.parent_suite('Novice')
@allure.suite("Advanced Language Features")
@allure.sub_suite("Unit Tests")
@allure.feature("String")
@allure.story('String subpattern recognition I')
@allure.tag('FUNDAMENTALS',
            'STRINGS',
            'REGULAR EXPRESSIONS',
            'DECLARATIVE PROGRAMMING',
            'ADVANCED LANGUAGE FEATURES')
@allure.link(
    url='https://www.codewars.com/kata/5a49f074b3bfa89b4c00002b',
    name='Source/Kata')
# pylint: enable-msg=R0801
class HasSubpatternTestCase(unittest.TestCase):
    """
    String subpattern recognition I
    Testing 'has_subpattern' function
    """
    def test_has_subpattern(self):
        """
        String subpattern recognition I

        Verify that 'has_subpattern' function to returns
        either true/True or false/False if a string can be
        seen as the repetition of a simpler/shorter subpattern or not.
        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title("Testing 'has_subpattern' (part 1) function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p></p>")

        with allure.step("Pass the string and verify the output"):
            # pylint: disable-msg=R0801
            test_data = [
                ("a", False),
                ("aaaa", True),
                ("abcd", False),
                ("abababab", True),
                ("ababababa", False),
                ("123a123a123a", True),
                ("123A123a123a", False),
                ("abbaabbaabba", True),
                ("abbabbabba", False),
                ("abcdabcabcd", False),
                ('cV', False),
                ('MTvRAG70pTMgx7jn5sEZEEMnOOnwUpBFz8VCr4GXExSMo9EpLclhTIZ',
                 False),
                ('0DbTh4mlN0DbTh4mlN0DbTh4mlN0DbTh4mlN0DbTh4mlN0DbTh4mlN0'
                 'DbTh4mlN0DbTh4mlN0DbTh4mlN0DbTh4mlN0DbTh4mlN0DbTh4mlN0D'
                 'bTh4mlN0DbTh4mlN0DbTh4mlN0DbTh4mlN0DbTh4mlN0DbTh4mlN0Db'
                 'Th4mlN0DbTh4mlN0DbTh4mlN0DbTh4mlN0DbTh4mlN0DbTh4mlN0DbTh'
                 '4mlN0DbTh4mlN0DbTh4mlN0DbTh4mlN0DbTh4mlN0DbTh4mlN0DbTh4m'
                 'lN0DbTh4mlN0DbTh4mlN0DbTh4mlN0DbTh4mlN0DbTh4mlN0DbTh4mlN'
                 '0DbTh4mlN0DbTh4mlN0DbTh4mlN0DbTh4mlN0DbTh4mlN0DbTh4mlN0Db'
                 'Th4mlN0DbTh4mlN0DbTh4mlN0DbTh4mlN0DbTh4mlN0DbTh4mlN0DbTh4'
                 'mlN0DbTh4mlN0DbTh4mlN0DbTh4mlN0DbTh4mlN0DbTh4mlN0DbTh4mlN'
                 '0DbTh4mlN0DbTh4mlN0DbTh4mlN0DbTh4mlN0DbTh4mlN0DbTh4mlN0Db'
                 'Th4mlN0DbTh4mlN0DbTh4mlN0DbTh4mlN0DbTh4mlN0DbTh4mlN0DbTh4'
                 'mlN0DbTh4mlN0DbTh4mlN0DbTh4mlN0DbTh4mlN0DbTh4mlN0DbTh4mlN'
                 '0DbTh4mlN0DbTh4mlN0DbTh4mlN0DbTh4mlN0DbTh4mlN0DbTh4mlN0Db'
                 'Th4mlN0DbTh4mlN0DbTh4mlN0DbTh4mlN0DbTh4mlN0DbTh4mlN0DbTh4m'
                 'lN0DbTh4mlN0DbTh4mlN0DbTh4mlN0DbTh4mlN0DbTh4mlN0DbTh4mlN0D'
                 'bTh4mlN0DbTh4mlN0DbTh4mlN0DbTh4mlN0DbTh4mlN0DbTh4mlN0DbTh4'
                 'mlN0DbTh4mlN0DbTh4mlN0DbTh4mlN0DbTh4mlN0DbTh4mlN0DbTh4mlN0'
                 'DbTh4mlN0DbTh4mlN0DbTh4mlN0DbTh4mlN0DbTh4mlN', True),
                ('qMUU2ABUJQL2J42vnX3PeW1uiRs7clCKYDqKIyLLvTRuTP6WncLOA5y4yz'
                 'iCF8XbADPCcO8FfoFEOhRiiCEEvIVLHqwe0fer3A8jNjF48TGr3Tl1sAGw'
                 'q5RCqbPerl0afYeM3N7mhYq8FqFIFuJL9Y1IeQK3RyR2jcxhHfTxSsLxDJ'
                 'Bpx4N6T9uXfNbxQZbzrS3j4qvBP6gzpbK12l6hi1WzPMTQn25iiXoXGO49'
                 'G2JzdimO1ABBiBf0w3iMcHE5CZDIp3qZlSH8Cq5egMjFTXyuY3gV9WmGow5'
                 'oVHz2b7vlKKBS1TJWkLW2S4Ld2GejWlEAt1XHuNCFzUpSWAbL9kAM3V0FSq'
                 'GomF6RkEFzMZcf9B9B9mqdJxjJF1GKQ6kwTUu0D110Shn3VmTAC17sjujDwK'
                 'xdpbPcXpDMZKem5aIaagtBLDtKt0IIBkAShwcUGNbnh6SjjH18GgLpUcCuXJ'
                 'REIXk2YeZOj7UE6KEGP3DcS0UYCG6XqerdCDd6oXgN3tjEjD6SqUeGtF0AGp'
                 '3Lbw7ZDsQOHFOehRujRxtO4La4vBN5nleeZgF6lTt8OeG5CQb2OpdCG8jYJXl'
                 'NhjUlFqj4fllqPEIwMgXunYNdOal691fCbsxoIuPwENV86QgXp9uKgs21BIxw'
                 '07QXp7vuBrOcx0dcifjm0P6n37o520GPJ9kAqRVPdhqL6UAk4YgqRVmXdLImv'
                 'v6mEjZnisZx3zZQtTFC6aQh0Geiwzefgj86yGhyf4oI6rCTV7RHhEgQYDotJ06'
                 'eucONYYCbg50Rpyzwy9okYvQo513gDYaQU7ElHPQ4Nvu8yaYjHznGkIFkwnYt0'
                 '6o5I5FM3fbxT6NCRaSbRyqYgX565LhoLfHrd06xtMvBOaLJjynmXlf51WFduFP'
                 'GHVcQ3bCpAffEJ8kPL7EOmMdW1f6WVI8y9AjM8LrCmqUahYXSnVcp5iuZim4gx'
                 '6duH84cELZzkXjHA1RZD9wmY7RTTfZQJk9a0x5CjGH3oOAegBLeQpkNnNhIz93f'
                 'JJlDfobtrcMAzjM1TM1AmZkDZuGxFohPbpL9Qlxj436zCDCjcPZQhGM0SRpJ1Vu'
                 'UJcHLKJ5mbJFkNhkecplvKzCL4XT4bHhsc2aZtISvOTaPdAtiyz5z3gGI31vWJU'
                 '3HCbThBer68W5YXwqZhp94KEfCeLU43OWflINWWjgysiRdLgO8mCmDzXW9f6quS'
                 'J9rVXLpsBqs1QAgCDiVYmPtduDzduqZJnfxMMMkxPn82WK4zqFGS5b3wGKRutni8'
                 'UVI0Fo8OwBQMc8VrFtIT2PR679lToWsWQCKKOX5KrvkkiLtd3QjBinHHz9tnExru'
                 '2h0W51GADIQPWkgtRl50vmcbloWN6HiBeRSlvnkzC9Nqih6otMY12QbSy0QrPtPj'
                 'DYz8s8ZRvStQiHNvssWsqJL2zvM72pDy8cwDCAtCIxqKtgEJitiUfv3KhJaQLDd9'
                 'GJ9dLKZz69ivONPwvnikMOLGGQBGhvCV0RIfPywRxYFRkmTlg7mri3WdVMmewhiE'
                 'ZaCs4k0DiOvgJ8DDcH2TSwGVFvuRRdMtl3i1c7SgtLX0sObIW70JMl8Ca6prx5hR6'
                 'ud3Hiuf3T363lRTCjQ9wv8NIYc3BK81cOvZKa5JMF3KCw57YeIfYMQQdngYScEA9n'
                 'NPueMBh8DBUgIX30ojCOMNAfyCkZx3pEiGjEyInJmjWHwpIK0kqyd5YnixP4XYY3EI'
                 'Dk8MN5nO01V2cjBamcFBdlpobrx5ZCVeCQG11aJW0TJXxNMY1f7UNiTM8IRZWF26W1'
                 'SXPpLqfukoBIiEZgEUeHwTNy4CweMuR0V5coT3YWQwSz9HYlSUzZefkthKwnD3sjGfn'
                 '0L3o2Jjq8gl1FCpZhO8AtRLQsxAJtcKCRetmiJNuKMkMEE86YMxVSCafeUrItds2n5f'
                 'SDZLWJZ0NNWKkM7WGoFFHb3KDLd6NGBapeRc1VuGn9CiX8OtWPoDyNNwRgi3l1x79ip'
                 'ihmMjaUlmDKlur7cHCtwC3jbt9AbljLFrltWGa6tvcFqvzFh5cpRUpTXteyw5laifqtz'
                 'rmcWsQwB0pyCNM9v326aCGPieg5mvgxJm3lHzfFdiWysWcrF83PgkAamv1nadzM8pBLP'
                 'cc9WyGcTTg2ObwMcyWvFW2gj3ipD4opAzZAUal6ctMMOn5bbfmLkjPF9tyTtuLNLniuH'
                 '03yJJI5gzapVkhIp2RSBBRis3NXZatgzSw8Rs9GLvH6u5yLW259E2YZJaxAY9FVcApAB7'
                 'M1I8lOrLS206a3bw4jXVUFFLUBmOmjl7qMAMmC19UC0giLeDLF3wCPbI5fupxCVKJPaVF'
                 'HPXo1jH8uTKOPv9pqrAaEq2wmoXUtvOaoaoTNhv15y86EKKSTwbSiZVIzVT4EgFx25I5cP'
                 'A6WbtDUuGZZPFF6jnD0zu5LhH5EpbKzdYR2pO16OQYjnWK54ZBuHC5IO3bEVT4UkpIw6ee'
                 'WJApLmlBXzqBVSgG9Sv4BUbFUGbTkSrAoICEJADrwe8I1SjBoDxpTXEBew7xkS81aTrgHsr'
                 'wsQDu6utTxJELeLsMr8efapfeCRFB8z0AnEuFR6DurTwVCjijmxGlHoL6a91wkhAVsjsJNQ'
                 'c9ImNRrvnwxuBeHYPwFqKTQEf1bVmgfBGheouUDJtkcSLmSkOLf5rU9ZUQpE1WYm5s74sBC'
                 'ywaXXOqPH3wK1TFl1PhKr368KBYe9oBJfV3E8diWARALfKxeHs0SGiaFwDv7oXkaoE8B5ZCv'
                 '9AhB6KnozbzdW6p4SCAoFnee0HyT03uNxt5hLzbjC5c2AN7LxzEtGHZ2BYtUko6qCiG9EGKY'
                 'foV21VzOANQvGZDvo5vpBsxJbySEJtMST2pgIJ18NOzFFSzg0jfDUcy0Qpf5nVxfiorYX4zn'
                 'QvKkoXFFC3CH9pm2eWHhHiwA3qnUeSQSQjsFus7ZAKVIKZN54MvY91beEcbJbOjSmbcG3fRR'
                 '0XBj47uKWBefwC6KAKGL64OlAJcLqD50lsCV7nRoS8LgB1q11ccRjiLG4SdFOOFouLV4dsWm'
                 '5CP7G5gSt5NxyZu4tKGsZavnmAWF35ksFxEQlvE5137A3VhsQ6FJ6UNppKjv76GmL5SYcRmS'
                 'nIGMb0WKcbKzi6veUxwxvlGbOdXVFmm3kf7hvZQarT9eq0Wi4aIMRQYwmL5ZnOqHSddmKuTp'
                 'Og8DIxUwpu6u5z0TlmPo9WpIx9sNOMe8bKJPIdmxv22iUvNs5dY5M6J0VK5NNPeFIM5ze2gS'
                 'DDA5AgJRazkzypfJCXAf3ZTaPQZSmaBUw7pLu0yhXPFNMukrjhOSGMwXnUElhSDpNl30wpma'
                 'wcCSeYG0kZXuBfwMSExZyTf0ip5ANOgOSoIHN6FnbqntM52X8HjSbxPm4jAo9fBmXkbWSNhf'
                 'WbLF1Oisf6cbXgHamWcOshCf3H6nqIqI1FVfxaO8warADMpwGgo9BHMvFvr2wcqMUU2ABUJQ'
                 'L2J42vnX3PeW1uiRs7clCKYDqKIyLLvTRuTP6WncLOA5y4yziCF8XbADPCcO8FfoFEOhRiiC'
                 'EEvIVLHqwe0fer3A8jNjF48TGr3Tl1sAGwq5RCqbPerl0afYeM3N7mhYq8FqFIFuJL9Y1IeQ'
                 'K3RyR2jcxhHfTxSsLxDJBpx4N6T9uXfNbxQZbzrS3j4qvBP6gzpbK12l6hi1WzPMTQn25iiX'
                 'oXGO49G2JzdimO1ABBiBf0w3iMcHE5CZDIp3qZlSH8Cq5egMjFTXyuY3gV9WmGow5oVHz2b7'
                 'vlKKBS1TJWkLW2S4Ld2GejWlEAt1XHuNCFzUpSWAbL9kAM3V0FSqGomF6RkEFzMZcf9B9B9m'
                 'qdJxjJF1GKQ6kwTUu0D110Shn3VmTAC17sjujDwKxdpbPcXpDMZKem5aIaagtBLDtKt0IIBk'
                 'AShwcUGNbnh6SjjH18GgLpUcCuXJREIXk2YeZOj7UE6KEGP3DcS0UYCG6XqerdCDd6oXgN3t'
                 'jEjD6SqUeGtF0AGp3Lbw7ZDsQOHFOehRujRxtO4La4vBN5nleeZgF6lTt8OeG5CQb2OpdCG8'
                 'jYJXlNhjUlFqj4fllqPEIwMgXunYNdOal691fCbsxoIuPwENV86QgXp9uKgs21BIxw07QXp7'
                 'vuBrOcx0dcifjm0P6n37o520GPJ9kAqRVPdhqL6UAk4YgqRVmXdLImvv6mEjZnisZx3zZQtT'
                 'FC6aQh0Geiwzefgj86yGhyf4oI6rCTV7RHhEgQYDotJ06eucONYYCbg50Rpyzwy9okYvQo51'
                 '3gDYaQU7ElHPQ4Nvu8yaYjHznGkIFkwnYt06o5I5FM3fbxT6NCRaSbRyqYgX565LhoLfHrd0'
                 '6xtMvBOaLJjynmXlf51WFduFPGHVcQ3bCpAffEJ8kPL7EOmMdW1f6WVI8y9AjM8LrCmqUahY'
                 'XSnVcp5iuZim4gx6duH84cELZzkXjHA1RZD9wmY7RTTfZQJk9a0x5CjGH3oOAegBLeQpkNnN'
                 'hIz93fJJlDfobtrcMAzjM1TM1AmZkDZuGxFohPbpL9Qlxj436zCDCjcPZQhGM0SRpJ1VuUJc'
                 'HLKJ5mbJFkNhkecplvKzCL4XT4bHhsc2aZtISvOTaPdAtiyz5z3gGI31vWJU3HCbThBer68W'
                 '5YXwqZhp94KEfCeLU43OWflINWWjgysiRdLgO8mCmDzXW9f6quSJ9rVXLpsBqs1QAgCDiVYm'
                 'PtduDzduqZJnfxMMMkxPn82WK4zqFGS5b3wGKRutni8UVI0Fo8OwBQMc8VrFtIT2PR679lTo'
                 'WsWQCKKOX5KrvkkiLtd3QjBinHHz9tnExru2h0W51GADIQPWkgtRl50vmcbloWN6HiBeRSlv'
                 'nkzC9Nqih6otMY12QbSy0QrPtPjDYz8s8ZRvStQiHNvssWsqJL2zvM72pDy8cwDCAtCIxqKt'
                 'gEJitiUfv3KhJaQLDd9GJ9dLKZz69ivONPwvnikMOLGGQBGhvCV0RIfPywRxYFRkmTlg7mri'
                 '3WdVMmewhiEZaCs4k0DiOvgJ8DDcH2TSwGVFvuRRdMtl3i1c7SgtLX0sObIW70JMl8Ca6prx'
                 '5hR6ud3Hiuf3T363lRTCjQ9wv8NIYc3BK81cOvZKa5JMF3KCw57YeIfYMQQdngYScEA9nNPu'
                 'eMBh8DBUgIX30ojCOMNAfyCkZx3pEiGjEyInJmjWHwpIK0kqyd5YnixP4XYY3EIDk8MN5nO0'
                 '1V2cjBamcFBdlpobrx5ZCVeCQG11aJW0TJXxNMY1f7UNiTM8IRZWF26W1SXPpLqfukoBIiEZ'
                 'gEUeHwTNy4CweMuR0V5coT3YWQwSz9HYlSUzZefkthKwnD3sjGfn0L3o2Jjq8gl1FCpZhO8A'
                 'tRLQsxAJtcKCRetmiJNuKMkMEE86YMxVSCafeUrItds2n5fSDZLWJZ0NNWKkM7WGoFFHb3KD'
                 'Ld6NGBapeRc1VuGn9CiX8OtWPoDyNNwRgi3l1x79ipihmMjaUlmDKlur7cHCtwC3jbt9Ablj'
                 'LFrltWGa6tvcFqvzFh5cpRUpTXteyw5laifqtzrmcWsQwB0pyCNM9v326aCGPieg5mvgxJm3'
                 'lHzfFdiWysWcrF83PgkAamv1nadzM8pBLPcc9WyGcTTg2ObwMcyWvFW2gj3ipD4opAzZAUal'
                 '6ctMMOn5bbfmLkjPF9tyTtuLNLniuH03yJJI5gzapVkhIp2RSBBRis3NXZatgzSw8Rs9GLvH'
                 '6u5yLW259E2YZJaxAY9FVcApAB7M1I8lOrLS206a3bw4jXVUFFLUBmOmjl7qMAMmC19UC0gi'
                 'LeDLF3wCPbI5fupxCVKJPaVFHPXo1jH8uTKOPv9pqrAaEq2wmoXUtvOaoaoTNhv15y86EKKS'
                 'TwbSiZVIzVT4EgFx25I5cPA6WbtDUuGZZPFF6jnD0zu5LhH5EpbKzdYR2pO16OQYjnWK54ZBu'
                 'HC5IO3bEVT4UkpIw6eeWJApLmlBXzqBVSgG9Sv4BUbFUGbTkSrAoICEJADrwe8I1SjBoDxpTX'
                 'EBew7xkS81aTrgHsrwsQDu6utTxJELeLsMr8efapfeCRFB8z0AnEuFR6DurTwVCjijmxGlHoL'
                 '6a91wkhAVsjsJNQc9ImNRrvnwxuBeHYPwFqKTQEf1bVmgfBGheouUDJtkcSLmSkOLf5rU9ZUQ'
                 'pE1WYm5s74sBCywaXXOqPH3wK1TFl1PhKr368KBYe9oBJfV3E8diWARALfKxeHs0SGiaFwDv7'
                 'oXkaoE8B5ZCv9AhB6KnozbzdW6p4SCAoFnee0HyT03uNxt5hLzbjC5c2AN7LxzEtGHZ2BYtUk'
                 'o6qCiG9EGKYfoV21VzOANQvGZDvo5vpBsxJbySEJtMST2pgIJ18NOzFFSzg0jfDUcy0Qpf5nV'
                 'xfiorYX4znQvKkoXFFC3CH9pm2eWHhHiwA3qnUeSQSQjsFus7ZAKVIKZN54MvY91beEcbJbOjS'
                 'mbcG3fRR0XBj47uKWBefwC6KAKGL64OlAJcLqD50lsCV7nRoS8LgB1q11ccRjiLG4SdFOOFouL'
                 'V4dsWm5CP7G5gSt5NxyZu4tKGsZavnmAWF35ksFxEQlvE5137A3VhsQ6FJ6UNppKjv76GmL5S'
                 'YcRmSnIGMb0WKcbKzi6veUxwxvlGbOdXVFmm3kf7hvZQarT9eq0Wi4aIMRQYwmL5ZnOqHSddm'
                 'KuTpOg8DIxUwpu6u5z0TlmPo9WpIx9sNOMe8bKJPIdmxv22iUvNs5dY5M6J0VK5NNPeFIM5ze'
                 '2gSDDA5AgJRazkzypfJCXAf3ZTaPQZSmaBUw7pLu0yhXPFNMukrjhOSGMwXnUElhSDpNl30wpm'
                 'awcCSeYG0kZXuBfwMSExZyTf0ip5ANOgOSoIHN6FnbqntM52X8HjSbxPm4jAo9fBmXkbWSNhfW'
                 'bLF1Oisf6cbXgHamWcOshCf3H6nqIqI1FVfxaO8warADMpwGgo9BHMvFvr2wcqMUU2ABUJQL2J'
                 '42vnX3PeW1uiRs7clCKYDqKIyLLvTRuTP6WncLOA5y4yziCF8XbADPCcO8FfoFEOhRiiCEEvIV'
                 'LHqwe0fer3A8jNjF48TGr3Tl1sAGwq5RCqbPerl0afYeM3N7mhYq8FqFIFuJL9Y1IeQK3RyR2j'
                 'cxhHfTxSsLxDJBpx4N6T9uXfNbxQZbzrS3j4qvBP6gzpbK12l6hi1WzPMTQn25iiXoXGO49G2'
                 'JzdimO1ABBiBf0w3iMcHE5CZDIp3qZlSH8Cq5egMjFTXyuY3gV9WmGow5oVHz2b7vlKKBS1TJW'
                 'kLW2S4Ld2GejWlEAt1XHuNCFzUpSWAbL9kAM3V0FSqGomF6RkEFzMZcf9B9B9mqdJxjJF1GKQ6'
                 'kwTUu0D110Shn3VmTAC17sjujDwKxdpbPcXpDMZKem5aIaagtBLDtKt0IIBkAShwcUGNbnh6Sj'
                 'jH18GgLpUcCuXJREIXk2YeZOj7UE6KEGP3DcS0UYCG6XqerdCDd6oXgN3tjEjD6SqUeGtF0AGp'
                 '3Lbw7ZDsQOHFOehRujRxtO4La4vBN5nleeZgF6lTt8OeG5CQb2OpdCG8jYJXlNhjUlFqj4fllq'
                 'PEIwMgXunYNdOal691fCbsxoIuPwENV86QgXp9uKgs21BIxw07QXp7vuBrOcx0dcifjm0P6n37'
                 'o520GPJ9kAqRVPdhqL6UAk4YgqRVmXdLImvv6mEjZnisZx3zZQtTFC6aQh0Geiwzefgj86yGhy'
                 'f4oI6rCTV7RHhEgQYDotJ06eucONYYCbg50Rpyzwy9okYvQo513gDYaQU7ElHPQ4Nvu8yaYjHzn'
                 'GkIFkwnYt06o5I5FM3fbxT6NCRaSbRyqYgX565LhoLfHrd06xtMvBOaLJjynmXlf51WFduFPGH'
                 'VcQ3bCpAffEJ8kPL7EOmMdW1f6WVI8y9AjM8LrCmqUahYXSnVcp5iuZim4gx6duH84cELZzkXj'
                 'HA1RZD9wmY7RTTfZQJk9a0x5CjGH3oOAegBLeQpkNnNhIz93fJJlDfobtrcMAzjM1TM1AmZkDZ'
                 'uGxFohPbpL9Qlxj436zCDCjcPZQhGM0SRpJ1VuUJcHLKJ5mbJFkNhkecplvKzCL4XT4bHhsc2a'
                 'ZtISvOTaPdAtiyz5z3gGI31vWJU3HCbThBer68W5YXwqZhp94KEfCeLU43OWflINWWjgysiRdL'
                 'gO8mCmDzXW9f6quSJ9rVXLpsBqs1QAgCDiVYmPtduDzduqZJnfxMMMkxPn82WK4zqFGS5b3wGK'
                 'Rutni8UVI0Fo8OwBQMc8VrFtIT2PR679lToWsWQCKKOX5KrvkkiLtd3QjBinHHz9tnExru2h0W'
                 '51GADIQPWkgtRl50vmcbloWN6HiBeRSlvnkzC9Nqih6otMY12QbSy0QrPtPjDYz8s8ZRvStQiH'
                 'NvssWsqJL2zvM72pDy8cwDCAtCIxqKtgEJitiUfv3KhJaQLDd9GJ9dLKZz69ivONPwvnikMOLG'
                 'GQBGhvCV0RIfPywRxYFRkmTlg7mri3WdVMmewhiEZaCs4k0DiOvgJ8DDcH2TSwGVFvuRRdMtl3'
                 'i1c7SgtLX0sObIW70JMl8Ca6prx5hR6ud3Hiuf3T363lRTCjQ9wv8NIYc3BK81cOvZKa5JMF3K'
                 'Cw57YeIfYMQQdngYScEA9nNPueMBh8DBUgIX30ojCOMNAfyCkZx3pEiGjEyInJmjWHwpIK0kqy'
                 'd5YnixP4XYY3EIDk8MN5nO01V2cjBamcFBdlpobrx5ZCVeCQG11aJW0TJXxNMY1f7UNiTM8IRZ'
                 'WF26W1SXPpLqfukoBIiEZgEUeHwTNy4CweMuR0V5coT3YWQwSz9HYlSUzZefkthKwnD3sjGfn0'
                 'L3o2Jjq8gl1FCpZhO8AtRLQsxAJtcKCRetmiJNuKMkMEE86YMxVSCafeUrItds2n5fSDZLWJZ0'
                 'NNWKkM7WGoFFHb3KDLd6NGBapeRc1VuGn9CiX8OtWPoDyNNwRgi3l1x79ipihmMjaUlmDKlur7'
                 'cHCtwC3jbt9AbljLFrltWGa6tvcFqvzFh5cpRUpTXteyw5laifqtzrmcWsQwB0pyCNM9v326aC'
                 'GPieg5mvgxJm3lHzfFdiWysWcrF83PgkAamv1nadzM8pBLPcc9WyGcTTg2ObwMcyWvFW2gj3ip'
                 'D4opAzZAUal6ctMMOn5bbfmLkjPF9tyTtuLNLniuH03yJJI5gzapVkhIp2RSBBRis3NXZatgzS'
                 'w8Rs9GLvH6u5yLW259E2YZJaxAY9FVcApAB7M1I8lOrLS206a3bw4jXVUFFLUBmOmjl7qMAMmC'
                 '19UC0giLeDLF3wCPbI5fupxCVKJPaVFHPXo1jH8uTKOPv9pqrAaEq2wmoXUtvOaoaoTNhv15y8'
                 '6EKKSTwbSiZVIzVT4EgFx25I5cPA6WbtDUuGZZPFF6jnD0zu5LhH5EpbKzdYR2pO16OQYjnWK5'
                 '4ZBuHC5IO3bEVT4UkpIw6eeWJApLmlBXzqBVSgG9Sv4BUbFUGbTkSrAoICEJADrwe8I1SjBoDx'
                 'pTXEBew7xkS81aTrgHsrwsQDu6utTxJELeLsMr8efapfeCRFB8z0AnEuFR6DurTwVCjijmxGlH'
                 'oL6a91wkhAVsjsJNQc9ImNRrvnwxuBeHYPwFqKTQEf1bVmgfBGheouUDJtkcSLmSkOLf5rU9ZU'
                 'QpE1WYm5s74sBCywaXXOqPH3wK1TFl1PhKr368KBYe9oBJfV3E8diWARALfKxeHs0SGiaFwDv7'
                 'oXkaoE8B5ZCv9AhB6KnozbzdW6p4SCAoFnee0HyT03uNxt5hLzbjC5c2AN7LxzEtGHZ2BYtUko'
                 '6qCiG9EGKYfoV21VzOANQvGZDvo5vpBsxJbySEJtMST2pgIJ18NOzFFSzg0jfDUcy0Qpf5nVxf'
                 'iorYX4znQvKkoXFFC3CH9pm2eWHhHiwA3qnUeSQSQjsFus7ZAKVIKZN54MvY91beEcbJbOjSmb'
                 'cG3fRR0XBj47uKWBefwC6KAKGL64OlAJcLqD50lsCV7nRoS8LgB1q11ccRjiLG4SdFOOFouLV4'
                 'dsWm5CP7G5gSt5NxyZu4tKGsZavnmAWF35ksFxEQlvE5137A3VhsQ6FJ6UNppKjv76GmL5SYcR'
                 'mSnIGMb0WKcbKzi6veUxwxvlGbOdXVFmm3kf7hvZQarT9eq0Wi4aIMRQYwmL5ZnOqHSddmKuTp'
                 'Og8DIxUwpu6u5z0TlmPo9WpIx9sNOMe8bKJPIdmxv22iUvNs5dY5M6J0VK5NNPeFIM5ze2gSDD'
                 'A5AgJRazkzypfJCXAf3ZTaPQZSmaBUw7pLu0yhXPFNMukrjhOSGMwXnUElhSDpNl30wpmawcCS'
                 'eYG0kZXuBfwMSExZyTf0ip5ANOgOSoIHN6FnbqntM52X8HjSbxPm4jAo9fBmXkbWSNhfWbLF1O'
                 'isf6cbXgHamWcOshCf3H6nqIqI1FVfxaO8warADMpwGgo9BHMvFvr2wc', True)
            ]

            for data in test_data:
                print_log(string=data[0], expected=data[1])
                self.assertEqual(data[1], has_subpattern(data[0]))
