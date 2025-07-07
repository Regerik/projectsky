from src.masks import get_mask_card_number,get_mask_account

def mask_account_card(data: str) -> str:
    def mask_account_card(data: str) -> str:
        last_space = data.rfind(' ')
        if 'Счет' in data[:last_space]:
            return data[:last_space] + ' ' + get_mask_account(data[last_space + 1:])
        else:
            return data[:last_space] + ' ' + get_mask_card_number(data[last_space + 1:])
