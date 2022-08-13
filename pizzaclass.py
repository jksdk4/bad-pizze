class Toppings:
    def __init__(self) -> None:
        self.options = [
            {
               "pepperoni": {
                    'name': "pepperoni",
                    'diet': "M",
                    'sauce': False
                },
                "hamburger": {
                    'name': "hamburger",
                    'diet': "M",
                    'sauce': False
                },
                "italian sausage": {
                    'name': "italian sausage",
                    'diet': "M",
                    'sauce': False
                },
                "anchovies": {
                    'name': "anchovies",
                    'diet': "M",
                    'sauce': False
                },
                "chicken": {
                    'name': "chicken",
                    'diet': "M",
                    'sauce': False
                },
                "bacon": {
                    'name': "bacon",
                    'diet': "M",
                    'sauce': False
                },
                "ham": {
                    'name': "ham",
                    'diet': "M",
                    'sauce': False
                }
            },
            {
                "alfredo": {
                    'name': "alfredo",
                    'diet': "V", 
                    'sauce': True
                },
                "cajun ranch": {
                    'name': "cajun ranch",
                    'diet': "V", 
                    'sauce': True
                },
                "cheese sauce": {
                    'name': "cheese sauce",
                    'diet': "V", 
                    'sauce': True
                },
                "shredded mozzarella": {
                    'name': "shredded mozzarella",
                    'diet': "V",
                    'sauce': False
                },
                "shredded cheddar": {
                    'name': "shredded cheddar",
                    'diet': "V", 
                    'sauce': False
                },
                "fresh mozzarella": {
                    'name': "fresh mozzarella",
                    'diet': "V",
                    'sauce': False
                },
                "honey": {
                    'name': "honey",
                    'diet': "V", 
                    'sauce': False
                },
                "scrambled eggs": {
                    'name': "scrambled eggs",
                    'diet': "V", 
                    'sauce': False
                },
                 "marinara": {
                    'name': "marinara",
                    'diet': "VV",
                    'sauce': True
                },
                "garlic + olive oil": {
                    'name': "garlic + olive oil",
                    'diet': "VV",
                    'sauce': True
                },
                "no cheese": {
                    'name': "no cheese",
                    'diet': "VV",
                    'sauce': True
                },
                "vegan cheese": {
                    'name': "vegan cheese",
                    'diet': "VV",
                    'sauce': False
                },
                "bell peppers": {
                    'name': "bell peppers",
                    'diet': "VV",
                    'sauce': False
                },
                "red bell peppers": {
                    'name': "red bell peppers",
                    'diet': "VV",
                    'sauce': False
                },
                "spinach": {
                    'name': "spinach",
                    'diet': "VV",
                    'sauce': False
                },
                "artichokes": {
                    'name': "artichokes",
                    'diet': "VV",
                    'sauce': False
                },
                "olives": {
                    'name': "olives",
                    'diet': "VV",
                    'sauce': False
                },
                "mushrooms": {
                    'name': "mushrooms",
                    'diet': "VV",
                    'sauce': False
                },
                "diced tomato": {
                    'name': "diced tomato",
                    'diet': "VV",
                    'sauce': False
                },
                "sliced tomato": {
                    'name': "sliced tomato",
                    'diet': "VV",
                    'sauce': False
                },
                "lettuce": {
                    'name': "lettuce",
                    'diet': "VV",
                    'sauce': False
                },
                "red onion": {
                    'name': "red onion",
                    'diet': "VV",
                    'sauce': False
                },
            }
        ]
            

class Pizza:
    def __init__(self, name, dough_flavor, shell_type, price, size, toppings = []):
        self.name = name
        self.dough_flavor = dough_flavor
        self.shell_type = shell_type
        self.price = price
        self.size = size
        self.toppings = toppings
        
    def __repr__(self):
        desc = "{name} Pizza\n" \
        "{dough_flavor} Crust\n" \
        "Price: ${price}\n" \
        "Size: {size}\"\n" \
        "Type: {shell_type}\n" \
        "Toppings: {toppings}\n" \
        "Vegan? {is_vegan}\n" \
        "Vegetarian? {is_veg}".format(
            name=self.name.title(),
            dough_flavor=self.dough_flavor.title(),
            price=self.price,
            size=self.size,
            shell_type=self.shell_type.title(),
            toppings=[topping['name'] for topping in self.toppings],
            is_vegan=self.is_vegan(),
            is_veg=True if self.is_vegan() else self.is_veg()
        )
        return desc

    def is_vegan(self):
        options = Toppings().options
        for key in self.toppings:
            if key['name'] in options[0] or key['diet'] != "VV":
                return False
        return True

    def is_veg(self):
        for key in self.toppings:
            if key['diet'] == "M":
                return False
        return True

toppings = Toppings().options
meat_toppings = toppings[0]
veg_toppings = toppings[1]
pep = Pizza("pepperoni", "wheat", "hand-tossed", 15, 14, [
    meat_toppings['pepperoni'], 
    veg_toppings['shredded mozzarella'], 
    veg_toppings['marinara']
    ])
chz = Pizza("cheese", "garlic", "pan", 15, 14, [
    veg_toppings["shredded mozzarella"], 
    veg_toppings["marinara"]
    ])
v_mona = Pizza("vegan mona lisa", "plain", "thin", 20, 14, [
    veg_toppings["vegan cheese"], 
    veg_toppings["sliced tomato"], 
    veg_toppings["spinach"], 
    veg_toppings["garlic + olive oil"], 
    veg_toppings["artichokes"],
    veg_toppings["bell peppers"]
    ])

if __name__ == '__main__':
    print(pep)
    print()
    print(chz)
    print()
    print(v_mona)