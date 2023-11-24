SELECT  
	po
	, po_line
    , total
    , plant
    , description
    , total||plant
    , plant||description
    , po||'/'|| po_line
    
    
   FROM Tracking


 
 ;