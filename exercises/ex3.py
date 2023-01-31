# Ex 1
country = input("What country are you from? ").lower()

match country:
    case 'usa':
        print("Hello")
    case 'india':
        print("Namaste")
    case 'germany':
        print("Hallo")

# ex 2
ingredients = ["john smith", "sen plakay", "dora ngacely"]
for item in ingredients:
    print(item.title())


