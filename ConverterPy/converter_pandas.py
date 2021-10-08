import sys
import pandas as pd


# xl = pd.ExcelFile("Untitled.xlsx")
# df = xl.parse("Sheet1")
# df.head()

# filePath = ("file://D:/NANLI_DEV/STDBToDDA/ConverterPy/Untitled.xlsx")

#pd.read_excel(filePath, sheet_name=0, header=0, names=None, index_col=None, usecols=None, squeeze=False, dtype=None, engine=None, converters=None, true_values=None, false_values=None, skiprows=None, nrows=None, na_values=None, keep_default_na=True, na_filter=True, verbose=False, parse_dates=False, date_parser=None, thousands=None, comment=None, skipfooter=0, convert_float=None, mangle_dupe_cols=True, storage_options=None)

print("Start to Load excel")
ExcelData= pd.read_excel('Untitled.xlsx', index_col=0,dtype = str)
ExcelData2 = ExcelData
#ExcelData2 = ExcelData.astype("string")
#print(ExcelData2.dtypes)
NewExcelDataFrame = pd.DataFrame()


print("total rows: ")
print(len(ExcelData2))

print("Start to process excel")

for x in range(len(ExcelData2)):
    print(x)

    if ExcelData2.iloc[x]["F_Barcode"] == ExcelData2.iloc[x]["B_Barcode"] :
        tempReadData = ExcelData2.iloc[x]
        NewExcelDataFrame = NewExcelDataFrame.append (tempReadData)

    

    elif ExcelData2.iloc[x]["F_Barcode"] != ExcelData2.iloc[x]["B_Barcode"] :

        if ExcelData2.iloc[x]["F_Barcode"] == None and ExcelData2.iloc[x]["B_Barcode"] == None:
            tempReadData = ExcelData2.iloc[x]
            NewExcelDataFrame = NewExcelDataFrame.append (tempReadData)
    
        elif ExcelData2.iloc[x]["F_Barcode"] == None and ExcelData2.iloc[x]["B_Barcode"] !=None:
            tempReadData = ExcelData2.iloc[x]
            tempReadData["F_Barcode"] = tempReadData["B_Barcode"]
            NewExcelDataFrame = NewExcelDataFrame.append (tempReadData)
        
        elif ExcelData2.iloc[x]["F_Barcode"] != None and ExcelData2.iloc[x]["B_Barcode"] ==None:
            tempReadData = ExcelData2.iloc[x]
            NewExcelDataFrame = NewExcelDataFrame.append (tempReadData)



        else:
            tempReadData = ExcelData2.iloc[x]
            NewExcelDataFrame = NewExcelDataFrame.append (tempReadData)

            ExcelData2.iloc[x]["F_Barcode"] = ExcelData2.iloc[x]["B_Barcode"]
            tempReadData = ExcelData2.iloc[x]
            NewExcelDataFrame = NewExcelDataFrame.append (tempReadData)
        
    


print("total rows: ")
print(len(NewExcelDataFrame))
#print(ExcelData.iloc[5]["B_Barcode"])

print("Export to new excel")
NewExcelDataFrame.to_excel(r'export_dataframe.xlsx', index = True, header=True)