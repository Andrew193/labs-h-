Проблеми існуючого методу process_data:
	
	- Метод занадто великий і містить багато логіки обробки різних типів даних.
    	- Існує повторюваний код (логіка обробки типів 'A', 'B' і 'C').
    	- Код важко читати і підтримувати, оскільки він містить багато if-elif-else конструкцій.

У цьому рефакторінгу було: 

	1. Створено клас DataProcessor, який містить список стратегій для обробки різних типів даних. 
	2. Кожен тип даних обробляється окремою стратегією, яка інкапсулює логіку обробки. 
	3. Метод process_data в DataProcessor використовує відповідну стратегію для обробки кожного елемента даних.

Пілся рефакторінгу код став більш читабельним і простим у підтримці. Завдяки використанню шаблону "Стратегія", код став більш гнучким і розширюваним. Додавання нового типу даних буде легше виконати. Зменшилась складність методу process_data, що полегшує його розуміння та тестування.