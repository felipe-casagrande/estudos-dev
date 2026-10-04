
function checarNumero(numero){
    return new Promise((resolve, reject)=>{
        setTimeout(()=>{
            if (numero >=0){
                resolve(numero);
            }else{
                reject("Numero invalido");
            }
        },1000);
    });
}
checarNumero(10)
.then(valor=> console.log('Numero Valido: ',valor))
.catch(erro => console.log(erro))
