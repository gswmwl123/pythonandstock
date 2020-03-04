import tushare as ts
import pandas as pd
import time

ts.set_token('58194507256eb590f85fed25ca3251cb7d157d6abf71aef82ad1ed03')


def maintask():
    pro = ts.pro_api()
    # 获取基础信息数据，包括股票代码、名称、上市日期、退市日期等
    pool = pro.stock_basic(exchange='',
                           list_status='L',
                           adj='qfq',
                           fields='ts_code,symbol,name,area,industry,fullname,list_date, market,exchange,is_hs')
    # print(pool.head())
    print('获得上市股票总数：', len(pool) - 1)
    j = 1
    for i in pool.ts_code:
        print('正在获取第%d家，股票代码%s.' % (j, i))
        # 接口限制访问200次/分钟，加一点微小的延时防止被ban
        time.sleep(0.121)
        j += 1
        df = pro.daily(ts_code=i,
                       start_date=startdate,
                       end_date=enddate,
                       fields='ts_code, trade_date, open, high, low, close, pre_close, change, pct_chg, vol, amount')
        # print(df.head())
        writer = pd.ExcelWriter('D://quant//' + i + '.xlsx')
        df.to_excel(writer, sheet_name=i + '', index=False)
        writer.save()


if __name__ == '__main__':
    # 设置起始日期
    startdate = '19980101'
    enddate = '20200303'
    # 主程序
    maintask()
