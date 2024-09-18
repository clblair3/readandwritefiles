def main():
    #open a file named philosophers.txt
    outfile = open('philosophers.txt', 'w')


    #write our name to the bottom of the file
    outfile.write("Chasity Blair")


    #close the file
    outfile.close()

#call the main function
main()