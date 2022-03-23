import math
import random

def quitprogram():
    exit()

def randomG():
    tryLoop = 1
    x = 1
    while tryLoop == 1:
        try:
            highestnum = int(input("What is the range for your Random Number Generator? 1-(?) "))
            numofrandom = int(input("How many random numbers do you want? "))
        except:
            print("Sorry, that is not a number. Please try again. ")
        for x in range(numofrandom):
                random1 = [random.randint(1,highestnum)]
                print("Your random number is:",random1)
        leave = input("Would you like to return to the main menu? Y/N ")
        if leave == "y":
            return menu()

def roots():
    tryLoop = 1
    while tryLoop == 1:
        try:
            num = float(input("Enter a number: "))
            sqrt = math.sqrt(num)
            print("Square Root: ", sqrt, "\n")
           
        except:
            print("Sorry, that is not a number. Please try again. ")
        leave = input("Would you like to return to the main menu? Y/N ")
        if leave == "y":
            return menu()

def exponent():
    tryLoop = 1
    while tryLoop ==1:
        try:
            x = 0
            power = int(input("Enter the power: "))
            base = int(input("Enter the base: "))
            finalans = base**power
            print(finalans)
        except:
            print("Sorry, that is not a number. Please try again. ")
        leave = input("Would you like to return to the main menu? Y/N ")
        if leave == "y":
            return menu()

def division():
    tryLoop = 1
    while tryLoop == 1:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            division = num1 / num2
            print('{} / {}'.format(num1, num2))
            print (num1 / num2,"\n")
        except:
            print("Sorry, that is not a number. Please try again. ")
        leave = input("Would you like to return to the main menu? Y/N ")
        if leave == "Y" or  leave == "y":
            return menu()
            
def multiplication():
    tryLoop = 1
    while tryLoop == 1:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            multiplication = num1 * num2
            print('{} * {}'.format(num1, num2))
            print (num1 * num2, "\n")
        except:
            print("Sorry, that is not a number. Please try again. ")
        leave = input("Would you like to return to the main menu? Y/N ")
        if leave == "Y" or  leave =="y":
            return menu()

def subtraction():
    tryLoop = 1
    while tryLoop == 1:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            subtraction = num1 - num2
            print('{} - {}'.format(num1, num2))
            print (num1 - num2,"\n")
        except:
            print("Sorry, that is not a number. Please try again. ")
        leave = input("Would you like to return to the main menu? Y/N ")
        if leave == "Y" or  leave =="y":
            return menu()


def addition():
    tryLoop = 1
    while tryLoop == 1:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            addition = num1 + num2
            print('{} + {}'.format(num1, num2))
            print (num1 + num2, "\n")
        except:
            print("Sorry, that is not a number. Please try again. \n ")
        leave= input("Would you like to return to the main menu? Y/N ")
        if leave == "Y" or  leave =="y":
            return menu()
        
            
def main():
    name = input("Hi there, what is your name?")
    print("Hello there " + name + "\nhow may I assist you today?" )
    menu()

def menu():
    while True:
        print("Press #1: Addition \n")
        print("Press #2: Subtraction \n")
        print("Press #3: Multiplication \n")
        print("Press #4: Division \n")
        print("Press #5: Exponent \n")
        print("Press #6: Roots \n")
        print("Press #7: Random Number Generator \n")
        print("Press q: Quit \n")
        inpt = input("--- Enter 1 2 3 4 5 6 7 --- \n    Exit? Press q \n").lower()
        if inpt == ("q"):
            quitprogram()
        if inpt == "1":
            addition()
        elif inpt =="2":
            subtraction()
        elif inpt =="3":
            multiplication()
        elif inpt =="4":
            division()
        elif inpt =="5":
            exponent()
        elif inpt == "6":
            roots()
        elif inpt == "7":
            randomG()
        elif inpt == "q":
            quitprogram()
        else:
            print("Please try again. \n \n")
            continue
main()