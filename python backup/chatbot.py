def greet(bot_name, birth_year):
    print("Hello my name is {0}.".format(bot_name))
    print("I created in {0}.".format(birth_year))

def remind_name():
    print('Please,remind me your name.')
    name = input()
    print("what a great name you have.{0}!".format(name))

def guess_age():
    print('let me guess your age')
    print('enter reminders of dividing your age by 3,5 and 7')
    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105
    print("your age is {0};thats good time to start the programming".format(age))

def count():
    print('now i will prove to you that i can count to any number you want')
    num = int(input())
    counter = 0
    while counter <= num:
        print("{0}!".format(counter))
        counter += 1

def test():
    print("lets test your programming knowledge")
    print("why do you use method")
    print("1.to repeat a statement multiple time ")
    print("2.to decompose a program into several subroutines")
    print("3.to determine the execution time of the program")
    print("4.to interupt execution of a program")
    answer = 2
    guess = int(input())
    while guess != answer:
        print("please try again later")
        guess = int(input())
        print("completed you have a nice day! ")

def end():
    print("congratulations have a nice day! ")
    greet('Sbot', '2021')
    remind_name()
    
guess_age()
count()
test()
end()
