let nome = "Luiz"; // criando
var nome2 = "Luiz"; // crian
if (verdadeira) {
  let nome = "Otávio"; // criando
  var nome2 = "Rogério"; // redeclaran
  if (verdadeira) {
    var nome2 = "Ronaldo"; // redeclarando
    let nome = "Outra coisa";
  }
}
console.log(nome, nome2); 