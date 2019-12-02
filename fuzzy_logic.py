import csv

def imp():    
    with open('test.csv') as fuzz:
        iqro = csv.reader(fuzz)
        hasil=[]
        for i in iqro:
            hasil.append(i)
    return hasil

def fetchVal(a):
    hasil = []
    b = a[1:100]
    for i in b:
        data = []
        data.append(float(i[1]))
        data.append(float(i[2]))
        hasil.append(data)
    return hasil

def followercount(x):
    fuzz_rslt = []
    bagus = follower_bagus(x)
    cukup = follower_cukup(x)
    jelek = follower_jelek(x)
    fuzz_rslt.append(bagus)
    fuzz_rslt.append(cukup)
    fuzz_rslt.append(jelek)
    return fuzz_rslt

def engagementcount(x):
    fuzz_rslt = []
    bagus = engagement_bagus(x)
    cukup = engagement_cukup(x)
    jelek = engagement_jelek(x)
    fuzz_rslt.append(bagus)
    fuzz_rslt.append(cukup)
    fuzz_rslt.append(jelek)
    return fuzz_rslt

def engagement_bagus(x):
    if(x>5):
        fuzz_rslt = 1
    elif(x<=4):
        fuzz_rslt = 0
    else:
        fuzz_rslt = (x-4)/(5-4)

    return fuzz_rslt

def engagement_cukup(x):
    if(x<=0.5 or x>5):
        fuzz_rslt = 0
    elif (2<x<=3):
        fuzz_rslt = 1
    elif(0.5<x<=2):
        fuzz_rslt = (x-0.5)/(2-0.5)
    else:
        fuzz_rslt = (5-x)/(5-3)
    return fuzz_rslt

def engagement_jelek(x):
    if(x<0.5):
        fuzz_rslt = 1
    elif (x>=1.5):
        fuzz_rslt = 0
    else:
        fuzz_rslt = (1.5-x)/(1.5-0.5)
    return fuzz_rslt


def follower_bagus(x):
    if(x>55000):
        fuzz_rslt = 1
    elif(x<=45000):
        fuzz_rslt = 0
    else:
        fuzz_rslt = (x-45000)/(55000-45000)
    return fuzz_rslt

def follower_cukup(x):
    if (x>55000 or x<=5000):
        fuzz_rslt = 0
    elif (25000<x<=35000):
        fuzz_rslt = 1
    elif (5000<x<=25000):
        fuzz_rslt = (x-5000)/(25000-5000)
    else:
        fuzz_rslt = (55000-x)/(55000-35000)
    return fuzz_rslt


def follower_jelek(x):
    if(x<5000):
        fuzz_rslt = 1
    elif(x>=15000):
        fuzz_rslt = 0
    else:
        fuzz_rslt = (15000-x)/(15000-5000)
    return fuzz_rslt

def inference(x,y):
    rslt = []
    for i in x:
        for j in y:
            if(i>j):
                rslt.append(i)
            else:
                rslt.append(j)
    return rslt

def accepted(x):
    acc = []
    acc.append(x[0])
    acc.append(x[1])
    acc.append(x[3])
    hasil = max(acc)
    return hasil

def considered(x):
    con = []
    con.append(x[2])
    con.append(x[4])
    con.append(x[5])
    con.append(x[6])
    hasil = max(con)
    return hasil

def rejected(x):
    rej = []
    rej.append(x[7])
    rej.append(x[8])
    hasil = max(rej)
    return hasil

def sugeno(a,b,c):
    hasil = ((a*80)+(b*60)+(c*40))/(a+b+c)
    return hasil

def find_fuzz_max(x):
    b = sorted(range(len(x)), key=lambda k: x[k], reverse=True)
    c = b[:20]
    maxima = []
    for i in c:
        maxima.append([x[i],i+1])
    return maxima

# main program disini
a = imp()
data = fetchVal(a)
result = []
for i in data:
    follower = followercount(i[0])
    engage = engagementcount(i[1])
    infer = inference(follower,engage)
    acc = accepted(infer)
    con = considered(infer)
    rej = rejected(infer)
    hasil = sugeno(acc,con,rej)
    result.append(hasil)
maxima = find_fuzz_max(result)
print("================================================== 20 TOP GLOBAL ========================================")
for i in maxima:
    print("+++++++++++++++++++++++++++")
    print("   nilai fuzz : ",i[0])
    print("   index data : ",i[1])
    print("+++++++++++++++++++++++++++")
print('==========================================================================================================')

with open("hasilmantap.csv","w+") as my_csv:
    csvWriter = csv.writer(my_csv,delimiter=',')
    csvWriter.writerows(maxima)


