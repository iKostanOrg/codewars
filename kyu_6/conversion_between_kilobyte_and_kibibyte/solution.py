"""
Solution for -> Conversion between Kilobyte and KibiByte.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

UNITS: dict = {
    'KiB': ("kB", 1.024),
    "TiB": ("TB", 1.09951163),
    "GiB": ("GB", 1.07374182),
    'MiB': ('MB', 1.048576),
    'kB': ("KiB", 0.9765625),
    "TB": ("TiB", 0.9094947),
    "GB": ("GiB", 0.93132257461548),
    'MB': ('MiB', 0.95367432)}


def memorysize_conversion(memory_size: str) -> str:
    """
    Convert between the kB and the KiB-Units.

    The function receives as parameter a memory size
    including a unit and converts into the corresponding
    unit of the other system.
    :param memory_size: str
    :return: str
    """
    # Extract units and ratio
    units, convertor = unit_extractor(memory_size)
    # Convert memory size into float
    memory: float = float(memory_size.split()[0]) * convertor
    # No trailing zeros allowed
    memory_str: str = f'{memory:.3f}'
    return f'{memory_str.rstrip("0")} {units}'


def unit_extractor(memory_size: str) -> tuple:
    """
    Convert between multiple-byte units.

    :param memory_size: str
    :return: str
    """
    units: str = ''
    convertor: float = 0.0
    for key, val in UNITS.items():
        if key in memory_size:
            units = val[0]
            convertor = val[1]
            break
    return units, convertor