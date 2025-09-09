import pandas as pd
import akshare as ak
import time
import os
from datetime import datetime

# 读取股票代码列表
codes_df = pd.read_csv('codes.csv')
codes = codes_df['code'].astype(str).tolist()

# 创建汇总数据
all_signals = []

for code in codes:
    try:
        print(f"Fetching {code}...")
        
        # 获取ETF历史数据
        df = ak.fund_etf_hist_em(symbol=code, period="daily", adjust="qfq")
        
        # 重命名列
        df = df.rename(columns={
            '日期': 'date',
            '开盘': 'open', 
            '收盘': 'close',
            '最高': 'high',
            '最低': 'low',
            '成交量': 'volume',
            '成交额': 'amount',
            '振幅': 'amplitude',
            '涨跌幅': 'change_pct',
            '涨跌额': 'change',
            '换手率': 'turnover'
        })
        
        # 只保留需要的列
        keep_cols = ['date', 'open', 'close', 'high', 'low', 'volume', 'amount']
        existing_cols = [col for col in keep_cols if col in df.columns]
        df = df[existing_cols]
        
        # 添加代码列
        df['code'] = code
        
        # 转换数据类型
        numeric_cols = ['open', 'close', 'high', 'low', 'volume', 'amount']
        for col in numeric_cols:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors='coerce')
        
        # 保存单个ETF数据
        df.to_csv(f"data/{code}.csv", index=False)
        
        # 添加到汇总数据（只保留最近260天）
        df_recent = df.tail(260).copy()
        all_signals.append(df_recent)
        
        time.sleep(0.5)  # 避免请求过快
        
    except Exception as e:
        print(f"Failed to fetch {code}: {e}")
        continue

# 创建汇总信号表
if all_signals:
    signals_df = pd.concat(all_signals, ignore_index=True)
    
    # 添加空白列用于后续计算
    calc_cols = ['r60', 'r120', 'score', 'atr20', 'atr_ratio', 'ma200', 'regime_tag']
    for col in calc_cols:
        signals_df[col] = None
    
    # 按代码和日期排序
    signals_df = signals_df.sort_values(['code', 'date'])
    
    # 保存汇总数据
    signals_df.to_csv("signals.csv", index=False)
    print(f"Updated signals.csv with {len(signals_df)} rows")

# 创建订单模板
orders_df = pd.DataFrame(columns=['symbol', 'side', 'qty', 'amount', 'limit_low', 'limit_high', 'window'])
orders_df.to_csv("orders.csv", index=False)

# 创建更新时间戳
with open("last_update.txt", "w") as f:
    f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC"))
