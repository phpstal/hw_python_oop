import datetime as dt


class Calculator:    
    def __init__(self, limit):
        self.limit = limit    
        self.records = []

    def add_record(self, record):        
        self.records.append(record)

    def get_today_stats(self):
        pass

    def get_week_stats(self):
        pass


class Record:
    def __init__(self, amount, comment, date):
        self.amount = amount
        self.comment = comment
        self.date = date


class CashCalculator(Calculator):
    def get_today_cash_remained(self):
        return 'cash'


# создадим калькулятор денег с дневным лимитом 1000
cash_calculator = CashCalculator(1000)
        
# дата в параметрах не указана, 
# так что по умолчанию к записи должна автоматически добавиться сегодняшняя дата
cash_calculator.add_record(Record(amount=145, comment="кофе")) 
# и к этой записи тоже дата должна добавиться автоматически
cash_calculator.add_record(Record(amount=300, comment="Серёге за обед"))
# а тут пользователь указал дату, сохраняем её
cash_calculator.add_record(Record(amount=3000, comment="бар в Танин др", date="08.11.2019"))
                
print(cash_calculator.get_today_cash_remained("rub"))
# должно напечататься
# На сегодня осталось 555 руб 
if __name__ == '__main__'