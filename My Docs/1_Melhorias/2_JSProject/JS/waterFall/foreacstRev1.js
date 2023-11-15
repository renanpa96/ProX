// it is a form to Import the library
var xlsx = require("xlsx");
var fs = require("fs");
var path = require("path");

// var w = xlsx.readFile("\\Copy.xlsx");
// console.log(w.SheetNames);

var dir = __dirname + "\\FRCST\\";
var dir = path.join(__dirname, "FRCST");
var dirfile = __filename;
// var dirf =;
console.log(dir);

function readFileToJson(filename) {
  var wb = xlsx.readFile(filename, { cellDates: true });
  var wb = wb.SheetNames[0];
  var wb = xlsx.utils.sheet_to_json(wb);
  return data;
}

file = fs.readFileSync(dir);
console.log(dir);
