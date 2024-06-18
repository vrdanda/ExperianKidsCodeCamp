# Writing content to a file
jokes_file = open("./favorite_jokes.txt", "w")  # "w" Open for writing
jokes_file.write("Why did the chicken cross the road? To get to the other side!\n")
jokes_file.close()