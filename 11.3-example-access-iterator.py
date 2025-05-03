categories = {
    "Id": 1,
    "name": "mobiles",
    "subCategories": {
        "samsung": [
            {
                "id": 50,
                "name": "NOTE 10",
                "prices": [5000, 6000],
                "madeIn": ["china", "germany"],
                "colors": {"primary": "black", "secondaryColors": ["red", "blue"]},
            },
            {
                "id": 60,
                "name": "S20",
                "prices": [7000, 8000],
                "madeIn": ["china", "germany"],
                "colors": {"primary": "white", "secondaryColors": ["brown", "orange"]},
            },
        ],
        "apple": [
            {
                "id": 70,
                "name": "Iphone X",
                "prices": 20000,
                "madeIn": {"counrty": "china"},
                "colors": ["red", "green", "black"],
            },
            {
                "id": 80,
                "name": "Iphone 12",
                "prices": 60000,
                "madeIn": {"counrty": "china"},
                "colors": [{"primary": "black"}, {"secondaryColors": ["red", "blue"]}],
            },
        ],
        "oppo": [
            {
                "id": 90,
                "name": "Oppo F1",
                "prices": [],
                "madeIn": [],
                "colors": [],
            },
            {
                "id": 100,
                "name": "Oppo F2",
                "prices": [],
                "madeIn": [],
                "colors": [],
            },
            {
                "id": 101,
                "name": "Oppo F2",
                "prices": [],
                "madeIn": [],
                "colors": [],
            },
        ],
    },
}


# NOTE10
# germany
# blue
# primary
# orange

# print(categories['subCategories']['samsung'][0]['name'])
# print(categories['subCategories']['samsung'][1]['madeIn'][1])
# print(categories['subCategories']['apple'][1]['colors'][1]['secondaryColors'][1])
