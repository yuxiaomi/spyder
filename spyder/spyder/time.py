import datetime
import time
import datetime

# ctime=int(time.time()*1000000)
# ctime=float(time.time())
# print(ctime)

# tt=15857458353846000
# tt=time.localtime(1585745982.7266655)
# timenow=time.strftime('%y%m%d %h%m%s',tt)
# print(timenow)
# registtime=datetime.datetime.now()
# print(registtime)

# 10位的数字转换成时间
def int_date():
    tuptime=time.localtime(1568217600)
    standartime=time.strftime("%Y-%m-%d",tuptime)
    print(standartime)

def textsplit():
    text="dp_id=4233197-3&crc64=1&source=2"
    af=text.split("&",3)
    print(af,af[0])

# textsplit()
def daterange():
    registtime=datetime.datetime.now()
    print(registtime)
    delta=datetime.timedelta(days=1)
    before=registtime-delta
    print(before)

def paesr(times):
    text=times/1000
    tuptime = time.localtime(text)
    standartime = time.strftime("%Y/%m/%d", tuptime)
    print(standartime)

if __name__ == '__main__':
    # daterange()
    paesr(1574870400000)