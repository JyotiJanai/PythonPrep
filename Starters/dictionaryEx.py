# Write a function which takes user details creates dictionary.
from typing import Dict, Union


def dict_fun(first_name: object, last_name: object, age: object, gender: object, address: object) -> object:
    var = {
        "first_name": first_name,
        "last_name": last_name,
        "age": age,
        "gender": gender,
        "address": address
    }

    return var


address: Dict[str, Union[int, str]] = {
    "unit_no": 614,
    "street": "flournoy",
    "city": "chicago",
    "country": "usa",
    "pin": 60656
}
x = dict_fun("abc", "xyz", 17, "male", address)
print(x)
add2 = address.update({"unit_no": 616})
print(add2)
y = dict_fun("aaa", "bbb", 26, "female", address)
print(y)
address["city"] = "new york"
print(y)
for t in address:
    print(t)
for c, d in address.items():
    print(c, d)
print(len(address))
address["street2"] = "East River rd"
print(address)
del address["street2"]
print(address)
j = address.copy()
print(j)
