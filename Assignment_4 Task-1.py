try:
    print("Reading content: ")
    file = open('sample.txt','r')
    lines = file.readlines()  # Read all lines into a list
    for i in range(1,4):
        if i <= len(lines):
          print("Line",i,": ",lines[i-1],end='')
    file.close()
except FileNotFoundError:
    print("The file 'sample.txt' was not found.")