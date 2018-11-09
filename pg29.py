def EvenOddSum(a, n):
    even = 0
    odd = 0
    avg_even = 0
    avg_odd = 0
    count_odd = 0
    count_even = 0
    for i in range(n):
        if i % 2 == 0:
            even += a[i]
            count_even+=1
            avg_even = even/count_even
        else:
            odd += a[i]
            count_odd+=1
            avg_odd = odd/count_odd
     
    print ("Even index positions sum ", even)
    print ("nOdd index positions sum ", odd)
    print("Number of even numbers :",count_even)
    print("Number of odd numbers :",count_odd)
    print("Average of even numbers :",avg_even)
    print("Average of odd numbers :",avg_odd)
arr = [1, 2, 3, 4, 5, 6]
n = len(arr)
EvenOddSum(arr, n)
