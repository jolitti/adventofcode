with open("example.txt") as file:
    sample_data = file.readlines()
    sample_data = [x.strip() for x in sample_data]
with open("input.txt") as file:
    data = file.readlines()
    data = [x.strip() for x in data]