import os
import sys
import pandas as pd
from datetime import *
from datautils import *
from pathlib import Path

BASE_URL = 'https://data.binance.vision/'
INTERVALS = ["1m", "5m", "15m", "30m", "1h", "2h", "4h", "6h", "8h", "12h", "1d", "3d", "1w", "1mo"]
DAILY_INTERVALS = ["1m", "5m", "15m", "30m", "1h", "2h", "4h", "6h", "8h", "12h", "1d"]
TRADING_TYPE = ["spot", "um", "cm"]

def download_file(base_path, file_name, date_range):
    save_path = os.path.dirname(__file__) + '/data/' + '{}/'.format(date_range) + file_name
    download_path = "{}{}".format(base_path, file_name)

    if os.path.exists(save_path):
        print("\nFile already exists! {}".format(save_path))
        return
    if not os.path.exists(save_path):
        Path(os.path.dirname(__file__) + '/data/' + '{}/'.format(date_range)).mkdir(parents=True, exist_ok=True)
    
    try:
        download_url = "https://data.binance.vision/{}".format(download_path)
        dl_file = urllib.request.urlopen(download_url)
        length = dl_file.getheader('content-length')
        if length:
            length = int(length)
            blocksize = max(4096,length//100)

        with open(save_path, 'wb') as out_file:
            dl_progress = 0
            print("\nFile Download: {}".format(save_path))
            while True:
                buf = dl_file.read(blocksize)   
                if not buf:
                    break
                dl_progress += len(buf)
                out_file.write(buf)
                done = int(50 * dl_progress / length)
                sys.stdout.write("\r[%s%s]" % ('#' * done, '.' * (50-done)) )    
                sys.stdout.flush()
    except urllib.error.HTTPError:
        print("\nFile not found: {}".format(download_url))
        pass

def download_daily_aggTrades(trading_type, symbols, num_symbols, dates, start_date, end_date, checksum):
    current = 0
    date_range = start_date + "_" + end_date
    start_date = convert_to_date_object(start_date)
    end_date = convert_to_date_object(end_date)

    print("Found {} symbols".format(num_symbols))

    for symbol in symbols:
        print("[{}/{}] - start downloading daily {} aggTrades ".format(current+1, num_symbols, symbol))
        for date in dates:
            current_date = convert_to_date_object(date)
            if current_date >= start_date and current_date <= end_date:
                path = get_path(trading_type, "aggTrades", "daily", symbol)
                file_name = "{}-aggTrades-{}.zip".format(symbol.upper(), date)
                download_file(path, file_name, date_range)

                if checksum == 1:
                    checksum_path = get_path(trading_type, "aggTrades", "daily", symbol)
                    checksum_file_name = "{}-aggTrades-{}.zip.CHECKSUM".format(symbol.upper(), date)
                    download_file(checksum_path, checksum_file_name, date_range)

        current += 1

if __name__ == "__main__":
    # 'spot' for SPOT
    # 'um' for USD-M Futures 
    # 'cm' for COIN-M Futures
    ACCOUNT_TYPE = 'spot'
    START_DATE = '2022-01-01' 
    END_DATE = '2022-01-05'
    CHECKSUM = 0 # Do not download the checksum file

    symbols = ['BTCUSDT']
    # symbols = get_all_symbols(ACCOUNT_TYPE)
    num_symbols = len(symbols)
    dates = pd.date_range(start = START_DATE, end = END_DATE).to_pydatetime().tolist()
    dates = [date.strftime("%Y-%m-%d") for date in dates]
    download_daily_aggTrades(ACCOUNT_TYPE, symbols, num_symbols, dates, START_DATE, END_DATE, CHECKSUM)