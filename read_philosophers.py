def main():

    #open a file named philosophers.txt
    infile = open('philosophers.txt', 'r')

    #read the file's contents
    #file_contents = infile.read()
    line1 = infile.readline().rstrip("\n")
    line2 = infile.readline().rstrip("\n")
    line3 = infile.readline().rstrip("\n")



    #print the data that was read into memory
    #print(file_contents)
    print(line1)
    print(line2)
    print(line3)

#call the main function
main()