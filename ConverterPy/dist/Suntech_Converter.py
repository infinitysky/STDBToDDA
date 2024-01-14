import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox
import sys
import os
import pyodbc 
import pandas as pd
import numpy as np
import xlsxwriter
import xlrd
import wget
import ssl
from tqdm import tqdm


ssl._create_default_https_context = ssl._create_unverified_context

def closesystem():
    sys.exit()

def convertToDDAExcel(SourceData,DDATemplate):
    DDAExcelDataFrame = pd.DataFrame()

    TemplateData=DDATemplate.iloc[0]

    z=0
    lenth=len(SourceData)
    print("Stage 2, Total: ",lenth )
    for z in tqdm(range(len(SourceData))):
        #print(z ," / ",len(SourceData) ," (2)" )
        if pd.notna(SourceData.iloc[z]["F_ItemNo"]):
            TemplateData=DDATemplate.iloc[0]
            TemplateData["ProductCode(15)"] = SourceData.iloc[z]["F_ItemNo"]
            TemplateData["Description1(100)"] = SourceData.iloc[z]["F_Desc"]
            TemplateData["Description2(100)"] = SourceData.iloc[z]["F_Desc2"]
            
            TemplateData["Category(25)"] = SourceData.iloc[z]["CATDES"]

            TemplateData["SalesPrice1(Inc GST)"] = SourceData.iloc[z]["F_Price"]
            TemplateData["WholesalePrice1(Inc GST)"] = SourceData.iloc[z]["F_WPrice"]
            
            TemplateData["LastOrderPrice(Ex GST)"] = SourceData.iloc[z]["F_PurPrice"]

            TemplateData["Barcode1(30)"] = SourceData.iloc[z]["F_Barcode"]
            TemplateData["Barcode2(30)"] = SourceData.iloc[z]["barcode1"]
            TemplateData["Barcode3(30)"] = SourceData.iloc[z]["barcode2"]
            TemplateData["Barcode4(30)"] = SourceData.iloc[z]["barcode3"]
            TemplateData["Barcode5(30)"] = SourceData.iloc[z]["barcode4"]
            TemplateData["Barcode6(30)"] = SourceData.iloc[z]["barcode5"]
            
            TemplateData["Scaleable"] = SourceData.iloc[z]["F_WeightCount"]

            
            

 
        
            if SourceData.iloc[z]["F_TaxCode"] == "GST Free":
                TemplateData["GSTRate"] = 0
            elif SourceData.iloc[z]["F_TaxCode"] == "GST":
                TemplateData["GSTRate"] = 10    

        
      

            TemplateData = TemplateData.to_frame()
            TemplateData = TemplateData.transpose()
                

            DDAExcelDataFrame = pd.concat([DDAExcelDataFrame, TemplateData],ignore_index=True)



    return DDAExcelDataFrame


