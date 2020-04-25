#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


def domain_name(url: str) -> str:
    """
    Parses out just the domain name and
    returns it as a string.

    :param url: URL as a string
    :return: domain name as a string
    """
    for url_segment in url.split('/'):
        if '.' in url_segment:
            if 'www' in url_segment:
                return url_segment.split('.')[1]
            return url_segment.split('.')[0]
