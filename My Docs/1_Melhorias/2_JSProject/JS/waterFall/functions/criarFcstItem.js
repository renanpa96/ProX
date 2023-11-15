function criarForecastItem(
  id,
  Plant,
  BOM,
  Receipt_Date,
  Part_Number,
  Forecast_date,
  Qty,
  Family,
  Group
) {
  return {
    id,
    data: {
      Plant,
      BOM,
      Receipt_Date,
      PNumber: Part_Number,
      Forecast_date,
      Qty,
      Family,
      Group,
    },
  };
}

export default criarForecastItem();
