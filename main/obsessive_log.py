import xlsxwriter



def createworkbook():
#Asking the date to create a workbook
   f=input("Enter todays date in the form ""date.xlsx:     """)
   workbook=xlsxwriter.Workbook(f)
   worksheet=workbook.add_worksheet("Thoughts Log")
   worksheet.write("A1","6AM - 12PM")
   worksheet.write("B1", "12PM - 6PM")
   worksheet.write("C1","6PM-12AM")
   worksheet.write("D1","Total")
   #================================================================================================================
   #Thoughts log
   print("-----------------------------------------Thoughts Log-----------------------------")
   print("""------------------6AM-12PM-------------------
   
        """)
   phase1=int(input("""Enter the amount of time spent in minutes:   
   
        """))
   worksheet.write("A2",phase1)
   print("""------------------12PM-6PM--------------------
   
        """)
   phase2=int(input("""Enter the amount of time spent in minutes:  
   
        """))
   worksheet.write("B2",phase2)
   print("""------------------6PM-12AM---------------------
   
        """)
   phase3=int(input("""Enter the amount of time spent in minutes:  
   
        """))
   worksheet.write("C2",phase3)
   print("""------------------Total time spent--------------
   
        """)
   total=phase1+phase2+phase3
   print("Total time spent is", total,"minutes")
   print("Your information has been entered into an excel sheet")
   worksheet.write("D2",total)
   
   
   worksheet=workbook.add_worksheet("Activity Log")
   worksheet.write("A1","Activity")
   worksheet.write("B1", "Target")
   worksheet.write("C1","Action")

   #=======================================================================================================================
   #Activity log
   print("------------------------------------Activity Log-------------------------------------------")
   ques=int(input("""Enter no of activities:
    
        """))
   for i in range(ques):
        cellone=int(input("""Enter the order number of activity:
            
          """))
        act=input("""Enter name of the activity:
            
          """)
        
        cellone=cellone+1
        cellzero=str(cellone)
        cell1="A"+cellzero
        worksheet.write(cell1,act)
        print("Activity Logged")

        target=input("""Enter the target time:
            
          """)
        cell2="B"+cellzero
        worksheet.write(cell2,target)
        print("Target logged")

        action=input("""Enter the action:
            
          """)
        cell3="C"+cellzero
        worksheet.write(cell3,action)
        print("Action Logged")
    
   #===================================================================================================================
   #Trigger Log
   worksheet=workbook.add_worksheet("Trigger Log")
   worksheet.write("A1","Trigger")
   worksheet.write("B1", "Thought")

   print("-------------------------------------Trigger Log----------------------------------------------")
    
    
   notrig=int(input("""Enter no of trigger:
    
        """))
   for i in range(notrig):
        tellone=int(input("""Enter order no of trigger:
        
          """))
        tellone=tellone+1
        tellzero=str(tellone)
        tell1="A"+tellzero
        trigger=input("""Enter the trigger:
        
          """)
        worksheet.write(tell1,trigger)
        print("Trigger logged")

        Thought=input("""Enter the thought:
        
          """)
        tell2="B"+ tellzero
        worksheet.write(tell2,Thought)
        print("Thoughts Logged")




        
        

   
    



   workbook.close()



       


def menu(ans):
    if ans==1:
        createworkbook()
    if ans==2:
        pass
print("""---------------------------------------------------Obsessive Log----------------------------------------------------------

        ----------------------------------------------------Version 1.1------------------------------------------------------------
        
        ----------------------------------------------------Main Menu--------------------------------------------------------------
        
        1. Create a new logbook for the current day
        2. Exit the app""")
ans=int(input("Enter your choice (1-2)"))
menu(ans)

