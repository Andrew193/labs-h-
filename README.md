У першому рефакторінгу для видалення дублювання з функцій calculate_total_price та calculate_total_price_with_tax, було створено приватну функцію _calculate_total_price, яка виконує основну логіку обчислення загальної суми. Це дозволило зменшити кількість повторюваних рядків коду.

У другому рефакторінгу дублювання коду було усунуто шляхом створення приватного методу _calculate_statistics, який використовується для обчислення загальної суми та кількості елементів даних.