dictstudents={"akif":[["3162",300],["chemistry"]],"sena":[["1111",1111],["chemistry"]]}
dictadmin={"samet":"6616"}
dictcourses={"chemistry":3,"physics":3,"mathematics":4}
def admin(x):
    print("Welcome " + x + "!"+"What do you want to do?\n\n1-List courses\n2-Create a course\n3-Delete a course\n4-Show students registered to a course\n5-Users Budget Menu\n6-List Users\n7-Create User\n8-Delete User\n9-Exit\n")
    wish = int(input("your choice:"))
    if wish==1:
        print("Your choice:"+str(wish))
        print("--------courses--------")
        print("course offer     credit")
        sayı=1
        for i in dictcourses:
            print(str(sayı)+"-"+i+((17-len(i))*" ")+str(dictcourses[i]))
            sayı+=1
        admin(x)
    if wish==2:
        print("Your choice:"+str(wish))
        lessonname=input("What is the name of the course that you want to add?:")
        while lessonname in dictcourses:
            print("there is already a course as "+lessonname)
            lessonname = input("What is the name of the course that you want to add?:")
        lessoncredit=int(input("How many credits this course has?:"))
        print(lessonname+" will be added with "+str(lessoncredit)+" credits.")
        sureness=input("Are you sure?[Y/N]:")
        while sureness!="y" and sureness!="Y" and sureness!="n" and sureness!="N":
            sureness=input("please chose Y or N:")
        if sureness=="y" or sureness=="Y":
            dictcourses[lessonname]=lessoncredit
            admin(x)
        elif sureness=="n" or sureness=="N":
            admin(x)
    if wish==3:
        print("Your choice:"+str(wish))
        sayı=1
        for i in dictcourses:
            print(str(sayı)+"-"+i+((17-len(i))*" ")+str(dictcourses[i]))
            sayı+=1
        deleting=int(input("which course do yo want to delete?"))
        sayı=1
        for i in dictcourses:
            if deleting==sayı:
                for j in dictstudents:
                    if i in dictstudents[j][1]:
                        dictstudents[j][0][1]+=dictcourses[i]*100
                print(i+ " is deleted and money has been transferred back to student accounts")
                dictcourses.pop(i)
                break
            sayı+=1
        admin(x)
    if wish==4:
        print("Your choice:"+str(wish))
        sayı=1
        course=input("Which course do you want to show?")
        print("Course name: "+course+"\nStudents taking "+course)
        for i in dictstudents:
            if course in dictstudents[i][1]:
                print(str(sayı)+"-"+i)
                sayı+=1
        admin(x)
    if wish==5:
        print("Your choice:"+str(wish))
        def shwstdbdg():
            sayı=1
            print("  User        Money")
            for i in dictstudents:
                print(str(sayı)+"-"+i+(12-len(i))*" "+str(dictstudents[i][0][1]))
                sayı+=1
            moneyqst=int(input("What do you want to do?\n\n1-Add money to user\n2-Subtract money from user\n3-Back to admin menu"))
            if moneyqst==1:
                sayı = 1
                for i in dictstudents:
                    print(str(sayı)+"-"+i)
                    sayı+=1
                moneytostd=int(input("Which user do you want add money to their account?"))

                mony=int(input("how much money do yo want to add?"))
                sureness = input("Are you sure?[Y/N]:")
                while sureness != "y" and sureness != "Y" and sureness != "n" and sureness != "N":
                    sureness = input("please chose Y or N:")
                if sureness == "y" or sureness == "Y":
                    sayı2 = 1
                    for i in dictstudents:
                        if sayı2 == moneytostd:
                            dictstudents[i][0][1] += mony
                        sayı2 += 1
                    shwstdbdg()
                elif sureness == "n" or sureness == "N":
                    shwstdbdg()
            if moneyqst==2:
                sayı = 1
                for i in dictstudents:
                    print(str(sayı)+"-"+i)
                    sayı+=1
                moneytostd=int(input("Which user do you want substract money to their account?"))
                mony=int(input("how much money do yo want to substract?"))
                sureness = input("Are you sure?[Y/N]:")
                while sureness != "y" and sureness != "Y" and sureness != "n" and sureness != "N":
                    sureness = input("please chose Y or N:")
                if sureness == "y" or sureness == "Y":
                    sayı2 = 1
                    for i in dictstudents:
                        if sayı2 == moneytostd:
                            dictstudents[i][0][1] -= mony
                        sayı2 += 1
                    shwstdbdg()
                elif sureness == "n" or sureness == "N":
                    shwstdbdg()
            if moneyqst==3:
                admin(x)
        shwstdbdg()

    if wish==6:
        print("Your choice:"+str(wish))
        print("--CURRENT USERS--")
        sayı = 1
        for i in dictstudents:
            print(str(sayı) + "-" + i)
            sayı += 1
        admin(x)
    if wish==7:
        print("Your choice:"+str(wish))
        newuser=input("What is the name of user that you want to create?")
        newpass=input("What is the password for account?")
        newbudget=int(input("How much money do you want user to have?"))
        dictstudents[newuser]=[[newpass,newbudget],[]]
        print("The new user has been added successfully!")
        admin(x)
    if wish==8:
        print("Your choice:"+str(wish))
        print("--CURRENT USERS--")
        sayı = 1
        for i in dictstudents:
            print(str(sayı) + "-" + i)
            sayı += 1
        exuser=int(input("Which user do you want to delete?:"))
        sayı=1
        for i in dictstudents:
            if exuser==sayı:
                dictstudents.pop(i)
                print(i+" is deleted!")
                break
            sayı+=1
        admin(x)
    if wish==9:
        system()
