import random
import math

from decimal import *

class Tool:
    def __init__(self):
        pass

    @staticmethod
    def random_number(min_number: int, max_number: int):
        delta_number = max_number - min_number
        random_number = math.fabs(Decimal(random.uniform(0, 1)) * 1000000 * delta_number)
        return int(random_number % delta_number) + min_number

    @staticmethod
    def random_numbers(min_number: int, max_number: int):
        if min_number == max_number:
            return min_number, max_number

        random_number1 = Tool.random_number(min_number, max_number)
        random_number2 = Tool.random_number(min_number, max_number)
        while random_number1 == random_number2:
            random_number2 = Tool.random_number(min_number, max_number)

        min_result = min(random_number1, random_number2)
        max_result = max(random_number1, random_number2)
        return min_result, max_result

    @staticmethod
    def upper_times(number: int, divisor: int):
        if divisor == 0:
            return 0

        upper_number = 0
        if number % divisor != 0:
            upper_number = 1

        return int(number / divisor) + upper_number

