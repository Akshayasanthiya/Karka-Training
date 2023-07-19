# file=open("/home/akshaya/Documents/name.txt",'r')
# # print(file.readlines(5))
# for line in file:
#     print(line)

# file=open("/home/akshaya/Documents/name.txt",'w')
# file.write("Achu\n")
# file.write("My name is Akshaya")
# file.close()
# file=open("/home/akshaya/Documents/name.txt",'r')
# for line in file:
#     print(line)

# file=open("/home/akshaya/Documents/name.txt",'a')
# file.write("\nI am B.Sc Graduate.")
# file.close()
file=open("/home/akshaya/Documents/name.txt",'r')
for line in file:
    print(line.split())
