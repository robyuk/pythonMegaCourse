meals = ['pasta', 'pizza', 'salad']

for index, meal in enumerate(meals):
    print(index, meal.capitalize())

print(f'\nAfter the for loop, index={index} and meal={meal}.')

print(type(enumerate(meals)))
print(enumerate(meals))
print(list(enumerate(meals)))