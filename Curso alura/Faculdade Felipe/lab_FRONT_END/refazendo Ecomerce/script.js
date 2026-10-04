let produtos = [];
async function carregarProdutos(){
    try{
    const resposta = await fetch('https://fakestoreapi.com/products');
    produtos = await resposta.json();
    exibirProdutos(produtos);
    }catch(erro){
        alert('Erro ao carregar produtos')
    }
}
function exibirProdutos(lista){
    const container = document.getElementById('container-produtos')
    container.innerHTML = '';

    lista.forEach(produto=>{
        
        const card = document.createElement('div');
        card.className = 'product-card';
        card.innerHTML = `
        <img src = "${produto.image}" alt = '${produto.title}'</h3>
        <h3>${produto.title}</h3>
        `;
        container.appendChild(card);

    })
    
}
 
carregarProdutos()