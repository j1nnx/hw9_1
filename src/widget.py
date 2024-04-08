def mask_number(number_info: str) -> str:
    """"""
    parts = number_info.split()
    if len(parts) < 2:
        return number_info
    masked_part = ''
    if parts[0] == 'Счет':
        number_type = 'Счет'
        account_number = parts[1]
        masked_part = '**' + account_number[-4:]
    else:
        number_type = parts[0]
        card_number = parts[1]
        masked_part = card_number[:4] + ' ' + '*' * 2 + '*' * 4 + ' ' + '****' + ' ' + card_number[-4:]
    return f'{number_type} {masked_part}'
