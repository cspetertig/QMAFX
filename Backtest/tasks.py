from celery import Celery
from celery.schedules import crontab
import os
import sys
import django
import sqlite3
pathname=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,pathname)
sys.path.insert(0,os.path.abspath(os.path.join(pathname,'..')))
# sys.path.insert(0,os.path.abspath(os.path.join(pathname,'./Engine/')))
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ForexWeb.settings')
django.setup()
from Strategy.models import Strategy
from Backtest.models import BackTest
app = Celery('tasks', backend='db+sqlite:///celery_result.sqlite', broker='redis://localhost:6379//0')
# app.conf.CELERY_RESULT_BACKEND = 'db+sqlite:///celery_result.sqlite'
# celery -A tasks worker -B
# celery -A tasks beat
# @app.on_after_configure.connect
@app.task
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(30, check_backtest.s(), name='peoredic_check')

@app.task(bind=True)
def  backtest_start(self,strategy_id):

    strategy=Strategy.objects.get(pk=strategy_id)
    backtest = BackTest(strategy=strategy,task=self.request.id)
    backtest.save()
    code=strategy.code
    filename=strategy.title+'.py'
    f=open(filename,'wb')
    f.write(code)
    f.close()
    commond1='import %s' %(strategy.title)
    exec(commond1)
    info=[]
    commond2='info =%s.main()' %(strategy.title)
    exec(commond2)
    backtest.Profit=info[0][1]
    backtest.Sharp=info[1][1]
    backtest.MaxDrawdown=info[2][1]
    backtest.MaxDrawdown = info[2][1]
    backtest.Buynumber = info[3][1]
    backtest.Buyprofit = info[4][1]
    backtest.Sellnumber = info[5][1]
    backtest.Sellprofit = info[6][1]
    backtest.Winrate = info[7][1]
    backtest.Profitfactor = info[8][1]
    backtest.Std = info[9][1]
    backtest.Mean=info[10][1]
    backtest.status='DONE'
    backtest.save()
    strategy.status='TESTED'
    strategy.save()

@app.task
def check_backtest():
    strategys=Strategy.objects.filter(status='PROCESSING')
    for i in strategys:
        backtests=BackTest.objects.filter(strategy=i)
        for index in backtests:
            conn = sqlite3.connect("celery_result.sqlite")
            cursor = conn.cursor()
            sql='select * from celery_taskmeta where task_id="%s"' %(index.task)
            cursor.execute(sql)
            try:
                results=cursor.fetchall()[0]
                status=results[2]
                info=results[5]
                if status=='FAILURE':
                    i.status='SAVED'
                    index.error_info=info
                    index.status='ERROR'
                    i.save()
                    index.save()
            except Exception:
                pass


