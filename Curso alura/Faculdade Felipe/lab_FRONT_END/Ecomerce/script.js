let produtos = []

async function carregarProdutos(){
    try{
        const resposta = await fetch("https://fakestoreapi.com/products");
        produtos = await resposta.json()
        console.log(produtos)
        exibirProdutos(produtos);
    }catch(erro){
        alert("Erro ao carregar produtos" +erro.message)
    }

}
function exibirProdutos(lista){
    const container = document.getElementById('produtos');
    container.innerHTML = ''
    if (lista.length === 0){
        container.innerHTML = '<p>Nenhum produto encontrado</p>';
        return
    }
    lista.forEach(produto =>{
        const card = document.createElement('div');
        card.className = 'product-card';
        card.innerHTML = `
        <img src = "${produto.image}" alt = "${produto.title}">
        <h3>${produto.title}</h3>
        <p>${produto.description.substring(0,60)}...</p>
        <strong>US$ ${produto.price}</strong>
         `;
         container.appendChild(card);


    });
}
document.getElementById('filtro').addEventListener('keyup',(event) =>{
    const termo = event.target.value.toLowerCase();
    const filtrados = produtos.filter(p => p.title.toLowerCase().includes(termo));
    exibirProdutos(filtrados);
});
carregarProdutos()
