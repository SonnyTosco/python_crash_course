def count_words(filename):
    """Count the approximate numnber of words in a file"""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
        # msg = "Sorry, the file " + filename + " does not exist."
        # print(msg)
    else:
        #Count the approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")

filenames = ['alice.txt', 'siddharthat.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)
