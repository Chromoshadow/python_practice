def NULL_not_found(object: any) -> int:
    if object is None:
        print(f"Nothing: {object} <class 'NoneType'>")
    elif object.__class__ is float:
        print(f"Cheese: {object} <class 'float'>")
    elif object.__class__ is int:
        print(f"Zero: {object} <class 'int'>")
    elif object == "":
        print("Empty: <class 'str'>")
    elif object is False:
        print(f"Fake: {object} <class 'bool'>")
    else:
        print("Type not Found")
        return 1
    return 0