def student(x):
    print("Welcome " +x+ "!"+" What do you want to do?\n\n1-Add courses to my courses\n2-Delete a course from my courses\n3-Show my courses\n4-Budget Menu\n5-Exit")
    wish=int(input("Your choice:"))
    print("Your choice:" + str(wish))
    if wish==1:
        while True:
            print("course offer     credit")
            sayı=1
            for i in dictcourses:
                print(str(sayı)+"-"+i+((17-len(i))*" ")+str(dictcourses[i]))
                sayı+=1

            enter=int(input("Which course do you want to take (Enter 0 to go to main menu)?"))
            othersayı=1
            newcourse="samet"
            for i in dictcourses:
                if enter==othersayı:
                    newcourse=i
                    if newcourse in dictstudents[x][1]:
                        print("This course is already in your profile, please choose another course:")
                    elif dictcourses[newcourse] * 100 > dictstudents[x][0][1]:
                        print(
                            "You don't have enough money in your account. Please deposit money, or choose a course with lesser credit.")
                    else:
                        print(newcourse + " has been successfully added to your courses.")
                        dictstudents[x][1].append(newcourse)
                        dictstudents[x][0][1] -= dictcourses[newcourse] * 100
                    break
                othersayı+=1


            if enter==0:
                student(x)
    if wish==2:
        print("course offer     credit")
        sayı = 1
        for i in dictstudents[x][1]:
            print(str(sayı) + "-" + i + ((17 - len(i)) * " ") + str(dictcourses[i]))
            sayı += 1
        othersayı=1
        delcourse=int(input("Which course do you want to remove?"))
        for i in dictcourses:
            if othersayı==delcourse:
                print("You have chosen:"+i+"\n"+str(dictcourses[i]*100)+"$ will be returned to your account")
                sureness=input("Are you sure that you want to remove this course? [Y/N]")
                while sureness != "y" and sureness != "Y" and sureness != "n" and sureness != "N":
                    sureness = input("please chose Y or N:")
                if sureness == "y" or sureness == "Y":
                    dictstudents[x][1].remove(i)
                    dictstudents[x][0][1]+=dictcourses[i]*100
                    print("Course has been deleted from your profile")
                    student(x)
                elif sureness == "n" or sureness == "N":
                    student(x)
            othersayı+=1
    if wish == 3:
        print("course name        credit")
        sayı2 = 1
        for i in dictstudents[x][1]:
            print(str(sayı2) + "-" + i + (17 - len(i)) * " ", str(dictcourses[i]))
            sayı2 += 1
            student(x)
    if wish == 4:
        print("##### BUDGET MENU #####")
        def stdbudget():
            print("Your budget is:" + str(dictstudents[x][0][1]))
            wanting = int(input("What do you want to do?\n\n1-add money\n2-go to main menu"))
            print("your choice:"+str(wanting))
            if wanting == 1:
                money =int(input("amount of money:"))
                dictstudents[x][0][1]+=money
                print("Your budget has been updated.")
                stdbudget()
            if wanting == 2:
                student(x)
        stdbudget()
    if wish == 5:
        system()

def system():
    print("-----Welcome to Course Management System-----")
    print("please provide login information")
    def contol():
        ıd=input("ID:")
        password=input("password:")
        for i in dictadmin:
            if ıd ==i  and password==dictadmin[i]:
                print("succesfuly logged in")
                admin(ıd)
                system()
        for j in dictstudents:
            if ıd==j and password==dictstudents[j][0][0]:
                print("succesfuly logged in")
                student(ıd)
                system()
        print("Invalid id or password please try again")
        contol()
    contol()
system()