// import criarForecastItem from "./functions/criarFcstItem";
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
const item1 = criarForecastItem(
  "1",
  "272J",
  "TRUE",
  "2023/28/08",
  "02311VFF-1",
  "02/01/2023",
  "176",
  "VFF-1",
  "ABC"
);
console.log(item1);

console.log(item1.data.Plant);
// Tem que chamar a informação para ele ter a referencia do objeto
