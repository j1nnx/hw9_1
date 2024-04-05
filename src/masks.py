def mask_credit_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    masked_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    return masked_number


def mask_account_number(account_number: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""
    masked_number = f"**{account_number[-4:]}"
    return masked_number