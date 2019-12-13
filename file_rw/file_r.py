def create_cast_list(filename):
    cast_list = []
    with open(filename,"r") as f:
        lines = f.readlines()
    for line in lines:
        line_split = line.split(",")
        cast_list += [line_split[0]]

    return cast_list

cast_list = create_cast_list('flying_circus_cast.txt')
for actor in cast_list:
    print(actor)