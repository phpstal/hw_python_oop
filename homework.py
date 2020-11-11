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
            if date ==  self.records[record.date]:
                total += self.records[record.amount]
        return total

    def get_week_stats(self):
        total = 0 
        week_ago = today - dt.timedelta(days=7)
        for record in self.records:
            if week_ago <=  self.records[record.date]:
                total += self.records[record.amount]
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
        return 'rub', 'usd', 'eur'


if __name__ == '__main__':    
    
    cash_calculator = CashCalculator(1000)

    cash_calculator.add_record(Record(amount=145, comment="кофе")) 
    # и к этой записи тоже дата должна добавиться автоматически
    cash_calculator.add_record(Record(amount=300, comment="Серёге за обед"))
    # а тут пользователь указал дату, сохраняем её
    cash_calculator.add_record(Record(amount=3000, comment="бар в Танин др", date="08.11.2019"))
                    
    print(cash_calculator.get_today_cash_remained("rub"))
    # должно напечататься
    # На сегодня осталось 555 руб 
    print((today - dt.timedelta(days=7)).strftime('%d.%m.%Y'))