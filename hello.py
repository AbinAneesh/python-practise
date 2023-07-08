number = int(input("plese enter a number "))
fizzbuzz = []
if number % 5 ==0 and number % 3== 0 :
    fizzbuzz.append("fizzbuzz")
elif number % 5== 0 :
    fizzbuzz.append("buzz")    
elif number % 3 ==0:
    fizzbuzz.append("fizz")    
else :
    fizzbuzz.append(number)    


print (fizzbuzz)
