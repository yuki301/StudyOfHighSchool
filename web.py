from this import d
from flask import Flask,render_template,request,redirect
import calendar_load,datetime
app=Flask(__name__)
nowtime=datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
today_work=calendar_load.get_today_work()
today_test=calendar_load.get_today_test()

@app.route("/")
def index():
    next=request.args.get("next")
    if next=="查看规划":
            return redirect("/calendar")
    return render_template("index.html",today_work=today_work,today_test=today_test,nowtime=nowtime)

@app.route("/calendar")
def calendar():
    next=request.args.get("next")
    if next=="查看完整工作日程":
        return redirect("/calendar/work_list")
    elif next=="查看完整测试日程":
        return redirect("/calendar/test_list")
    return render_template("calendar.html",today_work=today_work,today_test=today_test)

@app.route("/calendar/work_list")
def work_list():
    calendar_load.make_work_list()
    return render_template("work_list.html")

@app.route("/calendar/test_list")
def test_list():
    calendar_load.make_test_list()
    return render_template("test_list.html")



if __name__=='__main__':
    app.debug=True
    app.run(host='0.0.0.0',port=5000)

