# goit-algo-hw-10
Home work in scope of Basic Algorithms and Data Structures module

## Аналіз

Під час порівняння методу Монте-Карло і аналітичного розрахунку для інтеграції функції \(x^2 + 2x + 4\) на інтервалі від 0 до 2, були отримані такі результати:

- **Аналітичний інтеграл**: 14.6667
- **Інтеграл за методом Монте-Карло**: 14.6223

Різниця між цими двома методами становить приблизно 0.0444, що відповідає відхиленню близько 0.3%. Це демонструє досить високу точність методу Монте-Карло для даної задачі.

## Висновки

1. **Точність методу Монте-Карло**
   Метод Монте-Карло виявився досить точним, роблячи його практичним рішенням для числових обчислень, особливо у ситуаціях, де виконання аналітичних обрахунків складно або неможливо.

2. **Практичне застосування**
   Отримана точність робить метод Монте-Карло корисним для широкого спектру обчислень, зокрема, коли необхідні швидкі і приблизні рішення.

3. **Можливості для оптимізації**
   Для додаткового уменьшення помилок і варіативності можливо збільшити кількість випробувань у моделі Монте-Карло. Також корисно провести кілька незалежних симуляцій і усереднити їх результати.

4. **Перевірка роботи методу**
   Бажано регулярно перевіряти метод на різних функціях та інтервалах інтегрування, щоб забезпечити його універсальність та надійність.

Метод Монте-Карло показав високу надійність та точність у даному випадку, рекомендується його застосування для подібних обчислювальних задач.