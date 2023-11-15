// 1 - Importing the Lib > it is a form to Import the library
let xlsx = require("xlsx");
let fs = require("fs");
let path = require("path");
// const { timeStamp } = require("console");

// 2 - Paths
// To read every file name. Using Path we can read files path in any OS (windows, IOS etc)
// For this that would be like var targetDir = path.join(__dirname + "FRCST");
// fs.readdirSync > list all the name of the files in a folder
let nome_pasta = "FRCST";
let targetDir = path.join(__dirname, nome_pasta);
let files = fs.readdirSync(targetDir);
console.log(targetDir);
console.log(files);

// 3 - Declaracao de variaveis para armazenamento
let combineData = [];
let newCombineData = [];
let jsonData = [];

// 4 - Code:
//  Aq ele funciona como o for do PY, pra cada file dentro da lista de files, faca....
files.forEach(function (file) {
  consolidatePath = path.join(targetDir, file);
  let workBase = xlsx.readFile(consolidatePath, {
    type: "binary",
    cellText: false,
    cellDates: true,
  });

  let workSheet = workBase.Sheets["Sheet1"];
  // console.log(workSheet);
  let data = xlsx.utils.sheet_to_json(workSheet, {
    raw: false,
    // dateNF: "mm-dd-yyyy",
    dateNF: "mm/dd/yyyy",
  });
  // function criarIndex ()
  console.log(data);
  combineData = combineData.concat(data);

  // data = JSON.parse(data);
  // console.log(data.PLant);

  // const teste = combineData.map(e){
  //   teste
  // }

  let newCombineData = combineData.map(function (record) {
    record.Id_Stamp = Math.round(Date.now() / 1000);
    // record.Search_Month = record.Receipt_Date.Search_Month;
    return record;
  });
  // console.log(newCombineData);
  // var
  // var newCombineData = combineData.map(function (record) {
  //   record.ID = Math.round(Date.now() / 1000);
  // });
  // console.log(combineData);
  // console.log(combineData);
  return newCombineData;
});

newCombineData.Id_Stamp = parseFloat(newCombineData.Id_Stamp);

// console.log(typeof newCombineData.Qty);

// transforma de JSON para string, nao e mais objeto
jsonData = JSON.stringify(combineData);
let obj = JSON.parse(jsonData);
// console.log(jsonData.Plant); //Undef
// console.log(jsonData);
// console.log(typeof jsonData)

// entender como procesos de salvar funciona
fs.writeFile("test.txt", jsonData, function (err) {
  if (err) {
    console.log(err);
  }
});

// Esse aq de Baixo da erro
// fs.writeFile("test.xlsx", combineData, function (err) {
//   if (err) {
//     console.log(err);
//   }
// });

// https://www.youtube.com/watch?v=Uv_yDqfxS2s
//timestamp > https://www.epochconverter.com/ > Para checagem
// function idTimeStamp() {
//   TimeStamp = Math.round(Date.now() / 1000);
//   return TimeStamp;
// }

// console.log(TimeStamp);
// console.log(Math.round(Date.now() / 1000));
