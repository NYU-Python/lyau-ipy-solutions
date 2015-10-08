print 'For average closing price, enter a ticker symbol (aapl, goog, fb, lnkd, or msft) followed by the number of days (1-251), then press [Enter]'
userinput=False

#create a while loop to check if user inputs a valid ticker symbol and number of days
while not userinput:
    stock, days = raw_input().split()
    if (stock in ['aapl','goog','fb','msft','lnkd']) and (1<=int(days)<=251):
        userinput=True
    elif stock not in ['aapl','goog','fb','msft','lnkd']:
        print 'Please choose a ticker from the list'
    else: 
        print 'Please choose a number between 1 and 251'
        
file=str(stock)+'.csv'
#retrieves the appropriate file from the stock the user inputs.  Splits file into a list of lists.  
#Where each line/row in the file becomes a list of elements in each row of the file. 
#Removes the header row and creates a new list of just the closing prices (the 5th element of each line).
lines= [line.split() for line in open(file, 'rb')]
lines=lines[1:]
data=[]
for line in lines:
    data.append(line[-1].split(','))
closingprices=[]
for line in data:
    closingprices.append(line[4])
   
average=0
sum=0

#Adds up the appropriate number of closing prices and then divides it by the number of days for the average
for i in closingprices[0:int(days)]:
    sum+=float(i)
    average=sum/int(days)            
        
print round(average,2)

