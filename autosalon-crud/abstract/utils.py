# Если существуют несколько объектов с одинаковыми значениями выбранного аттрибута, то функция возвращает список из этих объектов
# Если нет, функция возвращает один объект
def get_obj_or_404(model, attr, val):
    found = False

    counter = 0
    obj_list = []
    for obj in model.objects:
        obj_val = getattr(obj, attr)
        if obj_val == val:
            found = True
            counter += 1
            obj_list.append(obj)
            found_object = obj

    if not found:
        raise Exception(f"404: model {model.__name__} not found")

    if counter > 1:
        return obj_list
    elif counter == 1:
        return found_object

def login_required(obj):
    if not obj.is_authenticated:
        raise Exception("Юзер не авторизирован")