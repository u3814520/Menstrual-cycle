import time
import datetime
import calendar

localtime = time.localtime(time.time())
try:
    in_month = int(input("請輸入上次經期月份: "))
    if in_month <= 12:
        try:
            in_day = int(input("請輸入上次經期日期: "))
            if in_day <= 31:
                in_date = str(localtime[0]) + '-' + str(in_month) + '-' + str(in_day)
                try:
                    cycle = int(input("請輸入月經週期(天): "))
                    Half_cycle = int(cycle / 2)
                    dt = datetime.datetime.strptime(in_date, '%Y-%m-%d')
                    out_date = (dt + datetime.timedelta(days=Half_cycle)).strftime('%Y-%m-%d')
                    out_MC = (dt + datetime.timedelta(days=cycle)).strftime('%Y-%m-%d')
                    yy=int(out_MC[0:4])
                    mm=int(out_MC[5:7])
                    print(f'下次排卵日期是:{out_date}')
                    print(f'下次經期日期是:{out_MC}')
                    print()
                    print(calendar.month(yy,mm))
                except ValueError:
                    print('請輸入數字。')
            else:
                print('請輸入正確日期')
        except ValueError:
            print('請輸入正確日期')
    else:
        print('請輸入正確月份')
except ValueError:
    print('請輸入正確月份')
