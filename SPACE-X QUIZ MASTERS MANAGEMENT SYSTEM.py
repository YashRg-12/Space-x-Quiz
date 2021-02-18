import random
from datetime import date
import mysql.connector as mysql

#---------------------------------------------------------------------------ADMIN MODULE-------------------------------------------------------------------
def add_question():                             #to add a new question to a quiz
    print("\n\t\t***********************************************************************************************************************************")
    print("\t\t\t\tADD QUIZ QUESTION MODULE")
    print("\t\t***********************************************************************************************************************************")
    print("\t\t***********************************************************************************************************************************")
    qid=input("\t\t\t\t\tEnter a Question Id:-")
    print("\t\t***********************************************************************************************************************************")
    question=input("\tEnter a Question:-")
    print("\t\t***********************************************************************************************************************************")
    option1=input("\t\t\t\t\t\tEnter First Option:-")
    print("\t\t***********************************************************************************************************************************")
    option2=input("\n\t\t\t\t\t\tEnter Second Option:-")
    print("\t\t***********************************************************************************************************************************")
    option3=input("\n\t\t\t\t\t\tEnter Third Option:-")
    print("\t\t***********************************************************************************************************************************")
    option4=input("\n\t\t\t\t\t\tEnter Fourth Option:-")
    print("\t\t***********************************************************************************************************************************")
    correctanswer=input("\n\t\t\t\t\t\tEnter The Correct Answer:-")
    print("\t\t***********************************************************************************************************************************")
    foption1=input("\n\t\t\t\t\t\tEnter the first fifty fifty Option:-")
    print("\t\t***********************************************************************************************************************************")
    foption2=input("\n\t\t\t\t\t\tEnter the second fifty fifty Option:-")
    mycursor.execute("insert into questions values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(qid,question,option1,option2,option3,option4,correctanswer,foption1,foption2,))
    mydb.commit()
    print("\t\t*****************************************************************************************************************************")
    print("\t\t\t\tYour Question has been added to Python Quiz Successfully!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("\t\t*****************************************************************************************************************************")


def view_questions():           #to view all questions of a quiz
    print("\n\t\t***********************************************************************************************************************************")
    print("\t\t\t\tQUESTIONS IN QUIZ ARE")
    print("\t\t***********************************************************************************************************************************")
    mycursor.execute("select * from questions")
    res=mycursor.fetchall()
    if len(res)==0:
        print("\n\t\t\t\tNO QUESTION AVAILABLE IN QUIZ")
    else:
        for i in res:
            print("\t\t\t\tQUESTION ID :-",i[0])
            print("\t\t\t\tQUESTION      :-",i[1])
            print("\t\t\t\tOPTION1:-",i[2])
            print("\t\t\t\tOPTION2:-",i[3])
            print("\t\t\t\tOPTION3:-",i[4])
            print("\t\t\t\tOPTION4:-",i[5])
            print("\t\t\t\tCORRECT ANSWER:-",i[6])
            print("\t\t\t\tFIFTY FIFTY OPTION 1:-",i[7])
            print("\t\t\t\tFIFTY FIFTY OPTION 2:-",i[8])
            print("\t\t*******************************************************************************************************************************")

def search_question():      #Search/View a Particular Question in a Quiz
    qid=input("\n\t\t\t\tEnter A Valid Question Id:-")
    mycursor.execute("select * from questions where qid=%s",(qid,))
    res=mycursor.fetchall()
    if len(res)==0:
        print("\n\t\t\t\tENTER A VALID QUESTION ID")
    else:
        print("\n\t\t***********************************************************************************************************************************")
        print("\t\t\t\tQUESTION DETAILS ARE")
        print("\t\t***********************************************************************************************************************************")
        for i in res:
            print("\t\t\t\tQUESTION ID :-",i[0])
            print("\t\t\t\tQUESTION      :-",i[1])
            print("\t\t\t\tOPTION1:-",i[2])
            print("\t\t\t\tOPTION2:-",i[3])
            print("\t\t\t\tOPTION3:-",i[4])
            print("\t\t\t\tOPTION4:-",i[5])
            print("\t\t\t\tCORRECT ANSWER:-",i[6])
            print("\t\t\t\tFIFTY FIFTY OPTION 1:-",i[7])
            print("\t\t\t\tFIFTY FIFTY OPTION 2:-",i[8])
            print("\t\t*******************************************************************************************************************************")


def delete_question():              #to delete a question from a quiz
    qid=input("\n\t\t\t\tEnter A Valid Question Id:-")
    mycursor.execute("select * from questions where qid=%s",(qid,))
    res=mycursor.fetchall()
    if len(res)==0:
        print("\n\t\t\t\tENTER A VALID QUESTION ID")
    else:
        print("\n\t\t***********************************************************************************************************************************")
        print("\t\t\t\tWELCOME TO DELETE MODULE")
        print("\t\t***********************************************************************************************************************************")
        mycursor.execute("delete from questions where qid=%s",(qid,))
        mydb.commit()
        print("\t\t\t\tQUESTION HAS BEEN REMOVED FROM THE QUIZ SUCCESSFULLY!!!!")
        view_questions()

def modify_question():
    qid=input("\n\t\t\t\tEnter A Valid Question Id:-")
    mycursor.execute("select * from questions where qid=%s",(qid,))
    res=mycursor.fetchall()
    if len(res)==0:
        print("\n\t\t\t\tENTER A VALID QUESTION ID")
    else:
        while True:
            print("\n\t\t***********************************************************************************************************************************")
            print("\t\t\t\tWELCOME TO UPDATE MODULE")
            print("\t\t***********************************************************************************************************************************")
            print("\t\t\t\t1.Update Question")
            print("\t\t\t\t2.Update Option1")
            print("\t\t\t\t3.Update Option2")
            print("\t\t\t\t4.Update Option3")
            print("\t\t\t\t5.Update Option4")
            print("\t\t\t\t6.Update Correct Answer")
            print("\t\t\t\t7.Update Fifty Fifty Option1")
            print("\t\t\t\t8.Update Fifty Fifty Option2")
            print("\t\t\t\t9.Exit")
            ch=int(input("\n\t\t\t\tEnter Your Choice:-"))
            if ch==1:
                   nquestion=input("\n\t\t\t\tEnter a New Question:-")
                   mycursor.execute("update questions set question=%s where qid=%s",(nquestion,qid,))
                   mydb.commit()
            elif ch==2:
                   noption1=input("\n\t\t\t\tEnter New First Option:-")
                   mycursor.execute("update questions set option1=%s where qid=%s",(noption1,qid,))
                   mydb.commit()
            elif ch==3:
                   noption2=input("\n\t\t\t\tEnter New Second Option:-")
                   mycursor.execute("update questions set option2=%s where qid=%s",(noption2,qid,))
                   mydb.commit()
            elif ch==4:
                   noption3=input("\n\t\t\t\tEnter New Third Option:-")
                   mycursor.execute("update questions set option3=%s where qid=%s",(noption3,qid,))
                   mydb.commit()
            elif ch==5:
                   noption4=input("\n\t\t\t\tEnter New Fourth Option:-")
                   mycursor.execute("update questions set option4=%s where qid=%s",(noption4,qid,))
                   mydb.commit()
            elif ch==6:
                   nanswer=input("\n\t\t\t\tEnter a New Correct Answer:-")
                   mycursor.execute("update questions set correctanswer=%s where qid=%s",(nanswer,qid,))
                   mydb.commit()
            elif ch==7:
                   nf1=input("\n\t\t\t\tEnter a New Fifty Fifty First Option:-")
                   mycursor.execute("update questions set foption1=%s where qid=%s",(nf1,qid,))
                   mydb.commit()
            elif ch==8:
                   nf2=input("\n\t\t\t\tEnter a New Fifty Fifty Second Option:-")
                   mycursor.execute("update questions set foption2=%s where qid=%s",(nf2,qid,))
                   mydb.commit()
            elif ch==9:
                   break
        print("\t\t********************************************************************************************************************************")
        print("\t\t\t\tYour Record Has been Updated Successfully")
        mycursor.execute("select * from questions where qid=%s",(qid,))
        res=mycursor.fetchall()
        print("\t\t***********************************************************************************************************************************")
        print("\t\t\t\tUPDATED QUESTION DETAILS ARE")
        print("\t\t***********************************************************************************************************************************")
        for i in res:
            print("\t\t\t\tQUESTION ID :-",i[0])
            print("\t\t\t\tQUESTION      :-",i[1])
            print("\t\t\t\tOPTION1:-",i[2])
            print("\t\t\t\tOPTION2:-",i[3])
            print("\t\t\t\tOPTION3:-",i[4])
            print("\t\t\t\tOPTION4:-",i[5])
            print("\t\t\t\tCORRECT ANSWER:-",i[6])
            print("\t\t\t\tFIFTY FIFTY OPTION 1:-",i[7])
            print("\t\t\t\tFIFTY FIFTY OPTION 2:-",i[8])
            print("\t\t*******************************************************************************************************************************")


def view_players():    #to view the details of all players
    mycursor.execute("select * from player")
    res=mycursor.fetchall()
    if len(res)==0:
        print("\n\t\t\t\tNO PLAYERS AVAILABLE IN QUIZ")
    else:
        print("\n\t\t***********************************************************************************************************************************")
        print("\t\t\t\tPLAYERS DETAILS ARE")
        print("\t\t***********************************************************************************************************************************")
        for i in res:
            print("\t\t\t\tPLAYER ID :-",i[0])
            print("\t\t\t\tPLAYER NAME     :-",i[1])
            print("\t\t\t\tPLAYER GENDER:-",i[2])
            print("\t\t\t\tPLAYER AGE:-",i[3])
            print("\t\t\t\tPLAYER EMAIL ID:-",i[4])
            print("\t\t\t\tPLAYER PHONE NUMBER:-",i[5])
            print("\t\t\t\t50-50 LIFE LINE :-",i[8])   
            print("\t\t*******************************************************************************************************************************")


def search_player():        #to search a particular player
    pid=input("\n\t\t\t\tENTER THE PLAYER ID:-")
    mycursor.execute("select * from player where pid=%s",(pid,))
    res=mycursor.fetchall()
    if len(res)==0:
        print("\n\t\t\t\tENTER A VALID PLAYER ID")
    else:
        print("\n\t\t***********************************************************************************************************************************")
        print("\t\t\t\tPLAYERS DETAILS ARE")
        print("\t\t***********************************************************************************************************************************")
        for i in res:
            print("\t\t\t\tPLAYER ID :-",i[0])
            print("\t\t\t\tPLAYER NAME     :-",i[1])
            print("\t\t\t\tPLAYER GENDER:-",i[2])
            print("\t\t\t\tPLAYER AGE:-",i[3])
            print("\t\t\t\tPLAYER EMAIL ID:-",i[4])
            print("\t\t\t\tPLAYER PHONE NUMBER:-",i[5])
            print("\t\t\t\t50-50 LIFE LINE :-",i[8])   
            print("\t\t*******************************************************************************************************************************")
        


def view_all_scoreboard():          #to view the scoreboard of all the players
    mycursor.execute("select * from scoreboard")
    res=mycursor.fetchall()
    if len(res)==0:
        print("\n\t\t\t\tOOPPPPS!!!!!!!!!!!!SORRY!!!!!!!!!!!NO DATA IS AVAILABLE")
    else:
        print("\n\t\t=======================================================================================================")
        print("\t\t\t\tSPACE-X Quiz Masters SCOREBOARD")
        print("\t\t========================================================================================================")
        for i in res:
            sid=i[0]
            pid=i[1]
            date=i[2]
            correct=i[3]
            incorrect=i[4]
            total_score=i[5]

            print("\t\t\tSCORE ID:-",sid)
            print("\t\t\t\tDATE:-",date)
            print("\t\t\tPLAYER ID:-",pid)
            print("\t\t\tNUMBER OF INCORRECT ANSWERS:-",incorrect)
            print("\t\t\tNUMBER OF CORRECT ANSWERS:-",correct)
            print("\t\t\tTOTAL SCORE IS:-",total_score)
            print("\t\t========================================================================================================")


        
def admin_account():      #to register admin detail
               print("\t\t****************************************************************************************************************************")
               print("\t\t<<<<<<<<<<<<<<<<<WELCOME TO ADMIN REGISTRATION MODULE>>>>>>>>>>>>>>>>>>>>>>")
               print("\t\t****************************************************************************************************************************")
               aid=input("\t\t\t\tEnter Your ID:-")
               aname=input('\t\t\t\tEnter your name')
               apassword=input('\t\t\t\tEnter 7 digit  password')
               agender=input("\t\t\t\tEnter Your Gender(m/f):-")
               aemail=input("\t\t\t\tEnter your email id:-")
               aage=int(input("\t\t\t\tEnter Your Age:-"))
               ausername=input('\t\t\t\tEnter Your User Name:-')
               print("\t\t*****************************************************************************************************************************")
               mycursor.execute("insert into admin values(%s,%s,%s,%s,%s,%s,%s)",(aid,aname,aage,agender,aemail,ausername,apassword,))
               mydb.commit()
               print ('\n\t\t\t\tAccount created succesfully!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
               print("\n\t\t\t\tKindly Proceed to Login!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
               print("\t\t******************************************************************************************************************************")

def loginmodule1():                     #admin Login Module
            global log
            print("\n\t\t************************************************************************************************************************")
            print("\t\t<<<<<<<<<<<<<<<<<<<<<<<<WELCOME TO ADMIN LOGIN MODULE>>>>>>>>>>>>>>>>>>>>>>")
            print("\t\t***************************************************************************************************************************")
            ausername=input('\n\t\t\t\tENTER ADMIN USERNAME:-')
            apassword=input('\n\t\t\t\tEnter ADMIN PASSWORD:-')
            mycursor.execute("select * from admin where ausername=%s and apassword=%s",(ausername,apassword,))
            res=mycursor.fetchall()
            if len(res)==0:
                print("\n\t\t\t\tKindly Enter A Valid Username or Password!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            else:
                print("\n\t\t\tWELCOME, YOU LOGGED IN SUCCESSFULLY!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                return 1


#-------------------------------------------------------------------PLAYER MODULE-----------------------------------------------------------------------------
def player_account():          #To register Player details
    print("\t\t**********************************************************************************************************************************")
    print("\t\t<<<<<<<<<<<<<<<<<WELCOME TO PLAYER REGISTRATION MODULE>>>>>>>>>>>>>>>>>>>>>>")
    print("\t\t**********************************************************************************************************************************")
    pid=input("\t\t\t\tEnter the Player Id in positive natural number:-")
    pname=input('\t\t\t\tEnter Player name:-')
    ppassword=input("\t\t\t\tEnter 7 digit  password:-")
    pgender=input('\t\t\t\tEnter Player Gender:-')
    pemail=input('\t\t\t\tEnter Player Email Id:-')
    pphone=input('\t\t\t\tEnter Player mobile no:-')
    page=int(input("\t\t\t\tEnter Player Age:-"))
    pusername=input("\t\t\t\tEnter Player User Name:-")
    mycursor.execute("insert into player values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(pid,pname,pgender,page,pemail,pphone,pusername,ppassword,'NOT USED'))
    mydb.commit()
    print("\t\t**************************************************************************************************************************************")
    print ('\t\t\t\t\tAccount created succesfully!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    print('\n\t\t\t\tKindly Proceed to LOGIN!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    print("\t\t*************************************************************************************************************************************")


def loginmodule2():         #Player login module
    global log
    print("\n\t\t**********************************************************************************************************************************")
    print("\t\t<<<<<<<<<<<<<<<<<<<<<<<<WELCOME TO PLAYER LOGIN MODULE>>>>>>>>>>>>>>>>>>>>>>")
    print("\t\t************************************************************************************************************************************")
    pusername=input('\n\t\t\t\tENTER PLAYER USER NAME:-')
    ppassword=input('\n\t\t\t\tENTER PLAYER PASSWORD:-')
    mycursor.execute("select * from player where pusername=%s and ppassword=%s",(pusername,ppassword,))
    res=mycursor.fetchall()
    if len(res)==0:
        print("\n\t\t\t\tKindly Enter A Valid Username or Password!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    else:
        print("\n\t\t\tWELCOME",pusername.upper()," YOU LOGGED IN SUCCESSFULLY!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        return pusername

def view_instructions():        #to view the instructions to play the quiz
    print("\n\t\t**********************************************************************************************************************************")
    print("\t\t<<<<<<<<<<<<<<<<<<<<<<<<<WELCOME TO SPACE-X Quiz Masters>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("\t\t*************************************************************************************************************************************")
    print("""\n\tHello Player, Welcome to the Space-X Quiz Masters. This is the good way to learn about planets,stars,nebulae and many more
            \tand test your knowledge about space.

            \tThis Space-X quiz consists 10  Multiple Choice Questions(MCQ) about space. Each Question consists four
            \tOptions out of which you have to select the one correct answer.


            \tAt any stage of SPACE-X Quiz Masters, if you want help then you have a lifeline 'Fifty Fifty' which removes two incorrect answers
            \tfrom your screen and leaves only two options: one option is correct and one option is incorrect. select the correct option.

            \tOnly Once in this quiz you will able to use this lifeline FIFTY FIFTY

            \tEach Correct Answer carries 5 Marks. At any stage you can quit the quiz.

            \tYou can also view the score  board to find out your score and the number of correctly answer questions.

            \tNow you are ready to play the Quiz

            \t\t\t\tALL THE BEST AND ENJOY YOUR LEARNING!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            \t**********************************************************************************************************************************************""")

def play_quiz(pusername):            # to start playing a quiz
    mycursor.execute("select count(*) from questions")
    res=mycursor.fetchall()
    for i in res:
        total_questions=i[0]
    if len(res)==0 and total_questions<10:
        print("\n\t\tSORRY!!!!!!!!!!!!!!!!!!!!!!!There  is some Error, Kindly Come Again after sometime or Contact to the SPACE-X Quiz Masters ADMIN")
    else:
        print("\n\t\t***********************************************************************************************************************************")
        print("\t\t\tWELCOME TO SPACE-X Quiz Masters. LETS START THE QUIZ")
        print("\t\t*************************************************************************************************************************************")
        r=random.randint(1,total_questions)
        qid=r
        question_list=[qid]
        correct=incorrect=0
        for j in range(1,11):             
              mycursor.execute("select * from questions where qid=%s",(str(qid),))
              res=mycursor.fetchall()
              for i in res:
                  correct_answer=i[6]
                  fifty_option1=i[7]
                  fifty_option2=i[8]
              print("\n\t\t********************************QUESTION NUMBER ",j," *********************************************************")
              print("\t\t",i[1])
              print("\t\t********************************************************************************************************************************")
              print("\t\t(a)",i[2],"\t\t\t(b)",i[3])
              print("\t\t(c)",i[4],"\t\t\t(d)",i[5])
              fifty_ch=input("\n\t\tDo you want to use your Life line FIFTY-FIFTY(yes/no)")
              if fifty_ch=="yes":
                      mycursor.execute("select fifty_status from player where pusername=%s",(pusername,))
                      data=mycursor.fetchall()
                      for i in data:
                          fifty_status=i[0]
                      if fifty_status=="USED":
                          print("\n\t\tYou Have already Used the lifeline")
                      if fifty_status=="NOT USED":
                          mycursor.execute("update player set fifty_status=%s where pusername=%s",('USED',pusername,))
                          mydb.commit()
                          print("\n\t\t\t\t******************OPTIONS AFTER USING FIFTY FIFTY*************************")
                          print("\t\t(a) ",fifty_option1,"\t\t\t(b)",fifty_option2)
              elif fifty_ch=='no':
                      pass
              ans=input("\n\t\tEnter Your Correct answer:-")
              if ans==correct_answer:
                    correct=correct+1
                    print("\n\t\t\t!!!!!!!!!!!HURREY!!!THIS IS THE CORRECT ANSWER")
              else:
                    incorrect=incorrect+1
                    print('\n\t\t\t!!!!SORRY!!!!THIS IS THE WRONG ANSWER')
              qid=random.randint(1,11)
              if qid in question_list:
                          maximum=question_list[0]
                          for k in range(0,len(question_list)):
                              if question_list[k]>=maximum:
                                  maximum=question_list[k]
                          qid=maximum+1
                          question_list.append(qid)
              else:
                          question_list.append(qid)
              chp=input("\n\t\tDo you want to Quit(yes/no)?")
              if chp=="yes":
                    break
              else:
                    continue
        sid=str(qid)+pusername
        pdate=date.today()
        mycursor.execute("select pid from player where pusername=%s",(pusername,))
        res1=mycursor.fetchall()
        pid=res1[0][0]
        total_score=correct*5
        mycursor.execute("insert into scoreboard values(%s,%s,%s,%s,%s,%s)",(sid,pid,pdate,correct,incorrect,total_score,))
        mydb.commit()
        print("\n\t\t\t***********************WELL DONE!!!!!PLEASE COME BACK AGAIN*******************************************")
        print("\n\t\t\tYOUR SCORE ID IS:-",sid)
        print("\n\t\t\tTo Check Your Score Please View the Score Board!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        mycursor.execute("update player set fifty_status='NOT USED' where pusername=%s",(pusername,))
        mydb.commit()



def view_scoreboard():      #to view the scoreboard of a player
        print("\t\t**********************************************************************************************************************************")
        sid=input("\n\t\t\t\tEnter Your Score Id:-")
        mycursor.execute("select sid,player.pid,date,no_correct_ans,no_incorrect_ans,total_score,pname,fifty_status from scoreboard,player where player.pid=scoreboard.pid and sid=%s",(sid,))
        res=mycursor.fetchall()
        if len(res)==0:
            print("\n\t\t\tEnter A Registered Score ID")
        else:
            for i in res:
                pid=i[1]
                date=i[2]
                correct=i[3]
                incorrect=i[4]
                total_score=i[5]
                pname=i[6]
                fifty_status=i[7]
            print("\n\t\t=======================================================================================================")
            print("\t\t\t\tSPACE-X Quiz Masters SCOREBOARD")
            print("\t\t========================================================================================================")
            print("\t\t\tSCORE ID:-",sid,"\t\t\t\tDATE:-",date)
            print("\t\t\tPLAYER ID:-",pid,"\t\t\tPLAYER NAME:-",pname)
            print("\t\t========================================================================================================")
            print("\t\t\tNUMBER OF INCORRECT ANSWERS:-",incorrect)
            print("\t\t\tNUMBER OF CORRECT ANSWERS:-",correct)
            print("\t\t=========================================================================================================")
            print("\t\t\tYOUR TOTAL SCORE IS:-",total_score)
            print("\t\t========================================================================================================")    

#----------------------------------------------MAIN MODULE------------------------------------------------------------------------
mydb = mysql.connect(host="localhost",user="root",passwd="1758591")
mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS PYTHONQUIZ")
mydb.commit()
mycursor.execute("USE PYTHONQUIZ")

mycursor.execute("create table if not exists admin(Aid varchar(10) Primary Key, Aname varchar(20),Aage varchar(10) not null,agender varchar(10) not null, aemail varchar(30) not null,ausername varchar(30) unique not null,Apassword varchar(10))")
mycursor.execute("create table if not exists player(pid varchar(10) Primary Key,pname varchar(20),pgender varchar(10) not null,page int(3) not null,pemail varchar(30) not null,pphone varchar(10) not null,pusername varchar(20) unique not null,ppassword varchar(10),fifty_status varchar(30) not null)")
mycursor.execute("create table if not exists questions(qid varchar(40) primary key,question varchar(500) not null unique,option1 varchar(100) not null,option2 varchar(100) not null,option3 varchar(100) not null,option4 varchar(100) not null,correctanswer varchar(100) not null,foption1 varchar(100) not null,foption2 varchar(100) not null)")
mycursor.execute("create table if not exists scoreboard(sid varchar(40) primary key,pid varchar(10) references player(pid) on delete cascade on update cascade,date date not null,no_correct_ans int(10) not null,no_incorrect_ans int(10) not null,total_score int(40) not null)")
def mainquizmenu():
            while True:
                 print("\t\t=============================================================================")
                 print("\t\t <<<<<<<<<<<<<<<<<<<<<WELCOME TO SPACE-X QUIZ  SYSTEM>>>>>>>>>>>>>>>>>>>>>>>")
                 print("\t\t=============================================================================")
                 print("\t\t\t\t1. ADMIN")
                 print("\t\t\t\t2. PLAYER")
                 print("\t\t\t\t3. EXIT")
                 print("\t\t=============================================================================")
                 x=int(input("\n\t\t\t\tEnter Your Choice :- "))
                 if x==1:       #admin
                     while True:
                         print("\t\t=============================================================================")
                         print("\t\t <<<<<<<<<<<WELCOME TO ADMIN MODULE>>>>>>>>>>>>>>>>>>")
                         print("\t\t=============================================================================")
                         print("\t\t\t\t1. ADMIN REGISTRATION")
                         print("\t\t\t\t2. ADMIN LOGIN")
                         print("\t\t\t\t3. EXIT")
                         print("\t\t=============================================================================")
                         y=int(input("\n\t\t\t\tEnter Your Choice :- "))
                         if y==1:
                             admin_account()
                         elif y==2:
                             log=loginmodule1()
                             if (log==1): 
                                 while True:
                                          print("\n\t\t===================================================================")
                                          print("\t\t<<<<<<<<<<<<<<<<<<<<<<<<<<ADMIN MENU>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                                          print("\t\t====================================================================")
                                          print("\t\t\t\t1.Add A Question for a Quiz")
                                          print("\t\t\t\t2.Delete a Question from a Quiz")
                                          print("\t\t\t\t3.Modify Question for a Quiz")
                                          print("\t\t\t\t4.Search a Particular Question in a Quiz")
                                          print("\t\t\t\t5.View All Questions in a Quiz")
                                          print("\t\t\t\t6.View All Players Details")
                                          print("\t\t\t\t7.View a Particular Player Details")
                                          print("\t\t\t\t8.View Score Board for all Players")
                                          print("\t\t\t\t9.View A Score Board Of A Particular Player")
                                          print("\t\t\t\t10.Exit")
                                          ny=int(input('\n\t\t\t\tEnter Your Choice:'))
                                          if(ny==1):
                                                  add_question()
                                          elif(ny==2):
                                                  delete_question()
                                          elif(ny==3):
                                                 modify_question()
                                          elif(ny==4):
                                                  search_question()
                                          elif(ny==5):
                                                  view_questions()                                         
                                          elif(ny==6):
                                                  view_players()
                                          elif(ny==7):
                                                  search_player()
                                          elif(ny==8):
                                                  view_all_scoreboard()
                                          elif(ny==9):
                                                  view_scoreboard()         #to search a scoreboard of a particular player
                                          elif(ny==10):
                                                 break                                              
                             else:
                                    print ('\n\t\t\t\tWrong Username Or password!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                         elif y==3:
                            break
                 elif x==2:         #Player module
                    while True:
                         print("\t\t=============================================================================")
                         print("\t\t <<<<<<<<<<<WELCOME TO PLAYER MODULE>>>>>>>>>>>>>>>>>>")
                         print("\t\t=============================================================================")
                         print("\t\t\t\t1. PLAYER REGISTRATION")
                         print("\t\t\t\t2. PLAYER LOGIN")
                         print("\t\t\t\t3. EXIT")
                         print("\t\t=============================================================================")
                         y=int(input("\n\t\t\t\tEnter Your Choice :- "))
                         if y==1:
                             player_account()
                         elif y==2:
                             pusername=loginmodule2()
                             if (pusername): 
                                 while True:
                                            print("\n\t\t===================================================================")
                                            print("\t\t<<<<<<<<<<<<<<<<<<<<<<<<<<PLAYER MENU>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                                            print("\t\t====================================================================")
                                            print("\t\t\t\t1.View Instructions to Play Quiz")
                                            print("\t\t\t\t2.Start to Play Quiz")
                                            print("\t\t\t\t3.View Score Board")
                                            print("\t\t\t\t4.Exit")
                                            n=int(input('\n\t\t\t\tEnter Your Choice:'))
                                            if(n==1):
                                                view_instructions()
                                            elif(n==2):
                                                play_quiz(pusername)
                                            elif(n==3):
                                                view_scoreboard()
                                            elif(n==4):
                                                break
                             else:
                                        print ('\n\t\t\t\tWrong Username Or Password!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                         elif y==3:
                                break
                 elif x==3:
                     break
mainquizmenu()
