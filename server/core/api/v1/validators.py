from rest_framework import serializers


def duplicated_name_to_ingredient_item_validator(value):
    names = []

    for item in value["ingredients"]:
        if item["name"] not in names:
            names.append(item["name"])
        else:
            raise serializers.ValidationError("Duplicated key value %s" % (item["name"]))

