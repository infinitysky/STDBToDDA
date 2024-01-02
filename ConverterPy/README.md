﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿* Database convertor

```sql

SELECT
	TProduct.*, 
	TBarcode.F_Barcode AS B_Barcode, 
	TBarcode.F_ItemNo AS B_ItemNo, 
	TBarcode.F_AuotoNo AS B_AutoNo
FROM
	dbo.TProduct,
	dbo.TBarcode
WHERE
	TProduct.F_ItemNo = TBarcode.F_ItemNo



SELECT TProduct.*, TBarcode.F_Barcode AS B_Barcode, TBarcode.F_ItemNo AS B_ItemNo, TBarcode.F_AuotoNo AS B_AutoNo FROM TProduct, TBarcode WHERE TProduct.F_ItemNo = TBarcode.F_ItemNo

```



```sql
SELECT
	TProduct.* 
FROM
	TProduct 
WHERE
	TProduct.F_ItemNo NOT IN ( SELECT TProduct.F_ItemNo FROM TProduct, TBarcode WHERE TProduct.F_ItemNo = TBarcode.F_ItemNo )SELECT
	TProduct.* 


SELECT TProduct.* FROM TProduct WHERE TProduct.F_ItemNo NOT IN ( SELECT TProduct.F_ItemNo FROM TProduct, TBarcode WHERE TProduct.F_ItemNo = TBarcode.F_ItemNo)

```





```sql

    SELECT TProduct.*, TCat.F_CatDesc as CATDES FROM TProduct, TCat where TProduct.F_CatCode = TCat.F_CatCode   order by F_ItemNo;

    Select F_ItemNo, MAX(CASE when a.rowNum=1 THEN F_Barcode else '' end) barcode1, MAX(CASE when a.rowNum=2 THEN F_Barcode else '' end) barcode2, MAX(CASE when a.rowNum=3 THEN F_Barcode else '' end) barcode3, MAX(CASE when a.rowNum=4 THEN F_Barcode else '' end) barcode4, MAX(CASE when a.rowNum=5 THEN F_Barcode else '' end) barcode5, MAX(CASE when a.rowNum=6 THEN F_Barcode else '' end) barcode6  from( select *,ROW_NUMBER( ) OVER ( PARTITION BY F_ItemNo ORDER BY F_Barcode  ) AS rowNum from TBarcode )a GROUP BY F_ItemNo;


```




