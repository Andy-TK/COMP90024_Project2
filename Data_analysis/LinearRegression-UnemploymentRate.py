# noinspection PyUnresolvedReferences
import numpy as np
# noinspection PyUnresolvedReferences
import xlrd
# noinspection PyUnresolvedReferences
import re
# noinspection PyUnresolvedReferences
import xlwt
# noinspection PyUnresolvedReferences
from openpyxl import Workbook
# noinspection PyUnresolvedReferences
import string
# noinspection PyUnresolvedReferences
import sys
# noinspection PyUnresolvedReferences
import csv
# noinspection PyUnresolvedReferences
import xlsxwriter
# noinspection PyUnresolvedReferences
import pandas
# noinspection PyUnresolvedReferences
import openpyxl
# noinspection PyUnresolvedReferences
from xlutils.copy import copy
# noinspection PyUnresolvedReferences
from xlwt import easyxf
# noinspection PyUnresolvedReferences
import pandas as pd
# noinspection PyUnresolvedReferences
import matplotlib.pyplot as plt
# noinspection PyUnresolvedReferences
import seaborn as sns




def CsvtoXlsx(csvfile):
    wb = Workbook()
    ws = wb.active
    with open(csvfile, "r") as f:
        for row in csv.reader(f):
            ws.append(row)
    wb.save("EMPoutput.xlsx")


def first_word(text: str) -> str:
    return re.search("([\w']+)", text).group(1)


def extract(inpath, formatting_info=True):
    data = xlrd.open_workbook(inpath)
    wb = copy(data)
    ws = wb.get_sheet(0)
    table = data.sheets()[0]  # 选定表
    nrows = table.nrows  # 获取行号
    ncols = table.ncols  # 获取列号

    for i in range(1, nrows):  # 第0行为表头
        alldata = table.row_values(i)  # 循环输出excel表中每一行，即所有数据
        result = alldata[2]  # 取出表中第二列数据
        ##print(result)
        a = result.split(",")
        ws.write(i, 3, a[0])
        print(a[0])
    ws.write(0, 3, "CITY")
    wb.save(inpath)

def extract2(inpath, formatting_info=True):
    data = xlrd.open_workbook(inpath)
    wb = copy(data)
    ws = wb.get_sheet(0)

    table = data.sheets()[0]  # 选定表
    nrows = table.nrows  # 获取行号
    ncols = table.ncols  # 获取列号

    for i in range(1, nrows):  # 第0行为表头
        alldata = table.row_values(i)  # 循环输出excel表中每一行，即所有数据
        result = alldata[0]  # 取出表中第二列数据
        ##print(result)
        b = result.split("(")
        ws.write(i, 2, b[0].rstrip())
        print(b[0])
    ws.write(0, 2, "CITY")
    wb.save(inpath)

def joinTheTable(f1, f2):
    file1 = pd.read_excel(f1)
    file2 = pd.read_excel(f2)
    table = pd.merge(file1, file2, on="CITY")


    table.to_csv("1112.csv")


    print(file1)
    print(file2)
    print(table)


def main():
    file1 = "/Users/zhaohuihou/Desktop/LGAEstimatesofPersonalIncome.csv/angry.xlsx"
    extract(file1)
    file2 = "/Users/zhaohuihou/Desktop/LGAEstimatesofPersonalIncome.csv/unemployment.csv"
    CsvtoXlsx(file2)
    print("-----This is the AURIN Income part-----")
    extract2("EMPoutput.xlsx")

    angryFile = "/Users/zhaohuihou/Desktop/LGAEstimatesofPersonalIncome.csv/angry.xlsx"
    incomeFile = "/Users/zhaohuihou/Desktop/linearRegressionCode/EMPoutput.xlsx"

    joinTheTable(angryFile, incomeFile)

    df = pd.read_csv("/Users/zhaohuihou/Desktop/linearRegressionCode/1112.csv", index_col= 0)

    df.plot.scatter(x='unemploy_Rate', y="angry_value")

    sns.set_style("white")
    sns.set_style("ticks")
    sns.regplot(x='unemploy_Rate', y='angry_value', color="g", data=df)

    plt.show()
    ##file2 = "/Users/zhaohuihou/Desktop/LGAEstimatesofPersonalIncome.csv/data.csv"
    ##extract(file2)




if __name__ == "__main__":
    main();