// 1) Declarar variáveis com let e const

let numero = 5;
console.log(numero);
const idade = 20;
console.log(idade);
// 2)Declarar um array de números e imprimir no console.
let lista = [1,2,3,4,5];
console.log(lista);

// 3)Criar função que soma dois números.
function soma(a,b){
    return a + b
}
console.log(soma(2,3));

// 4) Alterar texto de um <h1>.
const titulo = document.querySelector('h1');
titulo.innerHTML = 'novo titulo';

// 5) Adicionar evento de click a um botão.
const botao = document.querySelector('button');
botao.addEventListener('click',()=> {
   alert('clicou no botao porraaaaa ajahahhahaaa');
})

// 6)Criar função que recebe um callback e chama-o.

setTimeout(function(){
    const resultado = soma(1,2)
    console.log(`O resultado da soma é ${resultado}`);
},3000)
console.log("AGUARANDO 3 SEGUNDO PARA VIR O RESULTADO")
