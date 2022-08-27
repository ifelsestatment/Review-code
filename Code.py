import math
def runTriangleValidation(sideA, sideB, sideC ):
    if sideA+sideB>=sideC and sideB+sideC>=sideA and sideC+sideA>=sideB:
            return True
    else:
            return False 

def runCategoriseTrianglesMenu():
    print("Input lengths of the triangle sides: ")
    try:
        sideA = int(input("Side A: "))
        sideB = int(input("Side B: "))
        sideC = int(input("Side C: "))
        if sideA == sideB == sideC:
            print("This is an equilateral triangle")
        elif sideA==sideB or sideB==sideC or sideC==sideA:
            print("This is an isosceles triangle")
        else:
             print("This is a Scalene triangle")
    
        if  runTriangleValidation(sideA, sideB, sideC ):
            runCategoriseTrianglesMenu()
        else:
             print("This is not a valid triangle")  
         
    except ValueError:
         print("Please enter an appropriate value")
         return runCategoriseTrianglesMenu()
    
    
def runPythagorasCaculatorMenu():
    try:
        UsrInput = input("Do you know the hypotenus? Y/N")
        if UsrInput.lower() == "n":
            SidelengthAsqrd = int(input("Enter the length of the adjecent side: "))
            SidelengthBsqrd = int(input("Enter the length of the opposite side: "))
            AnswerPythag = math.sqrt(SidelengthAsqrd ** 2 + SidelengthBsqrd ** 2)
            print(AnswerPythag)  
    except ValueError:
        print("Please enter an appropriate value")
        return runPythagorasCaculatorMenu()

def runTriangleAngleCalculatorMenu():
    try:
        SidelengthAangle = int(input('Please Enter the First Angle of a Triangle: '))
        SidelengthBangle = int(input('Please Enter the Second Angle of a Triangle: '))
   
# Finding the Third Angle
        AnswerAngle = 180 - (SidelengthAangle + SidelengthBangle)
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
    if (UsrInput.lower() ==  'a') :
        print("A.Categorise triangles -choosen")
        runCategoriseTrianglesMenu()
        if UsrInput:
            input("please press enter to return to the main menu") == ''
            RunAgain
       
    #Pythagoras calculator      
    elif (UsrInput.lower() == 'b' ):
        print("B.Pythagoras calculator -choosen")
        runPythagorasCaculatorMenu()
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
    #exit program      
    elif (UsrInput.lower() == 'd'):
        print("exiting now..")
        exit()
    else:
        print("Please choosen from the following menu options")
        RunAgain 
        
        
        
        
        


        
        
        
