
with open("life-expectancy.csv") as life_expectancy:
    life_iter = iter(life_expectancy)
    line = next(life_iter)

    year_interest = int(input("Enter the year of interest: "))

    highest = 0.0 
    entity_highest = ""
    year_highest = 0
    lowest = 1000
    entity_lowest = ""
    year_lowest = 0

    interest_highest = 0.0
    interest_entityH = ""
    interest_lowest = 0.0
    interest_entityL = ""

    sum = 0
    numberoftimes = 0

    for line in life_expectancy:
        clean_line = line.strip()
        parts = clean_line.split(",")  
        
        if float(parts[3]) > float(highest): 
            highest = parts[3]
            enitity_highest = parts[0] 
            year_highest = parts[2]
        elif float(parts[3]) < float(lowest):
            lowest = parts[3]
            enitity_lowest = parts[0] 
            year_lowest = parts[2]

        if parts[2] == year_interest:
            if parts[3] > interest_highest:
                interest_highest = parts[3]
                interest_entityH = parts[0]
            elif parts[3] < interest_lowest:
                interest_lowest = parts[3]
                interest_entityL = parts[0]

        if year_interest == parts[3]:
            print(float(parts[3]))
            sum += float(parts[3])
            numberoftimes += 1
        

   # interest_average = sum / numberoftimes

    print(f"The overall max life expectancy is: {highest} from {str(entity_highest)} in {year_highest}")
    print(f"The overall max life expectancy is: {lowest} from {entity_lowest} in {year_lowest}")
    print()
    print(f"For the year: {year_interest}")
    #print(f"The average life expectancy across all countries was {interest_average:.2f}")
    print(f"The max life expectancy was in {interest_entityH} with {interest_highest}")
    print(f"The min life expectancy was in {interest_entityL} with {interest_lowest}")
