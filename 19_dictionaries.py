
months = {1: "January", 2: "February", 3: "March"}

person = {"name": "Alice", "age": 30, "city": "New York"}

print(person["name"])            # Alice
print(person.get("age"))        # 30

# add / update
person["email"] = "alice@example.com"
person["age"] = 31

# remove and show
removed = person.pop("city")
print("removed:", removed)

for k, v in person.items():
    print(k, "->", v)

print(list(person.keys()))

people = {"bob": {"age": 25, "city": "LA"}}
print(people["bob"]["city"])    # LA

