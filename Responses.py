from datetime import datetime
# from currency_converter import CurrencyConverter


def sample_responses(input_text):
    user_massage = str(input_text).lower()

    if user_massage in ("rate"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y ")
        
        # course = c.convert(100, 'EUR', 'USD')       

        return str(date_time)
    
    return "I don't understad you =("
