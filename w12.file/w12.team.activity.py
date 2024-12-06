with open("w12books_and_chapters.txt") as scriptures:
    largest = -1
    for line in scriptures:
        line = line.strip()
        line = line.split(":")
        if int(line[1]) > largest:
            largest = int(line[1])
            largest_book = line[0]
        
        print(f"Scripture: {line[2]}, Book: {line[0]}, Chapter: {line[1]}")
    print(f"The largest book is in {largest_book} with {largest} chapters!")