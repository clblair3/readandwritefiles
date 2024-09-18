def main():
    #open clients.txt
    file_object = open('clients.txt', 'r')
    count = 0

    for line in file_object:
        count += 1
        line = line.rstrip('\n')
        print(f'{count}. {line}')

    print()
    print(f"Total number of clients: {count}")

main()


