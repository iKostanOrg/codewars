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
    result = ''
    for url_segment in url.split('/'):
        if '.' in url_segment:
            if 'www' in url_segment:
                result = url_segment.split('.')[1]
            else:
                result = url_segment.split('.')[0]
            break
    return result
