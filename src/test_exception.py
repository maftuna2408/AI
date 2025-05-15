import sys
from src.exception import CustomException
import logging  # log faylni ham kuzatamiz

def divide(x, y):
    return x / y

try:
    result = divide(10, 0)
except Exception as e:
    raise CustomException(e, sys)
