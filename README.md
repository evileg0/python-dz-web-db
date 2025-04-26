Исторические цены акций на конец дня

Запустить web.py

Перейти на http://127.0.0.1:5000/

Установить лимит отображения записей

![изображение](https://github.com/user-attachments/assets/99acd0e8-ea59-4516-8e95-9ad2500380ae)

Выбрать компанию

![изображение](https://github.com/user-attachments/assets/ed8f0e36-a5fb-4196-96b6-ef25857b257c)

Отобраться список цен акций по датам
![изображение](https://github.com/user-attachments/assets/5ad1ddb5-e173-4585-a945-01ee21095739)

API

/list - Список всех компаний (используется для загрузки выпадающего списка)

/stocks?ticker=<ticker_id>[&limitrows=\<number\>] - запрос списка котировок

ticker_id - тикер компании

number - лимит возвращаемых строк
