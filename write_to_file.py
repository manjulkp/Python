look_up = input("what software do you want to look for")

found = False
with open('manjula.txt' , encoding='utf-8') as fi:
    for line in fi:
        if look_up in line:
            print(line)
            found = True
            break
        
if not found:
    print('The language is not practiced')