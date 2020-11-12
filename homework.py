import datetime as dt

today = dt.datetime.today().date()
date_format = '%d.%m.%Y'

class Calculator:    
    def __init__(self, limit):
        self.limit = limit    
        self.records = []

    def add_record(self, record):        
        self.records.append(record)

    def get_today_stats(self):
        total = 0        
        for record in self.records:
            if today ==  record.date:
                total += record.amount
        return total

    def get_week_stats(self):
        total = 0 
        week_ago = today - dt.timedelta(days = 7)        
        for record in self.records:
            if week_ago <=  record.date:
                total += record.amount
        return total


class Record:
    def __init__(self, amount, comment, date = None):
        self.amount = amount
        self.comment = comment
        self.date = self.check_type_date(date)
        
    def check_type_date(self, date):
        if isinstance(date, str): 
            return dt.datetime.strptime(date, date_format).date()
        elif date is None:
            return today
        else:
            return dt.datetime(date).date()
            

class CashCalculator(Calculator):
    USD_RATE = 76.58
    EURO_RATE = 90.37

    def get_today_cash_remained(self, currency):        
        remains = self.limit - self.get_today_stats()        
        if currency == 'usd': remains = round(remains / self.USD_RATE, 2)
        if currency == 'eur': remains = round(remains / self.EURO_RATE, 2)
        if remains > 0:
            return f'На сегодня осталось {remains} {currency}'
        elif remains == 0:
            return 'Денег нет, держись'
        else:
            remains = -(remains)
            return f'Денег нет, держись: твой долг - {remains} {currency}'


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        remains = self.limit - self.get_today_stats()
        if remains > 0:
            return(f'Сегодня можно съесть что-нибудь ещё, но '
                   f'с общей калорийностью не более {remains} кКал')
        else:
            return 'Хватит есть!'


if __name__ == '__main__':    
    
    cash_calculator = CashCalculator(1000)

    cash_calculator.add_record(Record(amount=50, comment="кофе"))     

    cash_calculator.add_record(Record(800, "Серёге за обед"))

    cash_calculator.add_record(Record(800, "Серёге за обед", '10.11.2020'))

    #print(cash_calculator.get_today_cash_remained("руб"))    
    print(cash_calculator.get_today_stats())    
    print(cash_calculator.get_week_stats())    

