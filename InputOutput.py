line = ''
with open("InputOutput.txt", 'r') as input_output:
    line = input_output.read()
    
arr = line.split('\n')
ver = []
hor = []
for i in range(0, 9):
    start = 0
    count = 0
    for j in range(0, 9):
        line = arr[i]
        symbol = line[j]
        if arr[i][j] == '-' and count == 0:
            start = j
            count = 1
        elif arr[i][j] == '-' and count != 0:
            count += 1
        elif arr[i][j] == '+' and count != 0:
            break

    if start != start + count - 1 and start < start + count - 1:    
        hor.append((start, start+count-1))    

for i in range(0, 9):
    start = 0
    count = 0
    for j in range(0, 9):
        symbol = arr[j][i]
        if arr[j][i] == '-' and count == 0:
            start = i
            count = 1
        elif arr[j][i] == '-' and count != 0:
            count += 1
        elif arr[j][i] == '+' and count != 0:
            break

    if start != start + count - 1 and start < start + count -1 :    
        ver.append((start, start+count-1))    

print(ver)
print(hor)