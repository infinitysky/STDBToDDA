import sys
import os
import pyodbc 
import pandas as pd
import numpy as np
from numba import jit
import timeit


def main():
    
    server = 'localhost,9899'
    database = 'Pacific_Pinesold'
    username = 'sa'
    password = '0000'

    #Password Connection
    PassSQLServerConnection = pyodbc.connect('DRIVER={SQL Server}; SERVER='+server+'; DATABASE='+database+'; UID='+username+'; PWD='+ password)
    #Windows Auth
    #WindowsAuthSQLServerConnection = pyodbc.connect('DRIVER={SQL Server}; SERVER='+server+'; DATABASE='+database+'; Trusted_Connection=True;' )

    #cursor = PassSQLServerConnection.cursor()
    linkedQuery = "SELECT top 100 TProduct.*, TBarcode.F_Barcode AS B_Barcode, TBarcode.F_ItemNo AS B_ItemNo, TBarcode.F_AuotoNo AS B_AutoNo FROM TProduct, TBarcode WHERE TProduct.F_ItemNo = TBarcode.F_ItemNo "

    NonLinkedQuery = "SELECT top 100 TProduct.* FROM TProduct WHERE TProduct.F_ItemNo NOT IN ( SELECT TProduct.F_ItemNo FROM TProduct, TBarcode WHERE TProduct.F_ItemNo = TBarcode.F_ItemNo) "

    SqlResult1 = pd.read_sql(linkedQuery, PassSQLServerConnection)
    SqlResult2 = pd.read_sql(NonLinkedQuery, PassSQLServerConnection)

    # ExcelData= pd.read_excel('20211013.xls', index_col=0,dtype = str)

    # unprocessedExcelData1 = ExcelData1.astype("string")
    # unprocessedExcelData2 = ExcelData2.astype("string")

    # wtData1=SqlResult1.astype("string")
    # wtData2=SqlResult2.astype("string")

    # wtData1.to_excel(r'linkedData.xlsx', index = True, header=True)
    # wtData2.to_excel(r'unlinked.xlsx', index = True, header=True)



    # ExcelData1= pd.read_excel('linkedData.xlsx', index_col=0,dtype = str)
    # ExcelData2= pd.read_excel('unlinked.xlsx', index_col=0,dtype = str)

    # unprocessedExcelData1 = ExcelData1.astype("string")
    # unprocessedExcelData2 = ExcelData2.astype("string")

    unprocessedExcelData1 = SqlResult1.astype("string")
    unprocessedExcelData2 = SqlResult2.astype("string")

    NewExcelDataFrame = pd.DataFrame()


    print("total Linke rows: ")
    print(len(unprocessedExcelData1))

    print("total unlinked rows: ")
    print(len(unprocessedExcelData2))

    NewExcelDataFrame=processLinkedList(unprocessedExcelData1,NewExcelDataFrame)
    NewExcelDataFrame=processUnlinkedList(unprocessedExcelData2,NewExcelDataFrame)

    print("total rows: ")
    print(len(NewExcelDataFrame))

    print("Export to new excel")
    NewExcelDataFrame.to_excel(r'export_dataframe.xlsx', index = True, header=True)
    print("Process completed")

    print("Start convert to DDA")
    DDADataTemplete = pd.read_excel('DDA_Templet.xlsx', index_col=0,dtype = str)
    DDADataTemplete=DDADataTemplete.astype("string")
    DDAExcel = convertToDDAExcel(NewExcelDataFrame,DDADataTemplete)
    DDAExcel.to_excel(r'DDA.xlsx', index = True, header=True)





