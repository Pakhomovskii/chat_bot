from datetime import datetime
from currency_converter import CurrencyConverter


def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("rate"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y ")
        c = CurrencyConverter()
        course = c.convert(1, 'USD', 'RUB')
        course = str(round(course, 2))
        return str(f"""
        taday is {date_time}\nand Ruble's exchange rate  is {course}""")
    
    return "I don't understad you =("
