const livros = [
  { titulo: "Dom Casmurro", autor: "Machado de Assis" },
  { titulo: "O Pequeno Príncipe", autor: "Antoine de Saint-Exupéry" },
  { titulo: "1984", autor: "George Orwell" }
];




function exibirLivros(lista){
    const container = document.getElementById("container-livros");
    container.innerHTML = ''
   
    lista.forEach(livro =>{
        const card = document.createElement('div')
        card.className = 'livro-card'


        card.innerHTML = `
        <h3>${livro.titulo}</h3>
        <p>Autor: ${livro.autor}</p>
        
        `;
    container.appendChild(card);
    });

}
const form = document.getElementById('form-livros')
form.addEventListener('submit', (e)=>{
    e.preventDefault();
    const titulo = document.querySelector('#titulo').value.trim()
    const autor = document.querySelector('#autor').value.trim()
    if (titulo && autor){
        livros.push({titulo,autor});
        exibirLivros(livros)
        form.reset();
    }

});


exibirLivros(livros);