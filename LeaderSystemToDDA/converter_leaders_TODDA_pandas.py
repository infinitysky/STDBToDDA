import sys
import os
import pyodbc 
import pandas as pd
import numpy as np

import timeit


def main():
    
    LeaderPriceListData = pd.read_excel('leaderData.xlsx', index_col=None,dtype = str)

    catagoryList=LeaderPriceListData
    catagoryList=catagoryList.drop_duplicates(subset=['Category'])
    catagoryList.to_excel(r'catagoryList.xlsx', index = False, header=True)
   


    print("total unlinked rows: ")
    print(len(LeaderPriceListData))


    print("Start convert to DDA")
    DDAExcel = pd.DataFrame()
    DDADataTemplete = pd.read_excel('DDD.xlsx', index_col=None,dtype = str)
    DDAExcel=DDADataTemplete.astype("string")
    DDAExcel = convertToDDAExcel(LeaderPriceListData,DDAExcel)

    DDAExcel.to_excel(r'Final.xls', index = False, header=True)
    print(DDAExcel)




def convertToDDAExcel(SourceExcelDataFrame,DDATemplete):
    z=0
       
    templateDDAData = DDATemplete.iloc[0]
    templateDDAData = templateDDAData.to_frame()
    templateDDAData = templateDDAData.transpose()

    DDAData= pd.DataFrame()
    for z in range(len(SourceExcelDataFrame)):
        print(z ," / ",len(SourceExcelDataFrame))
        
       
        if SourceExcelDataFrame.iloc[z]["Single_Price"] == "Single":
            z=z+1          
            
            
        else:
            tempReadData = templateDDAData
            tempReadData["ProductCode(15)"] = SourceExcelDataFrame.iloc[z]["Stock Code"]
            tempReadData["Description1(100)"] = SourceExcelDataFrame.iloc[z]["Stock Name"]
            tempReadData["Description2(100)"] = ""
            tempReadData["Category(25)"] = SourceExcelDataFrame.iloc[z]["Category"]
            tempReadData["SalesPrice5(Inc GST)"] = SourceExcelDataFrame.iloc[z]["RRP_Price"]
            tempReadData["SalesPrice2(Inc GST)"] = "0"
            
            tempReadData["SalesPrice5(Inc GST)"] = SourceExcelDataFrame.iloc[z]["Single_Price"]
            tempReadData["LastOrderPrice(Ex GST)"] = SourceExcelDataFrame.iloc[z]["Single_Price"]
        

            tempReadData["GSTRate"] = "10"
   


            DDAData = pd.concat([DDAData, tempReadData],ignore_index=False)

    return DDAData


main()

