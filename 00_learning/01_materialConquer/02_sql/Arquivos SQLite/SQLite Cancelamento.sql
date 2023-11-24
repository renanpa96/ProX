SELECT  
   mrp.qty_to_cancel qtdcancelada
   , mrp.moq 
   , mrp.__material material
   , mrp.material_description nomedomaterial
   , mrp.mrp_element_data poellinha
   , track.unit_price
   , track.status
   , track.total

   

  
FROM MRPData17 mrp 
LEFT JOIN TrackingOpenordersManausrev02 track
	ON track.poelinha=mrp.MRP_element_data
    
WHERE qtdcancelada != 0 and LOWER (track.status) = "waiting for invoice"
;
