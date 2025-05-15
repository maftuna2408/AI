import sys
from src.exception import CustomException
from colorama import Fore, Style, init

init(autoreset=True)  # Rangni avtomatik tiklab yuboradi

def divide(x, y):
    return x / y

if __name__ == "__main__":
    try:
        result = divide(10, 0)
        print(f"{Fore.GREEN}Natija: {result}")
    except Exception as e:
        custom_exc = CustomException(e, sys)
        print(f"{Fore.RED}{custom_exc}")  # QIZILDA chiqaradi
