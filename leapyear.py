n=int(input('enter a year'))
def year():
    if n  % 4==0:
        if n% 100==0:
            if n % 400==0:
                print("given year is leap year")
            else:
                print("given year is not a leap year")
        else:
            print("given year is leap year")
    else:
        print("given year is not leap year")   
year()             

                
            
