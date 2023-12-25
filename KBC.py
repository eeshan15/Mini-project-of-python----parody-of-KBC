## ___________KAUN BANEGA HAZARPATI_______##
print("Disclamer \n This is the parody of Kaun banega crorepati please do not get offended !!!")
ques = ["Q1","Q2","Q3","Q4","Q5"]
amount =5000
wining_amount = 0
#Introduction
for i in ques:
    wining_amount=wining_amount+5000
    print("For",i,"You will win ",wining_amount,"₹")
    z=input("Are you ready ? : ")
    if z=="yes" or z=="Yes" or z=="YES":
        print("\n Okay lets begin with : ",i)
        
        if i=="Q1":
            Q1=" Who wrote the national anthem of the country?"
            print("\n Question-1",Q1)
            option=["mahatma gandhi","bankim chandra chattopadhyay","rabindranath tagore","subhash chandra bose"]
            print("A :",option[0]," B :",option[1])
            print("C :",option[2]," D :",option[3])
            x=input("Enter your answer : ")
            if x.lower()=="rabindranath tagore" or x.upper()=="C":
                print("Correct answer !!! , you won :",amount,"₹")
            elif x.lower()!="rabindranath tagore" or x!="C":
                print("Wrong answer, you won : ",0,"₹")
                break
      
        elif i=="Q2":
                Q2="Who is the IronMan of India?"
                print(Q2)
                options=["netaji bose","shaheed bhagat singh","vallabh bhaipatel","vd savarkar"]
                print("A :",options[0]," B :",options[1])
                print("C :",options[2]," D :",options[3])
                y=input("Enter your answer :")
                if y.lower()=="vallabh bhaipatel" or y.upper()=="C":
                    print("Correct answer, you won :",wining_amount,"₹")
                elif y.lower()!="rabindranath tagore" or y.upper()!="C":
                    print("Wrong answer, you won : ",amount,"₹")
                    break
        
        elif i=="Q3":
                Q3="Who is the HitMan of India?"
                print("\n",Q3)
                option1=["virat kohli","rohit sharma","virendar sehwag","mahendra singh dhoni"]
                print("A :",option1[0]," B :",option1[1])
                print("C :",option1[2]," D :",option1[3])
                a=input("Enter your answer :")
                if a.lower()=="rohit sharma" or a.upper()=="B":
                    print("Correct answer, you won :",wining_amount,"₹")
                elif a.lower()!="rabindranath tagore" or a.upper()!="C":
                    print("Wrong answer, you won : ",amount*2,"₹")
                    break
        
        elif i=="Q4":
                Q4="Who is going to be the Next PM of India in 2024?"
                print("\n",Q4)
                options=["narendra modi","pappu rahul gandhi","muffler wala kejriwal","buddha amit shah"]
                print("A :",options[0]," B :",options[1])
                print("C :",options[2]," D :",options[3])
                b=input("Enter your answer :")
                if b.lower()=="narendra modi" or b.upper()=="A":
                    print("Correct answer, you won :",wining_amount,"₹")
                elif b.lower()!="narendra modi" or b.upper()!="A":
                    print("Wrong answer, you won : ",amount*3,"₹")
                    break
        
        elif i=="Q5":
            Q5="Where is ram mandir situated ?"
            print("\n",Q5)
            options=["muzzafarnagar","ajmer","lucknow","ayodhya"]
            print("A :",options[0]," B :",options[1])
            print("C :",options[2]," D :",options[3])
            c=input("Enter your answer : ")
            if c.lower()=="ayodhya" or c.upper()=='d':
                print("Correct answer , you won",wining_amount,"₹")
            else :
                print("Wrong answer,you won :",amount*4,"₹")

    else :
        print("Khel le bhai waise bhi konsa paise milne wale hai")
        break