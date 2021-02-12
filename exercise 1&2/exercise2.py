# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 18:47:02 2021

Exercise 2: Grade Evaluator

@author: Daniel Broderick
"""

import random
import math

class student:
    def __init__(self, name, effort, luck, charisma, IQ, description):
        self.name = name # a string
        # 5 possible values: .6, .7, .8, .9, 1
        self.effort = effort 
        self.luck = luck # 1 or -1
        # 5 possible values: .8, .85, .9, .95, 1
        self.charisma = charisma
        # converted into a probabilitY
        self.IQ = IQ 
        self.description = description
    
    def output(self): # for testing
        print(self.name)
        print(self.effort)
        print(self.luck)
        print(self.charisma)
        print(self.IQ)
    
    


def main(s1=None,s2=None,s3=None,s4=None,s5=None):
    """ arguments are for testing via exercise3 
    big function, gathers all the input and does some pre-processing
    """
    statement = '' # string to store inputs prior to conversion
    ##### name #####
    if s1 == None: # if we're running this script from exercise3,
                    # this statement will be skipped, easier than 
                    # simulating user input
        s1 = input("What is the student's name? ")
    statement += s1
    
    ##### effort ####
    options2 = ['non-existent', 'poor', 'sufficent', 'good', 'excellent']
    for i in range(5): # display the options
        print(str(i+1) + ":", options2[i])
    
    if s2 == None:
        while True: # loop until we get valid input
            s2 = input(f"How would you rate {s1}'s effort? ")
            if s2 in ['1','2','3','4','5']:
                break
            else:
                print("I don't understand. Please enter a number 1 through 5. ")
                continue
        
    statement += f"'s effort is {options2[int(s2)-1]}. "
    # convert the value
    if s2 in ['1','2','3','4','5']: # if you provide a number
        s2 = .6 + ((int(s2)-1)*.1)
    elif s2.lower() in options2: # in case you write the string
        s2 = .6 + (options2.index(s2.lower())*.1)
    
    #### luck ####
    if s3 == None:
        while True:
            s3 = input("Is {s1} lucky? (y/n): ")
            if s3.lower() in ('y','n','yes','no'):
                break
            else:
                print("I don't understand. Please enter 'y' or 'n': ")
                continue
    
    # convert the value
    if s3.lower() in ('y', 'yes'):
        s3 = 1
    elif s3.lower() in ('n', 'no'):
        s3 = -1
        
    statement += f"They {'are' if s3>0 else 'are not'} lucky. "
    
    ##### charisma #####
    # similar code as effort, different options and final values 
    print(f"Is {s1} charismatic? \n")
    options4 = ['like a block of wood', 
                'not really', "they're nice enough", 
                'definitely', 
                'It makes my day when they join the zoom']
    for i in range(5): # display the options
        print(str(i+1) + ":", options4[i])
    
    if s4 == None:
        while True: # loop until we get valid input
            s4 = input("Enter a number 1 through 5: ")
            if s4 in ['1','2','3','4','5']:
                break
            else:
                print("I don't understand.")
                continue
    
    statement+= f'For charisma, you said "{options4[int(s4)-1]}". '
    # convert the value
    if int(s4) in range(1,6): # if you provide a number
        s4 = round(.8 + ((int(s4)-1)*.05), 2)
    elif s4.lower() in options4: # in case you write the string
        s4 = round(.8 + (options4.index(s4.lower())*.05), 2)
    
    #### IQ #####
    print("What is {s1}'s IQ?\n")
    if s5 == None:
        while True: # verify the input
            s5 = input("Enter a value 45-155: ")
            if 45<=int(s5)<=155:
                break
            else:
                continue
    statement += f"Their IQ is {s5}."
    
    # conversion of the IQ value 
    if int(s5) >= 130: 
        s5 = 1
    elif int(s5) < 70:
        s5 = .2
    elif 70 <= int(s5) <85:
        s5 =.5
    elif 85 <= int(s5) < 100:
        s5 =.7
    elif 100 <= int(s5) < 115:
        s5 = .8
    elif 115 <= int(s5) < 130:
        s5 = .9
    
    
    
    #make the student 
    stud = student(s1,s2,s3,s4,s5,statement)
    
    score_ex = exercises_score(stud)
    score_test = test_score(stud)
    grade = letter_grade(score_ex, score_test)
    
    print(statement)
    print(f'{s1} got a {score_ex} on the the exercises and a {score_test} '+
          f'on the test. Grade in this class: {grade}')
    
    return {'student': stud, 
            'exercises': score_ex,
            'test' : score_test,
            'grade' : grade} 
    # makes passing everything to exercise 3 easier
    
    

def exercises_score(std):
    """Calculate the exercises score
    """  
    exercises = [None] *10
    # because we have 10 exercises
    for indx in range(10):
        pt1 = [None] *10 
        pt2 = [None] *10
        #10pts for each exercise, simulated twice
        for ix in range(10): 
            pt1[ix] = T_or_F(std.effort * std.IQ)
            pt2[ix] = T_or_F(std.effort * std.IQ)
           
        if std.luck > 0: #good luck, best result
            exercises[indx] = max(sum(pt1), sum(pt2))
        elif std.luck <0: #bad luck, worst result
            exercises[indx] = min(sum(pt1), sum(pt2))
        # convert to a boolean
        if exercises[indx] < 6:
            exercises[indx] = False
        else:
            exercises[indx] = True
    # returns the sumber of true values, 0-10
    return sum(exercises)
        


def test_score(std):
    """Calculate the test score
    """ 
    std.output()
    score = 10.0 * std.IQ * std.effort
    
    # charisma rounding
    if T_or_F(std.charisma):
        score = math.ceil(score)
    else:
        score = math.floor(score)
        
    return score
    


def letter_grade(sc_ex, sc_test):
    """take the exercise and test scores to produce a letter grade
    """
    percentage = sc_ex*.4 + sc_test*.6
    
    if percentage > 9:
        return 'A'
    if percentage > 8:
        return 'B'
    if percentage > 7:
        return 'C'
    if percentage >= 6:
        return 'D'
    if percentage < 6:
        return 'F'
    
    
def T_or_F(probability):
    """returns true or false given the probability, 
    allows us to skew the coinflip
    """
    return random.random() < probability



    
    


if __name__ == "__main__":
    main()