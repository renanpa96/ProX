SELECT 
	T.po_line
    , T._qty_
FROM MRP AS M
 LEFT JOIN Tracking T
 on T.concat_poline = M.MRP_element_data
 
 WHERE lower (status) = "waiting invoice"
 	



;