# INSERT INTO [dbo].[Product] ([ProductCode], [Category], [Description], [SalesPrice1], [SalesPrice2], [SalesPrice3], [SalesPrice4], [LimitStockQty], [GSTRate], [Live], [BarCode], [StockControl], [GSTStatus], [Notes], [LastOrderPrice], [Description1], [Description2], [Description3], [Memorandum], [StockOnOrder], [StockCommitted], [SerialID], [SpecialDate1], [SpecialDate2], [SpecialPrice], [SpecialPrice1], [SpecialPrice2], [SpecialPrice3], [ImageLoadPath], [ShowImage], [StockQty0001], [StockValue0001], [SubDescription], [SubDescription1], [SubDescription2], [SubDescription3], [Barcode1], [Barcode2], [Barcode3], [MultiplePrice], [DeductStockQty], [DeductStockQty1], [DeductStockQty2], [DeductStockQty3], [ManualSelectPrice], [DefaultSalesPrice], [AllowDiscount], [Measurement], [MeasureQty], [Scalable], [OpenPrice], [SpecialDate3], [SpecialDate4], [SpecialDate5], [SpecialDate6], [SpecialDate7], [SpecialDate8], [DefaultSalesQty], [Location], [MetCashCode], [SpecialPriceLinks], [ModifyDate], [SalesPrice5], [SalesPrice6], [SpecialDate9], [SpecialDate10], [SpecialDate11], [SpecialDate12], [SpecialPrice4], [SpecialPrice5], [ItemDiscountRate], [SubDescription4], [SubDescription5], [Barcode4], [Barcode5], [DeductStockQty4], [DeductStockQty5], [ShowOnSelectForm], [DefaultSupplier], [MaxStockQty], [FamilyCode], [SpecialPriceWithoutTerm], [LastEditor], [DepartmentCode], [PackHeight], [PackWidth], [PackLength], [SpecialKind], [ButtonColor], [FontName], [FontColor], [FontSize], [FontBold], [FontItalic], [FontUnderline], [FontStrikeout], [PackMeasurement], [UnitMeasurement], [Metric], [Weight], [WholesalePrice], [WholesalePrice1], [WholesalePrice2], [WholesalePrice3], [WholesalePrice4], [WholesalePrice5], [FamilyCode1], [FamilyCode2], [FamilyCode3], [FamilyCode4], [FamilyCode5], [SpecCode], [TareWeight], [OnlyPrice1CanBeDiscount], [BestBefore], [CalcSalesCostKind], [PrintJobListItem], [OnlineOrderItem], [ExpectedCostIncludeGST], [XeroTaxCode], [SpecialQtyLimit1], [SpecialQtyLimit2], [SpecialQtyLimit3], [SpecialQtyLimit4], [SpecialQtyLimit5], [SpecialQtyLimit6], [SpecialQty1], [SpecialQty2], [SpecialQty3], [SpecialQty4], [SpecialQty5], [SpecialQty6], [ConsolidateMode], [RewardPointsMode], [OnlinePrice1], [OnlinePrice2], [OnlinePrice3], [OnlinePrice4], [OnlinePrice5], [OnlinePrice6]) VALUES (N'A1000002', N'ACCESSORIES', N'128GB Kingston Canvas Select+ SDCS2 Micro SD Card', 56.4782608695652, 0, 0, 0, 0, 15, '1', N'740617298703', '0', '1', NULL, 25.06, NULL, NULL, NULL, NULL, 0, 0, 0, NULL, NULL, 0, 0, 0, 0, N'0.00', '0', 0, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '0', 1, 1, 1, 1, '0', 0, '1', NULL, 1, '0', '1', NULL, NULL, NULL, NULL, NULL, NULL, 1, N'ACC WH', NULL, 0, '2022-11-24 00:00:00.000', 0, 0, NULL, NULL, NULL, NULL, 0, 0, 0, NULL, NULL, NULL, NULL, 1, 1, '1', NULL, 0, NULL, '0', N'ZIISUPPORT', N'D011', 0, 0, 0, 0, 12632256, N'Arial', 0, 8, '1', '0', '0', '0', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, NULL, NULL, NULL, NULL, NULL, NULL, 0, '1', 0, NULL, '0', '0', '0', N'GST on income', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 0, 0, 0, 0, 0);


def processBarcodes(productList,productBarcodeList):
    finalResult = pd.DataFrame()
    finalResult["barcode1"]=""
    finalResult["barcode2"]=""
    finalResult["barcode3"]=""
    finalResult["barcode4"]=""
    finalResult["barcode5"]=""
    z=0
    lenth=len(productList)
    print("Stage 1, Total: ",lenth )
    for z in tqdm(range(len(productList))):
        #print(z ," / ",lenth, " (1)" )
        TemplateData = productList.iloc[z]
        
        
        T1= pd.DataFrame()
        
        T1=productBarcodeList[productBarcodeList["F_ItemNo"] == TemplateData['F_ItemNo']]
  
        barCodeLength = len(T1)
        
        #print(barCodeLength)
        if barCodeLength > 1:
            y=0
            for y in range (barCodeLength):
                if T1.iloc[y]["F_Barcode"] !=TemplateData["F_Barcode"]:
                    name="barcode"+ str(y+1)
                    TemplateData[name]=T1.iloc[y]["F_Barcode"]
            

        
        TemplateData = TemplateData.to_frame()
        TemplateData = TemplateData.transpose()
        finalResult = pd.concat([finalResult, TemplateData],ignore_index=True)
           

    return finalResult


         


