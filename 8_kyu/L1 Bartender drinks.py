def get_drink_by_profession(param):
    drinks = {
        "jabroni": "Patron Tequila",
        "school counselor": "Anything with Alcohol",
        "programmer": "Hipster Craft Beer",
        "bike gang member": "Moonshine",
        "politician": "Your tax dollars",
        "rapper": "Cristal",
        "pundit": "Beer",
        "pug": "Beer"
    }

    profession = param.lower()
    return drinks.get(profession, "Beer")