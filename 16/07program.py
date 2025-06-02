import json

with open("01student.json", "r") as file:
    data = json.load(file)

data["age"] += 1  # increase age by 1
data["grade"].append("two") # add a new subject 

with open("01student.json", "w") as file:
    json.dump(data, file, indent=4)

print("data updated succesfully")
