from pulp import LpMaximize, LpProblem, LpVariable

model = LpProblem("Maximize_Production", LpMaximize)

lemonade = LpVariable("lemonade", lowBound=0, cat='Integer')
juice = LpVariable("juice", lowBound=0, cat='Integer')

model += lemonade + juice

model += 2 * lemonade + juice <= 100, "Water_Constraint"
model += lemonade <= 50, "Sugar_Constraint"
model += lemonade <= 30, "Lemon_Juice_Constraint"
model += 2 * juice <= 40, "Fruit_Puree_Constraint"

model.solve()

print(f"Кількість виробленого лимонаду: {lemonade.value()}")
print(f"Кількість виробленого фруктового соку: {juice.value()}")
print(f"Максимальна загальна кількість вироблених продуктів: {model.objective.value()}")
