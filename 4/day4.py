


with open('input') as f:
    scans = f.read().replace("\n"," ").split("  ")


def gen_passport():
    passport = {}
    passport_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
    for field in passport_fields:
        passport[field] = None
    return passport


print("Puzzle 1")
passports = []
valid_passports = 0

for scan in scans:
    fields = scan.split()
    passport = gen_passport()
    for field in fields:
        key, value = field.split(":")
        passport[key] = value
    if list(passport.values()).count(None) == 0 or (list(passport.values()).count(None) == 1 and passport["cid"] is None):
        valid_passports += 1
        # print(passport)
    passports.append(passport)

print(valid_passports)

print("Puzzle 2")
def is_valid_passport(passport):
    if not(list(passport.values()).count(None) == 0 or (list(passport.values()).count(None) == 1 and passport["cid"] is None)):
        return False

    if not(1920 <= int(passport["byr"]) <= 2002):
        return False
    
    if not(2010 <= int(passport["iyr"]) <= 2020):
        return False

    if not(2020 <= int(passport["eyr"]) <= 2030):
        return False

    height = passport["hgt"][:-2]
    metric = passport["hgt"][-2:]
    if metric == "cm":
        if not(150 <= int(height) <= 193):
            return False
    elif metric == "in":
        if not(59 <= int(height) <= 76):
            return False
    else:
        return False
    
    if not(passport["hcl"][0] == "#" and [p for p in passport["hcl"][1:] if p in "1234567890abcdef"]):
        return False
    
    if not(passport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]):
        return False
    
    try:
        if len(passport["pid"]) == 9:
            int(passport["pid"])
            return True
    except ValueError:
        return False
    return False



passports = []
valid_passports = 0

for scan in scans:
    fields = scan.split()
    passport = gen_passport()
    for field in fields:
        key, value = field.split(":")
        passport[key] = value
    if is_valid_passport(passport):
        valid_passports += 1
        # print(passport)
    passports.append(passport)
print(valid_passports)