def processLinkedList(unprocessedExcelData1, NewExcelDataFrame):
    x=0
    for x in range(len(unprocessedExcelData1)):
        print(x ," / ",len(unprocessedExcelData1))

        # Empty F_Barcode & Empty B_Barcode 
        if pd.isna(unprocessedExcelData1.iloc[x]["F_Barcode"]) and pd.isna(unprocessedExcelData1.iloc[x]["B_Barcode"]):
            tempReadData = unprocessedExcelData1.iloc[x]
            NewExcelDataFrame = NewExcelDataFrame.append (tempReadData)
        

        # Empty F_Barcode  
        elif pd.isna(unprocessedExcelData1.iloc[x]["F_Barcode"]) and pd.notna(unprocessedExcelData1.iloc[x]["B_Barcode"]):
            tempReadData = unprocessedExcelData1.iloc[x]
            tempReadData["F_Barcode"] = tempReadData["B_Barcode"]
            NewExcelDataFrame = NewExcelDataFrame.append (tempReadData)
            
                
        # Empty B_Barcode      
        elif pd.notna(unprocessedExcelData1.iloc[x]["F_Barcode"]) and pd.isna(unprocessedExcelData1.iloc[x]["B_Barcode"]):
            tempReadData = unprocessedExcelData1.iloc[x]
            tempReadData["F_Barcode"] = tempReadData["B_Barcode"]
            NewExcelDataFrame = NewExcelDataFrame.append (tempReadData)
        


        elif pd.notna(unprocessedExcelData1.iloc[x]["F_Barcode"]) and pd.notna(unprocessedExcelData1.iloc[x]["B_Barcode"]):
            if  unprocessedExcelData1.iloc[x]["F_Barcode"] == unprocessedExcelData1.iloc[x]["B_Barcode"]:
                tempReadData = unprocessedExcelData1.iloc[x]
                NewExcelDataFrame = NewExcelDataFrame.append (tempReadData)
            
            
            elif unprocessedExcelData1.iloc[x]["F_Barcode"] != unprocessedExcelData1.iloc[x]["B_Barcode"]:
                tempReadData = unprocessedExcelData1.iloc[x]
                NewExcelDataFrame = NewExcelDataFrame.append (tempReadData)

                tempReadData = unprocessedExcelData1.iloc[x]
                tempReadData["F_Barcode"] = unprocessedExcelData1.iloc[x]["B_Barcode"]
                NewExcelDataFrame = NewExcelDataFrame.append (tempReadData)
        
    return NewExcelDataFrame
                

def processUnlinkedList(unprocessedExcelData2, NewExcelDataFrame):
   
    for y in range(len(unprocessedExcelData2)):
        print(y ," / ",len(unprocessedExcelData2))
        tempReadData = unprocessedExcelData2.iloc[y]
        NewExcelDataFrame = NewExcelDataFrame.append (tempReadData)

    return NewExcelDataFrame

def convertToDDAExcel(SourceExcelDataFrame,DDATemplete):
    z=0
    tempReadData = pd.DataFrame()
    for z in range(len(SourceExcelDataFrame)):
        print(z ," / ",len(SourceExcelDataFrame))

        if pd.isna(SourceExcelDataFrame.iloc[z]["F_ItemNo"]) or pd.isna(SourceExcelDataFrame.iloc[z]["F_Barcode"]):
            z=z+1
        else:    
            tempReadData["Product Code"] = SourceExcelDataFrame.iloc[z]["F_Barcode"]
            tempReadData["Description1"] = SourceExcelDataFrame.iloc[z]["F_Desc"]
            tempReadData["Description2"] = SourceExcelDataFrame.iloc[z]["F_Desc2"]
            tempReadData["Category"] = SourceExcelDataFrame.iloc[z]["F_CatCode"]
            tempReadData["Barcode1"] = SourceExcelDataFrame.iloc[z]["F_Barcode"]
            tempReadData["Price1"] = SourceExcelDataFrame.iloc[z]["F_Price"]
            tempReadData["Last P/O Price"] = SourceExcelDataFrame.iloc[z]["F_PurPrice"]
            
        
        
        if SourceExcelDataFrame.iloc[z]["F_TaxCode"] == "GST Free":
            tempReadData["GST(%)"] = 0
        elif SourceExcelDataFrame.iloc[z]["F_TaxCode"] == "GST":
            tempReadData["GST(%)"] = 10

        print(tempReadData)
        DDATemplete = DDATemplete.append (tempReadData)


        


    
    return DDATemplete


main()

