nutrition =[
    {"fruits":"apple","calories":"26"},
    {"fruits":"avocado","calories":"80"},
    {"fruits":"banana" ,  "calories":"44.5"},
    {"fruits":"cantaloupe","calories":"17"},
    {"fruits":"grapefruit","calories":"21"},
    {"fruits":"grapes","calories":"34.5"},
    {"fruits":"honeydew melon","calories":"18"},
    {"fruits":"kiwifruit","calories":"20.5"},
    {"fruits":"lemon","calories":"14.5"},
    {"fruits":"lime","calories":"14.5"},
    {"fruits":"nectarine","calories":"22"},
    {"fruits":"orange","calories":"23.5"},
    {"fruits":"peach","calories":"19.5"},
    {"fruits":"pear","calories":"28.5"},
    {"fruits":"pineaple","calories":"25"},
    {"fruits":"plum","calories":"23"},
    {"fruits":"strawberries","calories":"16"},
    {"fruits":"sweetberries","calories":"18.5"},
    {"fruits":"tangerine","calories":"26.5"},
    {"fruits":"watermelon","calories":"15"}
]
a = input("Item: ")
b = float(input("Serving size: "))
for i in nutrition:
    if i["fruits"] == a.lower():
        print("Calories: ",float(i["calories"])*b/50)
    