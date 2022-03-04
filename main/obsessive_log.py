import xlsxwriter



def createworkbook():
   f=input("Enter todays date in the form ""date.xlsx:     """)
   workbook=xlsxwriter.Workbook(f)

   jee=input("""Enter today's date:  
   
   """)
   worksheet=workbook.add_worksheet(jee)
   worksheet.write("A1","6AM - 12PM")
   worksheet.write("B1", "12PM - 6PM")
   worksheet.write("C1","6PM-12AM")
   worksheet.write("D1","Total")
   print("""------------------6AM-12PM-------------------
   
   """)
   phase1=input("""Enter the amount of time spent:   
   
   """)
   worksheet.write("A2",phase1)
   print("""------------------12PM-6PM--------------------
   
   """)
   phase2=input("""Enter the amount of time spent:  
   
   """)
   worksheet.write("B2",phase2)
   print("""------------------6PM-12AM---------------------
   
   """)
   phase3=input("""Enter the amount of time spent:  
   
   """)
   worksheet.write("C2",phase3)
   print("""------------------Total time spent--------------
   
   """)
   total=input("""Enter the total amount of time spent:  
   
   """)
   worksheet.write("D2",total)
   workbook.close()
   



def menu(ans):
    if ans==1:
        createworkbook()
    if ans==2:
        pass
print("""---------------------------------------------------Obsession Log----------------------------------------------------------

        ----------------------------------------------------Version 1.0------------------------------------------------------------
        
        ----------------------------------------------------Main Menu--------------------------------------------------------------
        
        1. Create a new logbook for the current month
        2. Exit the app""")
ans=int(input("Enter your choice (1-2)"))
menu(ans)
