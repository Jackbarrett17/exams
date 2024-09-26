#Question 1 (a)
#studentname: jack barrett

#length = 6
#width = 4
#length = 7.5 (iii)
#width = 4.7
#length = 7.532
#width = 4.674
length = 7.542
width = 4.876



print("This program can find the perimeter or area of a quadrilateral") #(i)
print("please enter the length:",length) #(iii)
print("please enter the width:",width)  #(iii)
name = input("Please enter your user name: ") #(ii)
choice = input("Do you want to find the(p)erimeter or (a)rea? ") 
if choice == "p":
    print(length + length + width + width)
elif choice == "a":
    print(length*width)
#print("A quadrilateral with a length of",length,"and a width of",width,"has an perimeter of: ",length + length + width + width) #(iv)
print("A quadrilateral with a length of",length,"and a width of",width,"has an area of: ",length*width) #(v)
print("Thank you for using the program",name) #(ii)