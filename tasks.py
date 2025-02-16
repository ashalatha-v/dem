"""1.
print(f"2 + 2 = {(2 + 2)}")

2.

bill=47.28
tip=(bill*15)/100
print(tip)

total=bill+tip
print(total)

share=(total)/2
print(share)

#print("Each person needs to pay:"+share)#TypeError: can only concatenate str (not "float") to str
print(f"Each person needs to pay:{share:.2f}")

3.

numerator = 10
denominator = 10
result = numerator / denominator
print(result)

4.

word1 = "How"
word2 = "do"
word3 = "you"
word4 = "like"
word5 = "Python"
word6 = "so"
word7 = "far?"

print(word1+" "+word2+" "+word3+" "+word4+" "+word5+" "+word6+" "+word7)

#or
first_word="word"
for i in range(1,8):
    #first_word+str(i) gives word1 to get word1 value we need to ue eval(word1)
    together=eval(first_word+str(i))
    res=" ".join(together)

5.
provide a discount for the bus ticket based on price and number of people.
ex:
price=int(input("enter price"))
qty=int(input("enter quantity"))
then calculate total price and provide a discounts 
applicable 10% discount on amount exceeding 10000, 
5% discount on amount between 5,000 to 10,000,
2% discount on amount between 2,000 and 5000,
and 1% for  between 1000 and 2000  respectively. 
No discount is applicable for amount less than 1000.


price=int(input("enter price"))
qty=int(input("enter quantity"))
total_price=price*qty
print(total_price)
if(total_price<1000):
    print("No discount is applicable for amount less than 1000.")
elif 1000<=total_price<=2000:
    discount=1/100
    final_price=total_price-discount
    print(f"amount to be paid after discount:{final_price}")
elif 2000<total_price<=5000:
    discount=2/100
    final_price=total_price-discount
    print(f"amount to be paid after discount:{final_price}")
elif 5000<total_price<=10000:
    discount=5/100
    final_price=total_price-discount
    print(f"amount to be paid after discount:{final_price}")
else:
    discount=10/100
    final_price=total_price-discount
    print(f"amount to be paid after discount:{final_price}")



5)Try below code with Menu- Driven- program

WELCOME TO CALCULATOR

Choose the operation to perform:
1. Addition of two numbers
2. Subtraction of two numbers
3. Multiplication of two numbers
4. Division of two numbers

Enter your Choice: 1
Addition of two numbers
Enter the first number: 
Enter the second number:

"""
def add(a,b):
    sum=a+b
    print(sum)
    return sum
def sub(a,b):
    sub=a-b
    return sub
def multiply(a,b):
    mul=a*b
    return mul
def div(a,b):
    if b!=0:
        div=a/b
        return div
    else:
        print("divide by zero error")
    
def menu():
    print("welcome to calculator")
    print("please choose the option")
    print("choose the operation to perform\n 1.addition of two numbers\n 3.multi of two numbers\n 4.division of two numbers \n 5.exit")


def main():
    while True:
        menu()
        choice=input("enter the choice(1-5): ")
        if choice.isdigit():
            choice=int(choice)
        if choice==5:
            print("good bye")
            break
        elif choice in [1,2,3,4]:
            first_num=float(input("enter the first number: "))
            second_num=float(input("enter the secoond number:"))
            if choice==1:
                print(f"addition of 2 numbers: {add(first_num,second_num)}\n ")
                continue
            elif choice==2:
                print(f"subtraction of 2 numbers: {sub(first_num,second_num)}\n")
                continue
            if choice==3:
                print(f"multiplication of 2 numbers: {multiply(first_num,second_num)}\n")
                continue
            if choice==4:
                print(f"division of 2 numbers: {div(first_num,second_num)}\n")
                continue
        else:
            print("invalid input")
            continue

if __name__=="__main__":
    main()










