import sys
import os
import pyodbc 
import pandas as pd
import numpy as np

import timeit


def main():
    
    server = 'Ziitech-Server\SQLExpress2008R2'
    database = 'Pacific_Pines_2021'
    username = 'ZiiPos'
    password = 'ZiiPos884568'

    #Password Connection
    PassSQLServerConnection = pyodbc.connect('DRIVER={SQL Server}; SERVER='+server+'; DATABASE='+database+'; UID='+username+'; PWD='+ password)
    #Windows Auth
    #WindowsAuthSQLServerConnection = pyodbc.connect('DRIVER={SQL Server}; SERVER='+server+'; DATABASE='+database+'; Trusted_Connection=True;' )

    #cursor = PassSQLServerConnection.cursor()
    linkedQuery = "SELECT TProduct.*, TBarcode.F_Barcode AS B_Barcode, TBarcode.F_ItemNo AS B_ItemNo, TBarcode.F_AuotoNo AS B_AutoNo FROM TProduct, TBarcode WHERE TProduct.F_ItemNo = TBarcode.F_ItemNo "

    NonLinkedQuery = "SELECT TProduct.* FROM TProduct WHERE TProduct.F_ItemNo NOT IN ( SELECT TProduct.F_ItemNo FROM TProduct, TBarcode WHERE TProduct.F_ItemNo = TBarcode.F_ItemNo) "

    SqlResult1 = pd.read_sql(linkedQuery, PassSQLServerConnection)
    SqlResult2 = pd.read_sql(NonLinkedQuery, PassSQLServerConnection)

  
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
    DDAExcel = pd.DataFrame()
    DDADataTemplete = pd.read_excel('DDA_Templet.xlsx', index_col=None,dtype = str)
    DDAExcel=DDADataTemplete.astype("string")

    DDAExcel = convertToDDAExcel(NewExcelDataFrame,DDAExcel)

    DDAExcel.to_excel(r'DDA.xls', index = False, header=True)







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
    
    for z in range(len(SourceExcelDataFrame)):
        print(z ," / ",len(SourceExcelDataFrame))
        
       
        if pd.notna(SourceExcelDataFrame.iloc[z]["F_ItemNo"]):          
            
            tempReadData = SourceExcelDataFrame.iloc[z]
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


            DDATemplete = DDATemplete.append (tempReadData)

        
        #del df['column_name']
        #PreProcessData.drop(columns=['B_AutoNo', 'B_Barcode', 'B_ItemNo', 'F_Actor', 'F_AutoNo', 'F_AvgCost' ,'F_Barcode', 'F_CatCode', 'F_Color', 'F_CommissionRate', 'F_DeliveryRuleCode', 'F_Desc', 'F_Desc2' ,'F_Discount', 'F_ExpiryDate', 'F_ForRental', 'F_GST', 'F_HasExpiry', 'F_Hotkey', 'F_HotkeyIndex', 'F_ISDiscontinue', 'F_InFav', 'F_IsForPayout', 'F_IsProductSet', 'F_IsPromoPrice', 'F_IsShowOnWeb', 'F_ItemNo', 'F_LastRetailPrice', 'F_LocationDiscount', 'F_MINQTY', 'F_ManualOrder', 'F_MultiRetailPrice', 'F_NotAllowMemberDiscount', 'F_NotShowInPanel', 'F_PGST', 'F_Price', 'F_ProductTypeCode', 'F_PromPageOrder', 'F_PromPrice', 'F_PromPriceGST', 'F_PurPrice', 'F_PurTaxCode', 'F_ReleaseDate', 'F_RentalPeriod', 'F_ReorderQty', 'F_RuleCode', 'F_Size', 'F_StockPlace', 'F_StyleNo', 'F_SubCatCode', 'F_SupplieIDNo', 'F_SupplierNo', 'F_SyncLoc', 'F_TaxCode', 'F_TimeStamp', 'F_Title','F_TotalCopies', 'F_TouchOrder', 'F_Unit', 'F_Volume', 'F_WGST', 'F_WPrice', 'F_WRRate', 'F_WareHouse', 'F_WebImage', 'F_WebLongDesc', 'F_WebLongDesc2', 'F_WebPrice', 'F_WebPriceGST', 'F_WebSync', 'F_Weight', 'F_WeightCount', 'F_buttonType', 'F_picture'])





    
   
   
    
    del DDATemplete['B_AutoNo']
    del DDATemplete['B_Barcode']
    del DDATemplete['B_ItemNo']
    del DDATemplete['F_Actor']
    del DDATemplete['F_AutoNo']
    del DDATemplete['F_AvgCost']
    del DDATemplete['F_Barcode']
    del DDATemplete['F_CatCode']
    del DDATemplete['F_Color']
    del DDATemplete['F_CommissionRate']
    del DDATemplete['F_DeliveryRuleCode']
    del DDATemplete['F_Desc']
    del DDATemplete['F_Desc2']
    del DDATemplete['F_Discount']
    del DDATemplete['F_ExpiryDate']
    del DDATemplete['F_ForRental']
    del DDATemplete['F_GST']
    del DDATemplete['F_HasExpiry']
    del DDATemplete['F_Hotkey']
    del DDATemplete['F_HotkeyIndex']
    del DDATemplete['F_ISDiscontinue']
    del DDATemplete['F_InFav']
    del DDATemplete['F_IsForPayout']
    del DDATemplete['F_IsProductSet']
    del DDATemplete['F_IsPromoPrice']
    del DDATemplete['F_IsShowOnWeb']
    del DDATemplete['F_ItemNo']
    del DDATemplete['F_LastRetailPrice']
    del DDATemplete['F_LocationDiscount']
    del DDATemplete['F_MINQTY']
    del DDATemplete['F_ManualOrder']
    del DDATemplete['F_MultiRetailPrice']
    del DDATemplete['F_NotAllowMemberDiscount']
    del DDATemplete['F_NotShowInPanel']
    del DDATemplete['F_PGST']
    del DDATemplete['F_Price']
    del DDATemplete['F_ProductTypeCode']
    del DDATemplete['F_PromPageOrder']
    del DDATemplete['F_PromPrice']
    del DDATemplete['F_PromPriceGST']
    del DDATemplete['F_PurPrice']
    del DDATemplete['F_PurTaxCode']
    del DDATemplete['F_ReleaseDate']
    del DDATemplete['F_RentalPeriod']
    del DDATemplete['F_ReorderQty']
    del DDATemplete['F_RuleCode']
    del DDATemplete['F_Size']
    del DDATemplete['F_StockPlace']
    del DDATemplete['F_StyleNo']
    del DDATemplete['F_SubCatCode']
    del DDATemplete['F_SupplieIDNo']
    del DDATemplete['F_SupplierNo']
    del DDATemplete['F_SyncLoc']
    del DDATemplete['F_TaxCode']
    del DDATemplete['F_TimeStamp']
    del DDATemplete['F_Title']
    del DDATemplete['F_TotalCopies']
    del DDATemplete['F_TouchOrder']
    del DDATemplete['F_Unit']
    del DDATemplete['F_Volume']
    del DDATemplete['F_WGST']
    del DDATemplete['F_WPrice']
    del DDATemplete['F_WRRate']
    del DDATemplete['F_WareHouse']
    del DDATemplete['F_WebImage']
    del DDATemplete['F_WebLongDesc']
    del DDATemplete['F_WebLongDesc2']
    del DDATemplete['F_WebPrice']
    del DDATemplete['F_WebPriceGST']
    del DDATemplete['F_WebSync']
    del DDATemplete['F_Weight']
    del DDATemplete['F_WeightCount']
    del DDATemplete['F_buttonType']
    del DDATemplete['F_picture'] 

    




    return DDATemplete


main()

