# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
phoneBook = dict()
for _ in range(n):
    name, phone = input().split()
    phoneBook[name] = phone

query = input() 
while(len(query)>0):
    if query in phoneBook:
        print(query + '=' + phoneBook[query])
    else:
        print('Not found')
    query = input()

