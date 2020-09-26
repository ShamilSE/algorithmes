print ("Enter size of array")
N = int(input())
array = [0] * N
for k in range(0, N, 1):
    print ("Enter " + str(k + 1) + " element of array")
    array[k] = input()
print (array)