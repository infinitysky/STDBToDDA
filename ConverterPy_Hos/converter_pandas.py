from distutils.util import rfc822_escape
import sys
import os
import pyodbc 
import pandas as pd
import numpy as np





def main():
    
    server = 'localhost\SQLExpress2008R2'
    database = 'DUCKYOLD'
    username = 'ZiiPos'
    password = 'ZiiPos884568'

    #Password Connection
    PassSQLServerConnection = pyodbc.connect('DRIVER={SQL Server}; SERVER='+server+'; DATABASE='+database+'; UID='+username+'; PWD='+ password)
    #Windows Auth
    #WindowsAuthSQLServerConnection = pyodbc.connect('DRIVER={SQL Server}; SERVER='+server+'; DATABASE='+database+'; Trusted_Connection=True;' )

    #cursor = PassSQLServerConnection.cursor()
    CategoryQuery = "SELECT * FROM TCat;"

    MenuItemQuery = "SELECT TProduct.*, TCat.F_CatDesc as CateDEC FROM TProduct, TCat where TProduct.F_CatCode=TCat.F_CatCode;"

    SqlResult1 = pd.read_sql(CategoryQuery, PassSQLServerConnection)
    SqlResult2 = pd.read_sql(MenuItemQuery, PassSQLServerConnection)

  
    unprocessedExcelData1 = SqlResult1.astype("string")
    unprocessedExcelData2 = SqlResult2.astype("string")

    NewExcelDataFrame = pd.DataFrame()
  
    NewExcelDataFrame = unprocessedExcelData1
    print("total Linke rows: ")
    print(len(unprocessedExcelData1))

    print("total unlinked rows: ")
    print(len(unprocessedExcelData2))


    xls = pd.ExcelFile('ZiiPOS_template.xls')


    #NewExcelDataFrame=processLinkedList(unprocessedExcelData1,NewExcelDataFrame)
    #NewExcelDataFrame=processUnlinkedList(unprocessedExcelData2,NewExcelDataFrame)

    print("total rows: ")
    #print(len(NewExcelDataFrame))

    print("Export to new excel")
    NewExcelDataFrame.to_excel(r'unprocessedExcelData1.xlsx', index = True, header=True)
    print("Process completed")

    #print("Start convert to DDA")
    #DDAExcel = pd.DataFrame()
    #DDADataTemplete = pd.read_excel('DDA_Templet.xlsx', index_col=None,dtype = str)
    #DDAExcel=DDADataTemplete.astype("string")

    #DDAExcel = convertToDDAExcel(NewExcelDataFrame,DDAExcel)

    #DDAExcel.to_excel(r'DDA.xls', index = False, header=True)



def processCate(cate):
    



main()

