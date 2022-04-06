import datetime


def directory_path(instance, filename):
    # file will be uploaded to static / images /virtualShop or foodItems/<filename>

    path = "static/images/"
    dt = datetime.datetime.now().isoformat(timespec='microseconds')

    virtualshop = getattr(instance, "virtualShop", None)
    fooditem = instance.foodItems.all() or None

    # todo: We need create a way to get the file type and insert in their proper directory
    if virtualshop:
        path += "virtualshop"

    if fooditem:
        path += "foodItem"

    else:
        path += "others"

    return '{0}/{1}{2}'.format(path, dt, filename)
