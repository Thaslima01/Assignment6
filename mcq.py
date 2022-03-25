Q1="""1.In which year of First World War Germany declared war on Russia and France?
A.1914
B.1915
C.1916
D.1917"""

Q2="""2.ICAO stands for
A.International Civil Aviation Organization
B.Indian Corporation of Agriculture Organization
C.Institute of Company of Accounts Organization
D.None of the above"""

Q3="""3.India has largest deposits of ____ in the world.
A.gold
B.copper
C.mica
D.None of the above"""

Q4="""4.How many Lok Sabha seats belong to Rajasthan?
A.32
B.25
C.30
D.17"""

Q5="""In a normal human body, the total number of red blood cells is
A.15 trillion
B.20 trillion
C.25 trillion
D.30 trillion"""
print("welcome to MCQ test")
name=input("your name: ")
options={Q1:"A",Q2:"A",Q3:"C",Q4:"B",Q5:"D"}
score=0
for i in options:
    print(i)
    answer=input("your answer (A/B/C/D) : ")
    if answer==options[i]:
        print("correct")
        score+=1
        print(score)
    else:
        print("incorrect")
        score-=1
        print(score)
print("final score is: ",score)


