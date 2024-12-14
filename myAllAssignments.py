#class definition
class myAllAssignments():
    
    #start function myBMI()
    def myBMI():
        #take input
        bmi=float(input("Enter the BMI Index:"))
        #check conditions single and multiple ranges with if and elif
        if(bmi<18.5):
            print("Under weight")
        elif(bmi>=18.5 and bmi<=24.9):
            print("Normal")
        elif(bmi>=25.00 and bmi<=29.9):
            print("Over Weight")
        elif(bmi==30):
            print("Obese ")
        elif(bmi>30.00 and bmi <34.9):
            print("Very Overweight: Class 1 Obese")
        elif(bmi>=35 and bmi <=39.9):
            print("Very Overweight: Class 2 Obese")
        #if none of the scenarion matches use the else
        else:
            print("Very Overweight: Class 3 Obese")
    # end of function myBMI()

    # start function subfields()
    def mySubfields():
        print("Sub-fields in AI are:")
        List=['Machine Learning', 'Neural Networks', 'Vision', 'Robotics', 'Speech Processing', 'Natural Language Processing']
        for temp in List:
            print(temp)
    #end of subfields function()

    #start function oddeven()
    def OddEven():
        num = int(input("Enter a number: "))  
        if (num % 2) == 0:  
           print("{0} is Even number".format(num))  
        else:  
           print("{0} is Odd number".format(num))  
    #end of function oddeven()

    # age eligibility function for male/female
    def Eligible():
        gender = input("Your Gender")
        age = int(input("Your age:"))
        if(gender =="Male"):
            if(age >=21):
                print("ELIGIBLE")
            else:
                print("NOT ELIGIBLE")
        elif(gender =="Female"):
            if(age >=18):
              print("ELIGIBLE")
            else:
              print("NOT ELIGIBLE")
        else:
            print("Ïnvalid")
    # end of age eligibility function 
    # find percentage function ()
    def calPercentage(s1,s2,s3,s4,s5):
        percentage = (s1+s2+s3+s4+s5) / 5
        return percentage
    # end of percentafe function ()

    # start function triangle area()
    def myTriangleArea(Height,Breadth):
        tarea =  (Height*Breadth)/2
        return tarea
    # end function triangle area

    # start function triangle perimeter()
    def myTrianglePerimeter(Height1,Height2,Breadth):
        tperimeter = Height1+Height2+Breadth
        return tperimeter
    # end function triangel perimeter()




    
