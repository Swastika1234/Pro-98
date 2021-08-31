def countWords():
    fileName=input("Enter the file name: ")
    count=0
    file=open(fileName,'r')
    for line in file:
        words=line.split()
        count+=len(words)
    print("Number of words= ")
    print(count)


countWords()