import sys
from src.exception import CustomException
from colorama import Fore, Style, init

init(autoreset=True)  # Rangni avtomatik tiklab yuboradi

def divide(x, y):
    return x / y

if __name__ == "__main__":
    try:
        result = divide(10, 0) # 0 ga bo'lib bo'lmaydi shunga error chiqardi, 0 o'zgarsa error yo'q
        print(f"{Fore.GREEN}Natija: {result}")
    except Exception as e:
        custom_exc = CustomException(e, sys)
        print(f"{Fore.RED}{custom_exc}")  # QIZILDA chiqaradi
