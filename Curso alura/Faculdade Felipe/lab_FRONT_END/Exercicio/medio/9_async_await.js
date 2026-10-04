function buscar_usuario(id){
    return new Promise((resolve,reject)=>{
        if (id>0){
            resolve({id:id,nome: "Usuario" + id});
        }else{
            reject("Id invalido");
        }
    })
}




async function buscarEimprimir(id){
    console.log('Buscando id...');
    try{

        // Se a Promise chamar resolve(), o valor vai para usuario, e o código continua normalmente dentro do try.
        const usuario = await buscar_usuario(id);
        console.log("Sucesso!, usuario encontrado")
        console.log(usuario);
        
        // no try e catch a mensagem do reject é capturada quando da erro, bloco catch

    }catch(erro){
        console.error(`Erro na busca: ${erro}`)
    }
}
buscarEimprimir(-10)