data={"Consumer":"user","eb_readings":[1100,1200,1350,1650,2050]}
def Calculate_electricity_bill():
    bills=data['eb_readings']
    bill=0
    List=[]
    for i in range(len(data['eb_readings'])-1):
        est=bills[i+1]-bills[i]
        
        print(f"month:{i+1}\nConsumed data:{est}")
        if est<100:
            a1=0
            print("Bill amount:0\n")
            bill=0
        if est>=100 and est<=200:
            a2=2*est
            print(f"Bill amount:{2*est}\n")
            bill+=(2*est)
        if est>200 and est<=500:
            a3=5*est
            print(f"Bill amount:{5*est}\n")
            bill+=(5*est)
        if est>500 and est<=1000:
            a4=10*est
            print(f"Bill amount:{10*est}\n")
            bill+=(10*est)
        if est>=1000:
            a5=14*est
            print(f"Bill amount:{14*est}\n")
            bill+=(14*est)
        Dict={"Month":i+1,"Consumed data":est,"Bill amount":bill}
       
        List.append(Dict)
    # return bill
    return str(List)

Bill=Calculate_electricity_bill()
print(Bill)
file=open(f"/home/akshaya/karka/D1920230718/Homework/{data['Consumer']}.txt",'w')
file.write(Bill)
file.close()
