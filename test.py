def strong_code_validator(numbers):
    try:
        numbers = [int(d) for d in numbers]
    except ValueError:
        print("Invalid input kindly enter a digit ")
        return False
    def unique_digit(numbers):
        seen = set()
        are_unique = True
        for num in numbers:
            if num in seen:
                are_unique = False
                break
            seen.add(num)
        return are_unique
    def middle_rule(numbers):
         if len(numbers) % 2 == 0:
             len_first = len(numbers)//2
             len_sec = len(numbers)//2 - 1
             first_num = numbers[len_sec]
             middle_num = numbers[len_first]
             sum = middle_num + first_num
             if sum > 4:
                 return True
             else:
                 return False
         else:
               mid_index = len(numbers)//2
               mid_num = numbers[mid_index]
               if mid_num > 4:
                   return True
               return None 
    def even_odd(numbers):
           for i in range(len(numbers) - 1):
                    if numbers[i] % 2 == 0 and numbers[i+1] % 2 == 0:
                        return False
                    elif numbers[i] % 2 != 0 and numbers[i+1] % 2 != 0:
                        return False
           return True
    def prime_test(numbers):
              primes = {2,3,5,7}
              return numbers[0] in primes and numbers[-1] in primes
                 
                 
    if not unique_digit(numbers):
          print("Error: All digits must be unique")
          return False
    if not middle_rule(numbers):
        print("Error: Middle digit must be greater than 4 if odd\n If even averaof the middle digit must be greater than 4")
        return False
    if not prime_test(numbers):
                  print("Error: First and last digit must be prime number")
                  return False
    if not even_odd(numbers):
                  print("Error: Consecutive digit must be odd and even")
                  return False
    print("Success")
    print("All checks passed")
    return True
    
    
while True:
         numbers = input("Enter your numbers")
         print(strong_code_validator(numbers))
         
         
                
                  
                  
                  
      
                  
                  
              
              
              