def processProductWithBarCode(connect_string):
    PassSQLServerConnection = pyodbc.connect(connect_string)

  

    productListQuery = "SELECT TProduct.*, TCat.F_CatDesc as CATDES FROM TProduct, TCat where TProduct.F_CatCode = TCat.F_CatCode   order by F_ItemNo"
    productbarcodeListQuery = "select F_ItemNo, MAX(CASE when a.rowNum=1 THEN F_Barcode else '' end) barcode1, MAX(CASE when a.rowNum=2 THEN F_Barcode else '' end) barcode2, MAX(CASE when a.rowNum=3 THEN F_Barcode else '' end) barcode3, MAX(CASE when a.rowNum=4 THEN F_Barcode else '' end) barcode4, MAX(CASE when a.rowNum=5 THEN F_Barcode else '' end) barcode5, MAX(CASE when a.rowNum=6 THEN F_Barcode else '' end) barcode6  from( select *,ROW_NUMBER( ) OVER ( PARTITION BY F_ItemNo ORDER BY F_Barcode  ) AS rowNum from TBarcode )a GROUP BY F_ItemNo;"

   

    productList = pd.read_sql_query(productListQuery, PassSQLServerConnection)
    productBarcodeList =  pd.read_sql_query(productbarcodeListQuery, PassSQLServerConnection)

    result=processBarcodes(productList,productBarcodeList)

    print("total rows: ")
    print(len(result))

 

    print("Export to new excel")
    result.to_excel(r'export_dataframe.xlsx', index = True, header=True,engine='xlsxwriter')
    print("Stage 1 Process completed")

    print("Start convert to DDA")
    DDAExcel = pd.DataFrame()

    try:
        downloadURL="https://download.ziicloud.com/programs/ziiposclassic/ItemImportFormat.xls"
        local_file="ItemImportFormat.xls"
        wget.download(downloadURL, local_file)
    except wget.Error as ex:
        print("Download Files error")
        

    DDADataTemplete = pd.read_excel('ItemImportFormat.xls', index_col=None,dtype = str)
    #DDAExcel=DDADataTemplete.astype(str)
    DDAExcel =DDADataTemplete

    DDAExcel = convertToDDAExcel(result,DDAExcel)

    DDAExcel.to_excel(r'outPut.xlsx', index = False, header=True,engine='xlsxwriter')
    messagebox.showinfo(title="Process Completed",message="Data Process Completed")




    
def ConnectionTest(connect_string):
    connectionTestResult = 0
   
    PassSQLServerConnection = pyodbc.connect(connect_string)

    print(connect_string)
    try:
        PassSQLServerConnection = pyodbc.connect(connect_string)
        print("{c} is working".format(c=connect_string))
        PassSQLServerConnection.close()
        connectionTestResult = 1
    except pyodbc.Error as ex:
        #print("{c} is not working".format(c=connect_string))
        messagebox.showerror(title="Error", message="{c} is not working")

    return connectionTestResult


def inforProcess(DBSource,DBUsername,DBPassword,DBName):
    connectionTestResult=0
    connect_string = 'DRIVER={SQL Server}; SERVER='+DBSource+'; DATABASE='+DBName+'; UID='+DBUsername+'; PWD='+ DBPassword
    if DBName=="":
        messagebox.showerror(title="Error", message="DB Name Field is Empty!!")
        connectionTestResult = 0
    else:
        connectionTestResult=ConnectionTest(connect_string)

    if connectionTestResult==1:
        print("next")
        processProductWithBarCode(connect_string)

    else:
        print("error")







