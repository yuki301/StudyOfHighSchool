import pandas as pd
import datetime
test_calendar=pd.read_excel("检测日程表.xlsx")
work_calendar=pd.read_excel("工期日程.xlsx")

date=datetime.datetime.now().strftime("%m%d")
def get_today_work():
    today_work=work_calendar[work_calendar["日期"]==date[1]+" "+date[2:]].工期
    today_work=today_work.reset_index(drop=True)
    if today_work.count()==0:
        today_work="今天没有截止的工作"
    else:
        today_work=today_work[0]

    return today_work

def get_today_test():
    today_test=test_calendar[test_calendar["日期"]==date[1]+" "+date[2:]]
    today_test=today_test.reset_index(drop=True)
    if today_test.上午.count()==0 and today_test.下午.count()==0:
        today_test="今天没有要进行的测试"
    else:
        if today_test[today_test.index==0].上午.count()!=0 and today_test[today_test.index==0].下午.count()!=0:
            today_test="上午："+today_test[today_test.index==0].上午[0]+" 下午："+today_test[today_test.index==0].下午[0]
        elif today_test[today_test.index==0].上午.count()!=0:
            today_test="上午:"+today_test[today_test.index==0].上午[0]
        elif today_test[today_test.index==0].下午.count()!=0:
            today_test="下午:"+today_test[today_test.index==0].下午[0]       
        
    return today_test

def make_work_list():
    work_calendar.to_html("templates/work_list.html")

def make_test_list():
    test_calendar.to_html("templates/test_list.html")
