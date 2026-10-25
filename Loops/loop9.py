#find the duplicate in string
items = ['Apple', 'banna','orange','Apple','mango']

unique_item = set(items)

for item in items:
    if item in unique_item:
        print("duplicate",item)
        break
print(unique_item);
