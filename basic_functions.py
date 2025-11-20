

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def fizz_buzz(number):
     if number % 5 == 0 and number % 3 == 0:
        return "FizzBuzz"
     elif number % 3 == 0:
         return "Fizz"
     elif number % 5 == 0:
         return "Buzz"
     else:
         return number
         

def fibonacci(n):
    fib= 0
    num= 1
    p_h= 0
    f_h=0
    for _ in range(n):
        fib=num + p_h
        p_h=fib
    



def triangle(n):
    tr_ls=[]
    num=0
    for i in range(1,n+1):
        try:
            p_h=('*'*i) + tr_ls[-1]
        except IndexError:
            tr_ls.append('*')
        if num > 0:   
            tr_ls.append(p_h)
        num+=1

    return tr_ls
        


def return_list_stats(numbers):
    """Given the list 'numbers', use the relevant functions to return a
        dictionary of statics for the list. This dictionary must have
        the following keys:
            unique_numbers : a set containing unique numbers from the list 'numbers',
            max : largest number in the list 'numbers',
            min : smallest number in the list 'numbers',
            average : average of the numbers in the list 'numbers',
            even_pairs : a list of tuples that have neighboring pairs 
                that sum up to an even number in the list 'numbers',
            odd_pairs : a list of tuples that have neighboring pairs 
                that sum up to an even number in the list 'numbers',
            even_numbers : a tuple of all the even numbers in the list
                'numbers',
            odd_numbers : a tuple of all the odd numbers in the list 
                'numbers',
            number_of_even_numbers : the total number of even numbers in the 
                list 'numbers',
            number_of_odd_numbers : the total number of even numbers in the list
                 'numbers'
    """
    statics = {'unique_numbers': set(num for num in numbers),
                'max': max(numbers),
                'min': min(numbers),
                'average':float(sum(numbers)/numbers),
                'even_pairs': [(numbers[i], numbers[i+1]) for i in range(0, len(numbers)-1) if (numbers[i] + numbers[i+1]) % 2 == 0],
                'odd_pairs': [(numbers[i], numbers[i+1]) for i in range(0, len(numbers)-1) if (numbers[i] + numbers[i+1]) % 3 == 0],
                'even_numbers': (i for i in numbers if i % 2 == 0),
                'odd_numbers' : (i for i in numbers if i % 3 == 0 or i == 1),
                'number_of_even_numbers': sum([i for i in numbers if i % 2 == 0]),
                'number_of_odd_numbers': sum([i for i in numbers if i % 3 == 0 or i == 1]),
                }
    # #odd_pairs
    # for i in range(0, len(numbers)-1):
    #     if (numbers[i] + numbers[i+1]) % 3 == 0:


    return statics

# TODO: (Bonus) Implement the pascal_triangle function below
def pascal_triangle(n):
    """
    Generates Pascal's triangle and returns the final row as a list.

    Parameters:
    n (int): The row number of Pascal's triangle to generate (0-based index).

    Returns:
    list: The final row of Pascal's triangle as a list.

    Formula for Pascal's Triangle:
    Each element in Pascal's triangle can be calculated using the following formula:

    C(n, k) = n! / (k! * (n-k)!)

    Where:
    - n is the row number (0-based index)
    - k is the column number (0-based index)
    - C(n, k) represents the value at row n and column k in Pascal's triangle
    - n! represents the factorial of n

    To generate a row of Pascal's triangle, iterate over the columns from 0 to n.
    Calculate each element using the formula and store them in a list to form the row.
    Repeat this process for each row up to the desired row number.

    Example:
     * Input: n = 6
     * Output:
     *           1
     *         1   1
     *       1   2   1
     *     1   3   3   1
     *   1   4   6   4   1
     * 1   5  10   10  5   1
    """
    pass

#triangle(3)
fibonacci(4)
