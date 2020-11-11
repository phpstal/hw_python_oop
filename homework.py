import datetime as dt

today = dt.datetime.today()

class Calculator:    
    def __init__(self, limit):
        self.limit = limit    
        self.records = []

    def add_record(self, record):        
        self.records.append(record)

    def get_today_stats(self):
        total = 0
        date = today.strftime('%d.%m.%Y')
        for record in self.records:
            if date ==  record.date:
                total += record.amount
        return total

    def get_week_stats(self):
        total = 0 
        week_ago = today - dt.timedelta(days=7)
        for record in self.records:
            if week_ago <=  record.date:
                total += record.amount
        return total


class Record:
    def __init__(self, amount, comment, date = today.strftime('%d.%m.%Y')):
        self.amount = amount
        self.comment = comment
        self.date = date


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

    cash_calculator.add_record(Record(amount=100, comment="кофе")) 
    
    cash_calculator.add_record(Record(amount=800, comment="Серёге за обед"))
    
    cash_calculator.add_record(Record(
        amount=3000, 
        comment="бар в Танин др", 
        date="08.11.2019"))
                    
    print(cash_calculator.get_today_cash_remained("руб"))    


    calor_calc = CaloriesCalculator(3200)

    calor_calc.add_record(Record(amount=1186, comment="Кусок тортика. И ещё один.")) 
    
    calor_calc.add_record(Record(amount=84, comment="Йогурт"))
    
    calor_calc.add_record(Record(
        amount=1140, 
        comment="Баночка чипсов.", 
        date="08.11.2019"))
                    
    print(calor_calc.get_calories_remained())