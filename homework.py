import datetime as dt


class Calculator:    
    def __init__(self, limit):
        self.limit = limit    
        self.records = []

    def add_record(self, record):        
        self.records.append(record)

    def get_today_stats(self):        
        today = dt.date.today()
        return sum(record.amount for record in self.records 
                   if record.date == today)

    def get_week_stats(self):
        today = dt.date.today()       
        week_ago = today - dt.timedelta(days = 7)                
        return sum(record.amount for record in self.records 
                   if week_ago < record.date <= today)


class Record:
    DATE_FORMAT = '%d.%m.%Y'   

    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        self.date = (dt.datetime.strptime(date, self.DATE_FORMAT).date() 
                     if isinstance(date, str) else dt.date.today())

class CashCalculator(Calculator):
    USD_RATE = 60.00
    EURO_RATE = 70.00
    GREATER_THAT_ZERO = 'На сегодня осталось {remains} {currency}'
    EQUAL_TO_ZERO = 'Денег нет, держись'
    LESS_THAT_ZERO = 'Денег нет, держись: твой долг - {remains} {currency}'
    CURRENCIES = {
        'usd': ['USD', USD_RATE],
        'eur': ['Euro', EURO_RATE],
        'rub': ['руб', 1.00]        
    }
    def get_today_cash_remained(self, currency):        
        remains = self.limit - self.get_today_stats()
        if remains == 0: return self.EQUAL_TO_ZERO
        remains = round(remains / self.CURRENCIES[currency][1], 2)
        type_currency = self.CURRENCIES[currency][0]
        if remains > 0:
            return self.GREATER_THAT_ZERO.format(
                remains=remains, 
                currency=type_currency)                        
        return self.LESS_THAT_ZERO.format(
            remains=-(remains), 
            currency=type_currency)


class CaloriesCalculator(Calculator):
    CAN_EAT = ('Сегодня можно съесть что-нибудь ещё, но '
               'с общей калорийностью не более {remains} кКал')               
    CAN_NOT_EAT = 'Хватит есть!'    

    def get_calories_remained(self):        
        remains = self.limit - self.get_today_stats()
        if remains > 0:
            return self.CAN_EAT.format(remains=remains) 
        return self.CAN_NOT_EAT


if __name__ == '__main__':    
    
    cash_calculator = CashCalculator(1000)

    cash_calculator.add_record(Record(amount=50, comment="кофе"))     

    cash_calculator.add_record(Record(100, "Серёге за обед", '11.11.2020'))

    cash_calculator.add_record(Record(200, "Серёге за обед", '10.11.2020'))

    cash_calculator.add_record(Record(200, "Серёге за обед", '09.11.2020'))

    cash_calculator.add_record(Record(200, "Серёге за обед", '8.11.2020'))

    print(cash_calculator.get_today_cash_remained("usd"))