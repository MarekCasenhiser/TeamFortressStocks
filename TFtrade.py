import steammarket as sm
import re
import time
from datetime import datetime
import csv
#import numpy as np
import json
import numpy as np
hour = 60*60

MyItem = 'Gruesome Gourd'

def TF2_analyzer(items,keys, recorded):
    

    price = {"Name": MyItem, "NumberSold": items["volume"], "MedianPrice": items["median_price"], "Date": recorded}
    key_price = {"Name": "Mann Co. Supply Crate Key", "LowestPrice": keys["lowest_price"], "NumberSold": keys["volume"], "MedianPrice": keys["median_price"], "Date": recorded}
    field_names = ['Name', 'LowestPrice','NumberSold', 'MedianPrice', 'Date']
    print("Running Stats")
    print(price)
    print(key_price)
    


    
    with open('TFData.csv', 'a', newline='') as file:
        dict_object = csv.DictWriter(file, fieldnames=field_names)
        dict_object.writerow(price)
        dict_object.writerow(key_price)
    


    time.sleep(hour)
    

while True:
    print("TFtrade has started updating...")
    key = sm.get_tf2_item('Mann Co. Supply Crate Key', currency = 'USD')
    item = sm.get_tf2_item(MyItem, currency = 'USD')
    event = datetime.now()
    current_time = event.strftime('%H:%M:%S')
    TF2_analyzer(item,key,current_time)