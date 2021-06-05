from statistics import mean
from statistics import mode

def ft_m(ft):
    return round(float(ft)/3.281,4)
def ft_cm(ft):
    return float(ft) * 30.48
def inch_m(inch):
    return float(inch) / 39.37
def inch_cm(inch):
    return float(inch) * 2.54        

while(1):
    print("-------------------------------------------------------------------------------------------")
    print("Welcome to calculation of Body Adiposity Index Calculation")
    print("The Body Adiposity Index (BAI) is a method of estimating the amount of body fat in humans.")
    print("The BAI is calculated without using body weight, unlike the body mass index (BMI).")
    print("Instead, it uses the size of the hips compared to the person's height.")
    print("-------------------------------------------------------------------------------------------")
    initial = input("Would you like to continue (Y/N) : ")
    if(initial.upper() == "N"):
        print("---------------------------------END----------------------------------")
        break
    elif(initial.upper() == "Y"):    
        Listheight = []
        Listcircumference = []
        Listage = []
        Listbai = []
        underweight = 0
        healthy = 0
        overweight = 0
        obese = 0
        count = 0
        while(1):
            count+=1
            sex = input("Enter you sex (M/F) : ")
            if(sex.upper() == "M"):
                cal = input("Enter the metric which you are about to enter (m/ft/in) : ")
                if(cal.lower() == "ft"):
                    while True:
                        height = input("Enter height : ")
                        try:
                            height = float(height)
                            break
                        except ValueError:
                            print("This is not a number. Please enter a valid height")
                    while True:
                        circumference = input("Enter hip circumference : ")
                        try:
                            circumference = float(circumference)
                            break
                        except ValueError:
                            print("This is not a number. Please enter a valid circumference")
                    height = ft_m(height)
                    circumference = ft_cm(circumference)
                elif(cal.lower() == "m"):
                    while True:
                        height = input("Enter height : ")
                        try:
                            height = float(height)
                            break
                        except ValueError:
                            print("This is not a number. Please enter a valid height")
                    while True:
                        circumference = input("Enter hip circumference : ")
                        try:
                            circumference = float(circumference)
                            break
                        except ValueError:
                            print("This is not a number. Please enter a valid circumference")
                    circumference = float(circumference) * 100
                elif(cal.lower() == "in"):
                    while True:
                        height = input("Enter height : ")
                        try:
                            height = float(height)
                            break
                        except ValueError:
                            print("This is not a number. Please enter a valid height")
                    while True:
                        circumference = input("Enter hip circumference : ")
                        try:
                            circumference = float(circumference)
                            break
                        except ValueError:
                            print("This is not a number. Please enter a valid circumference")
                    height = inch_m(height)
                    circumference = inch_cm(circumference)
                age = int(input("Enter your age : "))
                Listheight.append(float(height))
                Listcircumference.append(float(circumference))
                Listage.append(age)
                bai = round(((float(circumference)/pow(float(height),1.5)) - 18),2)
                if(age>=20 and age<=39):
                    if(bai<8):
                        s="underweight"
                        underweight+=1
                    elif(bai<21):
                        s="healthy"
                        healthy+=1
                    elif(bai>21 and bai<=26):
                        s="overweight"
                        overweight+=1
                    elif(bai>26):
                        s="obese"    
                        obese+=1        
                elif(age>=40 and age<=59):
                    if(bai<11):
                        s="underweight"
                        underweight+=1
                    elif(bai<23):
                        s="healthy"
                        healthy+=1
                    elif(bai>23 and bai<=29):
                        s="overweight"
                        overweight+=1
                    elif(bai>29):
                        s="obese" 
                        obese+=1
                elif(age>=60 and age<=79):
                    if(bai<13):
                        s="underweight"
                        underweight+=1
                    elif(bai<25):
                        s="healthy"
                        healthy+=1
                    elif(bai>25 and bai<=31):
                        s="overweight"
                        overweight+=1
                    elif(bai>31):
                        s="obese"
                        obese+=1        
                print("--------------------------------------------------")        
                print("Your BAI is "+str(bai))           
                print("According to your age and sex you are "+s)
                print("--------------------------------------------------")   
                Listbai.append(bai)
                
            else:
                cal = input("Enter the metric which you are about to enter (m/ft/in) : ")
                if(cal.lower() == "ft"):
                    while True:
                        height = input("Enter height : ")
                        try:
                            height = float(height)
                            break
                        except ValueError:
                            print("This is not a number. Please enter a valid height")
                    while True:
                        circumference = input("Enter hip circumference : ")
                        try:
                            circumference = float(circumference)
                            break
                        except ValueError:
                            print("This is not a number. Please enter a valid circumference")
                    height = ft_m(height)
                    circumference = ft_cm(circumference)
                elif(cal.lower() == "m"):
                    while True:
                        height = input("Enter height : ")
                        try:
                            height = float(height)
                            break
                        except ValueError:
                            print("This is not a number. Please enter a valid height")
                    while True:
                        circumference = input("Enter hip circumference : ")
                        try:
                            circumference = float(circumference)
                            break
                        except ValueError:
                            print("This is not a number. Please enter a valid circumference")
                    circumference = float(circumference) * 100
                elif(cal.lower() == "in"):
                    while True:
                        height = input("Enter height : ")
                        try:
                            height = float(height)
                            break
                        except ValueError:
                            print("This is not a number. Please enter a valid height")
                    while True:
                        circumference = input("Enter hip circumference : ")
                        try:
                            circumference = float(circumference)
                            break
                        except ValueError:
                            print("This is not a number. Please enter a valid circumference")
                    height = inch_m(height)
                    circumference = inch_cm(circumference)
                age = int(input("Enter your age : "))
                Listheight.append(float(height))
                Listcircumference.append(float(circumference))
                Listage.append(age)
                bai = round(((float(circumference)/pow(float(height),1.5)) - 18),2)
                if(age>=20 and age<=39):
                    if(bai<21):
                        s="underweight"
                        underweight+=1
                    elif(bai<33):
                        s="healthy"
                        healthy+=1
                    elif(bai>33 and bai<=39):
                        s="overweight"
                        overweight+=1
                    elif(bai>39):
                        s="obese"  
                        obese+=1          
                elif(age>=40 and age<=59):
                    if(bai<23):
                        s="underweight"
                        underweight+=1
                    elif(bai<35):
                        s="healthy"
                        healthy+=1
                    elif(bai>35 and bai<=41):
                        s="overweight"
                        overweight+=1
                    elif(bai>41):
                        s="obese" 
                        obese+=1
                elif(age>=60 and age<=79):
                    if(bai<25):
                        s="underweight"
                        underweight+=1
                    elif(bai<38):
                        s="healthy"
                        healthy+=1
                    elif(bai>38 and bai<=43):
                        s="overweight"
                        overweight+=1
                    elif(bai>43):
                        s="obese"   
                        obese+=1  
                print("--------------------------------------------------")        
                print("Your BAI is "+str(bai))           
                print("According to your age and sex you are "+s)
                print("--------------------------------------------------")   
                Listbai.append(bai)

            
            
            res = input("Would you like to add another response (Y/N) : ")
            
            if(res.upper() == "Y"):
                continue
            elif(res.upper() == "N"):
                print("----------------------------------------------------------------------")
                print("-----------------------------STATISTICS-------------------------------")
                print("----------------------------------------------------------------------")
                print("Mean BAI of respondants : "+str(mean(Listbai)))
                print("Mode BAI of respondants : "+str(mode(Listbai)))
                print("Range of BAI is from %s to %s"%(str(min(Listbai)),str(max(Listbai))))
                print("Range of height is from %s to %s"%(str(min(Listheight)),str(max(Listheight))))
                print("Range of circumference is from %s to %s"%(str(min(Listcircumference)),str(max(Listcircumference))))
                print("Range of age is from %s to %s"%(str(min(Listage)),str(max(Listage))))
                print("Number of underweight respondants : "+str(underweight))
                print("Percentage of underweight respondants of the whole list : ",str((underweight/count)*100))
                print("Number of healthy respondants : "+str(healthy))
                print("Percentage of healthy respondants of the whole list : ",str((healthy/count)*100))
                print("Number of overweight respondants : "+str(overweight))
                print("Percentage of overweight respondants of the whole list : ",str((overweight/count)*100))
                print("Number of obese respondants : "+str(obese))
                print("Percentage of obese respondants of the whole list : ",str((obese/count)*100))
                print("----------------------------------------------------------------------")
                print("---------------------------------END----------------------------------")
                print("----------------------------------------------------------------------")
                break