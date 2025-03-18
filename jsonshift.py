import json
import datetime

print("Would you like to limit results to shifts to before and including today?(Y/N)")
userInput = input()

shifts = {}

with open("shifts.json", "r") as f:
    data = json.load(f)
    f.close

semArray = data["studentCohortShifts"]

for sem in semArray:
    for shift in semArray[sem]:
        if userInput.lower() == "y": 
            shiftDate = datetime.datetime.strptime(shift, "%Y-%m-%dT%H:%M:%S.%fZ")
            if shiftDate > datetime.datetime.today() : continue
        shiftName = semArray[sem][shift][0]["type"]["name"]
        if shiftName not in shifts:
            shifts[shiftName] = 1
        else:
            shifts[shiftName] += 1

for key in shifts.keys():
    print(f"{key}: {shifts[key]}")

print("Do you want to save the output?(Y/N)")
userInput = input()

if userInput.lower() == "y":
    with open("output.txt", "w") as f:
        for key in shifts.keys():
            f.write(f"{ key }: { shifts[key] }\n")
        f.close
        print("Output saved")
else:
    exit()