class App:
    def __init__(self, root):
        #setting title
        root.title("Suntech Converter")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_DB_Source=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_DB_Source["font"] = ft
        GLabel_DB_Source["fg"] = "#333333"
        GLabel_DB_Source["justify"] = "left"
        GLabel_DB_Source["text"] = "DB Connection"
        GLabel_DB_Source.place(x=50,y=90,width=90,height=30)

        DBSource_Box=tk.Entry(root)
        DBSource_Box["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        DBSource_Box["font"] = ft
        DBSource_Box["fg"] = "#333333"
        DBSource_Box["justify"] = "left"
        DBSource_Box.insert(0,'localhost\sqlexpress2008r2')
        #DBSource_Box["text"] = "localhost\sqlexpress2008r2"
        
        DBSource_Box.place(x=190,y=90,width=275,height=30)

        DB_UserName_Label=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        DB_UserName_Label["font"] = ft
        DB_UserName_Label["fg"] = "#333333"
        DB_UserName_Label["justify"] = "left"
        DB_UserName_Label["text"] = "User Name"
        DB_UserName_Label.place(x=50,y=140,width=90,height=30)

        DB_UserName_Box=tk.Entry(root)
        DB_UserName_Box["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        DB_UserName_Box["font"] = ft
        DB_UserName_Box["fg"] = "#333333"
        DB_UserName_Box["justify"] = "left"
        #DB_UserName_Box["text"] = "sa"
        DB_UserName_Box.insert(0,'sa')
        DB_UserName_Box.place(x=190,y=140,width=275,height=30)

        DB_Password_Label=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        DB_Password_Label["font"] = ft
        DB_Password_Label["fg"] = "#333333"
        DB_Password_Label["justify"] = "left"
        DB_Password_Label["text"] = "Password"
        DB_Password_Label.place(x=50,y=200,width=90,height=25)

        DB_Password_Box=tk.Entry(root)
        DB_Password_Box["borderwidth"] = "1px"
        
        ft = tkFont.Font(family='Times',size=10)
        DB_Password_Box["font"] = ft
        DB_Password_Box["fg"] = "#333333"
        DB_Password_Box["justify"] = "left"
        #DB_Password_Box["text"] = "0000"
        DB_Password_Box.insert(0,'0000')
        DB_Password_Box.place(x=190,y=200,width=275,height=30)
        DB_Password_Box["show"] = "*"

        
        
        DB_Name_Label=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        DB_Name_Label["font"] = ft
        DB_Name_Label["fg"] = "#333333"
        DB_Name_Label["justify"] = "left"
        DB_Name_Label["text"] = "DB Name"
        DB_Name_Label.place(x=50,y=260,width=90,height=25)

        DB_Name_Box=tk.Entry(root)
        DB_Name_Box["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        DB_Name_Box["font"] = ft
        DB_Name_Box["fg"] = "#333333"
        DB_Name_Box["justify"] = "left"    
        DB_Name_Box.place(x=190,y=260,width=275,height=30)
        #DB_Name_Box.insert(0,'AUPOS_F')
 









         #-----------------Functions---------------------------------
        def getDBSource():
            result=DBSource_Box.get()
            return result
           
            
        def getDBUsername():
            result=DB_UserName_Box.get()
            return result
      
        def getDBPassword():
            result=DB_Password_Box.get()
            return result
        
        def getDBName():
            result=DB_Name_Box.get()
            return result
      
        
        def StartConversionProcess():
            DBSource=getDBSource()
            username=getDBUsername()
            password=getDBPassword()
            databaseName=getDBName()
            #inforProcess(DBSource,DBUsername,DBPassword,DBName):
            inforProcess(DBSource,username,password,databaseName)
            

        def testDBSource():
            DBSource=getDBSource()
            username=getDBUsername()
            password=getDBPassword()
            databaseName=getDBName()
            connect_string = 'DRIVER={SQL Server}; SERVER='+DBSource+'; DATABASE='+databaseName+'; UID='+username+'; PWD='+ password
            PassSQLServerConnection = pyodbc.connect(connect_string)
            if databaseName=="":
                messagebox.showerror(title="Error", message="DB Name Field is Empty!!")
            else:
                try:
                    PassSQLServerConnection = pyodbc.connect(connect_string)
                    print("{c} is working".format(c=connect_string))
                    PassSQLServerConnection.close()
                except pyodbc.Error as ex:
               
                    print("{c} is not working".format(c=connect_string))
                    messagebox.showerror(title="Error", message="{c} is not working")
          
            




            
            


            
            
        
        
        

            















        



            
#--------------Button Actions-------------------------
        Star_Button=tk.Button(root)
        Star_Button["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        Star_Button["font"] = ft
        Star_Button["fg"] = "#000000"
        Star_Button["justify"] = "center"
        Star_Button["text"] = "Start"
        Star_Button.place(x=70,y=390,width=90,height=45)
        Star_Button["command"] = StartConversionProcess

        TEST_Button=tk.Button(root)
        TEST_Button["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        TEST_Button["font"] = ft
        TEST_Button["fg"] = "#000000"
        TEST_Button["justify"] = "center"
        TEST_Button["text"] = "Test DB"
        TEST_Button.place(x=250,y=390,width=90,height=45)
        TEST_Button["command"] = testDBSource

        Close_Button=tk.Button(root)
        Close_Button["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        Close_Button["font"] = ft
        Close_Button["fg"] = "#000000"
        Close_Button["justify"] = "center"
        Close_Button["text"] = "Close"
        Close_Button.place(x=420,y=390,width=90,height=45)
        Close_Button["command"] = closesystem
       
        




#----------------Not in use--------------------------------
    def Star_Button_command(self):
        print("Star_Button_command")
    def TEST_Button_command(self):
        print("command")
    def Close_Button_command(self):
        print("Exit")
        exit()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
