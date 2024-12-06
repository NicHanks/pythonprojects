hr_system = open("w11.teamactivity/hr_system.txt")

for line in hr_system:
    parts = line.split(" ")
    name = parts[0]
    id_number = parts[1]
    job_title = parts[2]
    salary = float(parts[3])
    if parts[2].lower() == "engineer":
        salary += 1000
    pay_check = salary/24
    print(f"{name} (ID: {id_number}), {job_title} - ${pay_check:.2f}")