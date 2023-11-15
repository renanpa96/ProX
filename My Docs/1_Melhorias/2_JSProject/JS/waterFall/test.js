// 1 - Importing the Lib > it is a form to Import the library
let xlsx = require("xlsx");
let fs = require("fs");
let path = require("path");
const { compileFunction } = require("vm");
const { log } = require("console");
// const { timeStamp } = require("console");

// 2 - Paths
// To read every file name. Using Path we can read files path in any OS (windows, IOS etc)
// For this that would be like var targetDir = path.join(__dirname + "FRCST");
// fs.readdirSync > list all the name of the files in a folder
let nome_pasta = "FRCST";
let targetDir = path.join(__dirname, nome_pasta);
// var files = fs.readdirSync(targetDir);
let file = "Forecast Foxconn_04.23.xlsx";
console.log(targetDir);
console.log(file);

// 3 - Declaracao de variaveis para armazenamento
let combineData = [];
let newCombineData = [];
let jsonData = [];

consolidatePath = path.join(targetDir, file);
let workBase = xlsx.readFile(consolidatePath, {
  type: "binary",
  cellText: false,
  cellDates: true,
});

let workSheet = workBase.Sheets["Sheet1"];

let data = xlsx.utils.sheet_to_json(workSheet, {
  raw: false,
  // dateNF: "mm-dd-yyyy",
  dateNF: "yyyy/dd/mm",
});
// var data1 = readFileToJason(consolidatePath);
// console.log(data);

// const newData = data.map(function pessoa(Plant) {
//   this.Plant = Plant;
// });

const newData = data.map(function (e) {
  return e.Qty;
});

console.log(data);
console.log(newData.Plant);
console.log(newData);

Math.random();
a = 4;
console.log(isNaN(a));
// var data = criarIndex();
// console.log(data.Group);

// console.log(data.length);
// console.log(data.values());
// console.log(data{Plant});

// function criarIndex(
//   Plant,
//   BOM,
//   Receipt_Date,
//   Part_Number,
//   Forecast_date,
//   Qty,
//   Family,
//   Group
// ) {
//   return { data };
//   return {
//     Plant: Plant,
//     Qty: Qty,
//     BOM: BOM,
//     Receipt_Date: Receipt_Date,
//     Part_Number: Part_Number,
//     Forecast_date: Forecast_date,
//     Family: Family,
//     Group: Group,
//   };
// }
