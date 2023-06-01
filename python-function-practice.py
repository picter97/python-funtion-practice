def max_numbers(a,b,c):
    return max([a,b,c])

print(max_numbers(2,3,4))

def mult_list(*numbers):
    result = 1
    for num in numbers:
        result *= num
    return result
result = mult_list(1,2,3)
print(result)

def rev_string(string):
    output = string[::-1]
    return output

print(rev_string("hola"))

def num_within(x,a,b):
  return x in range(a,b+1)
     
print(num_within(3,2,4))  
print(num_within(10, 2, 5))

def pascal(n):
    triangle = []

    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                prev_row = triangle[i - 1]
                value = prev_row[j - 1] + prev_row[j]
                row.append(value)

        triangle.append(row)

    for row in triangle:
        for num in row:
            print(num, end=' ')
        print()

pascal(5)
                                                    