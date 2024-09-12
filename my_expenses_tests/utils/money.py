import config


def int_to_str(value, currency='$'):
    if config.settings.is_bstack:
        currency = '€'
    return f'{currency}{float(value):,.02f}'


def str_to_int(string, currency='$'):
    if config.settings.is_bstack:
        currency = '€'
    return int(string.removeprefix(currency).removesuffix('.00').replace(',', ''))
