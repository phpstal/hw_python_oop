≡ Краткое руководство Калькулятор денег и калорий

# Описание проекта Калькулятор денег и калорий

Данное web-приложение является очень простым калькулятором для подсчета потраченных калорий и денег.

***

## Установка
Для работы проекта достаточно установить:
- [Python](https://www.python.org/)
- Любой текстовый редактор кода (опционально). Например, [Visual Studio Code](https://code.visualstudio.com/download)
- Если вы пользователь Windows, то нужно установить [Git](https://git-scm.com/)

#### Команда клонирования репозитория:
    git clone https://github.com/phpstal/api_final_yatube

### Подготовка проекта
В файле **homework.py** нужно создать объект нужного класса: либо **CashCalculator**, либо **CaloriesCalculator**.
Например, создаем объект **CashCalculator**
    
    cash_calculator = CashCalculator(1000), где 1000 - это лимит денег
Далее перечисляем все траты, например:
```
cash_calculator.add_record(Record(100, "Серёге за обед", '11.11.2020'))

cash_calculator.add_record(Record(200, "Серёге за обед", '10.11.2020'))

cash_calculator.add_record(Record(200, "Серёге за обед", '09.11.2020'))

cash_calculator.add_record(Record(200, "Серёге за обед", '8.11.2020'))
```
И после всех наших трат выводим на печать результат. Причем можно указать в какой валюте это все будет.

    print(cash_calculator.get_today_cash_remained("usd"))

#### Запуск проекта:
Запускаете командную строку. Если вы пользователь Windows, то можете открыть консоль в текстовом редакторе. Либо в консоле Bash. Перейдите в каталог проекта и выполните команду:

    python homework.py

В консоле будет выведен результат, что-то вроде этого:

    На сегодня осталось 15.83 USD
    
#### Автор:
Владимир Половников. Задание было выполнено в рамках курса от Яндекс.Практикум.