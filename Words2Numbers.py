#-*-coding:utf8;-*-
#qpy:3
#qpy:console

print("THIS IS WORD TRANSLATOR TO NUMBER")
# first we create a dictionary using relevant
# numerical numbers in word form as key and 
# integer form as values
dict_of_numbers = {"zero":0,"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,
"eight":8,"nine":9,"ten":10,"eleven":11,"twelve":12,"thirteen":13,"fourteen":14,
"fifteen":15,"sixteen":16,"seventeen":17,"eighteen":+18,"nineteen":19,"twenty":20,
"thirty":30,"forty":40,"fifty":50,"sixty":60,"seventy":70,"eighty":80,"ninety":90,
"hundred":100,"thousand":1000,"million":1000000,"billion":1000000000,"point":111,"trillion":1000000000000}
# then we define a function that accepts one argument
# and iterates through such argument comparing its with the keys 
# of our dictionary, once an element is found to be the same with a key
# its value is used to increase the value of the variable num
# present in the function, and if it is found to not be equal to any key 
# in the dictionary it passes and iterates on to the next element
lis = []
def number(x):
   num = 0
   num1 = ""
   point = 0
   for i in x:
     if i in dict_of_numbers:
           if dict_of_numbers[i] < 100:# values of keys equal to elements in the dictionary 
              num = num + dict_of_numbers[i]# lesser than 100, are added to the value of the num variable, while
           elif dict_of_numbers[i] == 100:# values of keys greater than or equal to 100 are multiplied with the value of the num variable
              num = num * dict_of_numbers[i]
           elif dict_of_numbers[i] == 111:
              lis.append(num)
              point = 1
              j = x.index(i)
              k = x[(j+1)::]
              for o in k:
                if o in dict_of_numbers:             
                  num1 += str(dict_of_numbers[o])    
                else:
                  pass
           else:
              num = num * dict_of_numbers[i]
              lis.append(num)
              num = 0
     else:
       pass
   j = 0
   if point:
        o = int(num1)
        p = len(num1)
        num = o/10**p
        while j < len(lis):
          num = num + lis[j]
          j = j + 1
   else:
        while j < len(lis):
          num = num + lis[j]
          j = j + 1
   return(num)
# then finally we request for an input and we replace all unwanted characters, turn the string to all lower caps
your_input = (((((input("Write your number in words\n:")).lower()).replace(","," ")).replace("-"," ")).replace("."," "))
# and we split it into a list using (.split(" ")) 
word2number = (your_input).split(" ")
# then we utilize the splited string as the argument in our function and print the function
print(number(word2number))