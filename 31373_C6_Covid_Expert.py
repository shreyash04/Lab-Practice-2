temp=float(input("Enter Your Temperature: "))
oxy=int(input("Enter your oxygen level: "))
symp=['backpain','chestpain','nausea','fever','cough','sore throat','sunken eyes','low body temperature','restlessness']
covid=0
for i in range(len(symp)):
    print(symp[i])
    ans=input("y/n:")
    if i==3 and ans=='y':
        covid+=1
    if i==4 and ans=='y':
        covid+=1
    if i==5 and ans=='y':
        covid+=1
    if i==8 and ans=='y':
        covid+=1
if covid==4 and oxy<=85 and temp>100:
    print("You have high symptoms of Covid and requested to hospitalize")
elif covid==4 and oxy >90 and temp<100:
    print("You may have symptoms of covid requested to get tested ")
elif covid<4 and oxy >90 and temp>100:
    print("You have may viral fever but still requested to home quarantine")
elif covid<4 and oxy >90 and temp <97:
    print("You may have normal cold and take medicines as per prescription")
else:
    print("you may not have covid but do get full body check up for other diseases")