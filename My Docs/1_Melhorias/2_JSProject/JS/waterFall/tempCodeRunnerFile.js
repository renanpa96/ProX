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

const newData = data.map(function (e) {
  return e.Qty;
});

// const newData = data.map(function (e) {
//   return e.Qty;
// });

console.log(data);
console.log(newData);