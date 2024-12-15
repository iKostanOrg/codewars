"""
Solution for -> Count IP Addresses.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def ips_between(start: str, end: str) -> int:
    """
    Find IPs between 2 addresses.

    A function that receives two IPv4 addresses,
    and returns the number of addresses between
    them (including the first one, excluding the
    last one).
    :param start: str
    :param end: str
    :return: int
    """
    ip_start: list = [int(a) for a in start.split('.')]
    ip_end: list = [int(b) for b in end.split('.')]
    ips = zip(ip_start, ip_end)
    ips_range: list = [0, 0, 0, 0]

    for ip_id, ip in enumerate(ips):
        calc_ip_range(ip, ip_id, ips_range)

    return calc_result(ips_range)


def calc_ip_range(ip, ip_id, ips_range) -> None:
    """
    Calculate IPs range.

    :param ip:
    :param ip_id:
    :param ips_range:
    :return: None
    """
    if ip[0] == ip[1] != 0:
        ips_range[ip_id] = 0
    elif ip[1] == 0 and ip[0] != 0 and ips_range[ip_id - 1] > 0:
        ips_range[ip_id] = 256 - ip[0]
    elif ip[1] > ip[0]:
        ips_range[ip_id] = ip[1] - ip[0]
    elif ip[1] == ip[0] == 0 and ips_range[ip_id - 1] > 0:
        ips_range[ip_id] = 256


def calc_result(ips_range) -> int:
    """
    Calculate result.

    :param ips_range:
    :return: int
    """
    result: int = 1
    for i in ips_range:
        if i != 0:
            result *= i
    return result
