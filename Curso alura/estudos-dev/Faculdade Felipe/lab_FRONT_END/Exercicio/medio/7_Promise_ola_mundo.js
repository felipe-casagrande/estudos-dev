// 7 - Criar uma Promise que resolve com "Olá Mundo".
function verificar(mensagem){
    return new Promise((resolve, reject) =>{
        setTimeout(() => {
            if (mensagem === "ola mundo"){
                resolve(mensagem);
        }else{
            reject("Mensagem Invalida");
        }
        },1000);
    });
}

verificar("ola mundo")
    //.then é pra que a gente pega o resultado da promise quando foi resolvida com sucesso
 .then(dados => console.log("Sucesso: ", dados))


 //catch é pra pegar o erro quando a promise foi rejeitada, recebe o else

 .catch(erro => console.log("Nao é ola mundo", erro)); 

// 8 -Criar Promise que rejeita se número for negativo.



