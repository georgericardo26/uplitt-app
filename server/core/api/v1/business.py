from typing import List, Tuple


def create_or_get_ingredients(instance, IngredientItem, IngredientChosenToFoodItem, ingredients, virtualshop) -> List:

    new_ingredients = []

    for item in ingredients:

        if not IngredientItem.objects.filter(
                name=item["name"],
                virtualshop__pk=virtualshop.pk).exists():

            ingredient = IngredientItem(
                name=item["name"],
                details=item.get("detail"),
                virtualshop=virtualshop
            )

            ingredient.full_clean()
            ingredient.save()
            new_ingredients.append(ingredient)
        else:
            ingredient = IngredientItem.objects.get(
                name=item["name"],
                virtualshop__pk=virtualshop.pk)
            new_ingredients.append(ingredient)

    return new_ingredients


def calculate_distance_haversine(lat_long_1: Tuple[float, float], lat_long_2: Tuple[float, float]) -> float:
    from math import sin, cos, sqrt, atan2, radians

    # approximate radius of earth in km
    R = 6373.0

    lat1 = radians(lat_long_1[0])
    lon1 = radians(lat_long_1[1])
    lat2 = radians(lat_long_2[0])
    lon2 = radians(lat_long_2[1])

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c

    return round(distance, 1)


def calculate_distance_vincenty(lat_long_1: Tuple[float, float], lat_long_2: Tuple[float, float]) -> float:
    import geopy.distance

    coords_1 = (lat_long_1[0], lat_long_1[1])
    coords_2 = (lat_long_2[0], lat_long_2[1])

    return round(geopy.distance.distance(coords_1, coords_2).miles, 1)
