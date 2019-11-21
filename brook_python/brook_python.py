#!/usr/bin/env python3

import os
from datetime import datetime
from pathlib import Path

DB_NAME = 'some.db'
CUSTOMER_CSV = 'CUSTOMER.CSV'  # UPPERCASE come from assignment
INVOICE_CSV = 'INVOICE.CSV'  # UPPERCASE come from assignment
INVOICE_ITEM_CSV = 'INVOICE_ITEM.CSV'  # UPPERCASE come from assignment
CUSTOMER_SAMPLE_CSV = 'CUSTOMER_SAMPLE.CSV'  # UPPERCASE come from assignment


def move_single_file(fileName, dateAndTimeStamp):
    if os.path.isfile(fileName):
        Path(fileName).rename(os.path.join(dateAndTimeStamp, fileName))


def move_files():
    curr_time = datetime.now()
    dateAndTimeStamp = curr_time.strftime('%m-%d-%Y-%H-%M-%S-%f')

    if not os.path.isdir(dateAndTimeStamp):
        os.makedirs(dateAndTimeStamp)

    move_single_file(CUSTOMER_CSV, dateAndTimeStamp)
    move_single_file(INVOICE_CSV, dateAndTimeStamp)
    move_single_file(INVOICE_ITEM_CSV, dateAndTimeStamp)
    move_single_file(CUSTOMER_SAMPLE_CSV, dateAndTimeStamp)  


if __name__ == "__main__":
    move_files()