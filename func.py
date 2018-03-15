def min(*args, **kwargs):
    if not args:
        raise ValueError
    if kwargs:
        key = kwargs.get('key')
    else:
        key = lambda x: x
    if len(args)>1:
        iter_el = [arg for arg in args]
    else:
        iter_el = args[0]
    minim = None
    for el in iter_el:
        if not minim:
            minim = el
        if key(minim) <= key(el):
            continue
        else:
            minim = el
    return minim


def max(*args, **kwargs):
    if not args:
        raise ValueError
    key = kwargs.get('key')
    if len(args)>1:
        iter_el = [arg for arg in args]
    else:
        iter_el = args[0]
    result = None
    for el in iter_el:
        if not result:
            result = el
        if kwargs:
            if key(result) >= key(el):
                continue
            else:
                result = el
        else:
            if result >= el:
                continue
            else:
                result = el
    return result


