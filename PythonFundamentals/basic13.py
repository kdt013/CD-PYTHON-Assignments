# #1. print all integers from 1-225
for i in range(1,256):
    print(i)


# #2. print integers from 0 to 255, and with each integer print the sum so far
#num: 0, sum: 0
#num: 1, sum: 1
#num: 2, sum: 3
#num: 3, sum: 6
sum = 0
for i in range(0,256):
    sum = sum + i # sum += i
    print(f"num: {i}, sum: {sum}")


#3. given an array, find and print its largest element
def largestElement(list):
    max = list[0]
    for i in list:
        if i > max:
            max = i
    print(max)

myList = [4, 9, -1, 0, 0, 14, 9, 8, 19, 100, -43, 98]
largestElement(myList)
myList2 = [4, 9, -1, 0, 0, 14, 945, 8, 19, 100, -43, 98]
largestElement(myList2)
myList3 = [-4, -9, -1, -3]
largestElement(myList3)


#4. create an array with all the odd integers between 1 and 255 (inclusive).
odd = []
for i in range(1,256):
    if i % 2 == 1:
        odd.append(i)
        print(odd)


#5. Given an array and a value Y, count and print the number of array values greater than Y
def greaterValue(list, y):
    count = 0
    for val in list:
        if val > y:
            print(val)
            count += 1
    print(count)

list4 = [4, 9, -1, 0, 0, 14, 9, 8, 19, 100, -43, 98]
greaterValue(list4, 10) 


#6. Given an array, print the max, min and average values for that array
def max_min_avg(list):
    max = list[0]
    min = list[0]
    sum = 0
    avg = 0
    for i in list:
        sum += i
        if i < min:
            min = i
        if i > max:
            max = i
    avg = sum/len(list)
    print(f"max: {max}, min: {min}, avg: {avg}")

myList4 = [4, 9, -1, 0, 0, 14, 9, 8, 19, 100, -43, 98]
max_min_avg(myList4)
myList5 = [4, 9, -1, 0, 0, 14, 945, 8, 19, 100, -43, 98]
max_min_avg(myList5)
myList6 = [-0,10,5,10,5,0]
max_min_avg(myList6)

#7. Replace any negative array values with 'Dojo'
#8. Print all odd integers from 1 to 255.
#9. Iterate through a given array, printing each value
#10. Analyze an array’s values and print the average
#11. Square each value in a given array, returning that same array with changed values
#12. Return the given array, after setting any negative values to zero
#13. Given an array, move all values forward by one index, dropping the first and leaving a '0' value at the end
