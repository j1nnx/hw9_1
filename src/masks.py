def mask_credit_card_number(card_number: str) -> str:
    masked_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    return masked_number


def mask_account_number(account_number: str) -> str:
    masked_number = f"**{account_number[-4:]}"
    return masked_number


credit_card_number = input()
masked_credit_card = mask_credit_card_number(credit_card_number)
print(masked_credit_card)

account_number = input()
masked_account = mask_account_number(account_number)
print(masked_account)
