#import math for pythag 
import math

#Validation code to verify if the triangle is valid
def validationCategorisetriangles(sideA, sideB, sideC):
    #if the first two sides combined are equal to or greater then the third side then it is a valid triangle
    if sideA+sideB>=sideC and sideB+sideC>=sideA and sideC+sideA>=sideB:
        return True
    else:
        return False 

#Function for categorising triangles
def runCategoriseTrianglesMenu():
    print("Input lengths of the triangle sides: ")
    try:    
        sideA = int(input("Side A: "))
        sideB = int(input("Side B: "))
        sideC = int(input("Side C: "))
        if sideA == sideB == sideC:
            if validationCategorisetriangles(sideA, sideB, sideC) == False:
                print("please enter a valid triangle")
                return runCategoriseTrianglesMenu()
            print("This is an equilateral triangle")
        elif sideA==sideB or sideB==sideC or sideC==sideA:
            if validationCategorisetriangles(sideA, sideB, sideC) == False:
                print("please enter a valid triangle")
                return runCategoriseTrianglesMenu()
            print("This is an isosceles triangle")
            
        else:
            if validationCategorisetriangles(sideA, sideB, sideC) == False:
                print("please enter a valid triangle")
                return runCategoriseTrianglesMenu()
            print("This is a Scalene triangle")
         
    except ValueError:
         print("Please enter an appropriate value")
         return runCategoriseTrianglesMenu()
    
#Function for pythagoras calculator    
def runPythagorasCalculatorMenu():
    try:
        UsrInput = input("Do you know the hypotenus? Y/N:")
        if UsrInput.lower() == "n":
            SidelengthAsqrd = int(input("Enter the length of the adjecent side: "))
            SidelengthBsqrd = int(input("Enter the length of the opposite side: "))
            AnswerPythag = math.sqrt(SidelengthAsqrd ** 2 + SidelengthBsqrd ** 2)
            print("Answer is:", AnswerPythag)  
        
        elif UsrInput.lower() == "y":
            print("Transposing is in development")
            return runPythagorasCalculatorMenu()
        
        else:
            print("please choose from the following two options")
            return runPythagorasCalculatorMenu()
            
    except ValueError:
        print("Please enter an appropriate value")
        return runPythagorasCalculatorMenu()

#Function for Triangle angle calculator
def runTriangleAngleCalculatorMenu():
    try:
        SideangleA = int(input('Please Enter the First Angle of a Triangle: '))
        SideangleB = int(input('Please Enter the Second Angle of a Triangle: '))
   
# Finding the Third Angle
        AnswerAngle = 180 - (SideangleA + SideangleB)
        print("the remaining angle is:" , AnswerAngle)
    except ValueError:
        print("Please enter an appropriate value")
        return runTriangleAngleCalculatorMenu()
    

#RunAgain function set to true 
RunAgain = True
while(RunAgain == True):
    #Printing menu options 
    print("A.Categorise triangles")
    print("B.Pythagoras calculator")
    print("C.Calculate an angle within a triangle")
    print("D.exit")
    #User Input
    UsrInput = input ("Please Select:")
    #Categorise triangles
    if (UsrInput.lower() ==  'a' ) :
        print("A.Categorise triangles -choosen")
        runCategoriseTrianglesMenu()
        if UsrInput:
            input("please press enter to return to the main menu") == ''
            RunAgain
       
    #Pythagoras calculator      
    elif (UsrInput.lower() == 'b' ):
        print("B.Pythagoras calculator -choosen")
        runPythagorasCalculatorMenu()
        if UsrInput:
            input("please press enter to return to the main menu") == ''
            RunAgain
    #Angle of a Triangle calculator
    elif (UsrInput.lower() == 'c'):
        print("C.Calculate an angle within a triangle -choosen")
        runTriangleAngleCalculatorMenu()
        if UsrInput:
            input("please press enter to return to the main menu") == ''
            RunAgain
    #exit option      
    elif (UsrInput.lower() == 'd'):
        print("exiting now..")
        exit()
    else:
        print("Please choosen from the following menu options")
        RunAgain 
