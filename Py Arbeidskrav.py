#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 10:14:39 2024

@author: anders

@group: 127
"""

login = {"PGR107": "Python"}



def login_info(login):

    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
  
    while login.get(username) != password:
        print("Invalid username and/or password.")
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")
    
    print("Lets go!")
    


    
def main():
    CorrectAnswers = 0
    WrongAnswers = 0
    FailedQuestions = []
    
    
    #login_info(login)

#Question 1
    print("What is the capital of Norway?")
    print("a, Bergen")
    print("b, Oslo")
    print("c, Stavanger")
    print("d, Trondheim")
    q1Answer = input("Please enter your answer: ")
    if q1Answer.lower() == "b":
        CorrectAnswers = CorrectAnswers + 1
    else:
        WrongAnswers = WrongAnswers + 1
#Question 1
    print("What is the currency of Norway?")
    print("a, Euro")
    print("b, Pound")
    print("c, Krone")
    print("d, Deutsche Mark")
    q2Answer = input("Please enter your answer: ")
    if q2Answer.lower() == "c":
        CorrectAnswers = CorrectAnswers + 1
    else:
        WrongAnswers = WrongAnswers + 1        
#Question 1
    print("What is the largest city in Norway?")
    print("a, Oslo")
    print("b, Stavanger")
    print("c, Bergen")
    print("d, Trondheim")
    q3Answer = input("Please enter your answer: ")
    if q3Answer.lower() == "a":
        CorrectAnswers = CorrectAnswers + 1
    else:
        WrongAnswers = WrongAnswers + 1      
        
        
        
        
        
    print("Correct answers:", CorrectAnswers)
    print("Wrong answers:", WrongAnswers)


main() 