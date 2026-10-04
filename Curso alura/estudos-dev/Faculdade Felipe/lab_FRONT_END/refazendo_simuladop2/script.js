
const livros = [
  { titulo: "Dom Casmurro", autor: "Machado de Assis" },
  { titulo: "O Pequeno Príncipe", autor: "Antoine de Saint-Exupéry" },
  { titulo: "1984", autor: "George Orwell" }
];



const container = document.getElementById('container-livros');
const form = document.getElementById('form-livro')
function exibirLivros(){
    container.innerHTML='';
    livros.forEach(livro =>{
        const card = document.createElement('div');
        card.className = 'livro-card';
        card.innerHTML = `
        <h3>${livro.titulo}</h3>
        <p>${livro.autor}</p>
        `
        container.appendChild(card);
    });

}

form.addEventListener('submit', (e)=>{
    e.preventDefault()
    const titulo = document.getElementById('titulo').value.trim();
    const autor = document.getElementById('autor').value.trim()
    if (autor && titulo){
        livros.push({titulo,autor});
        exibirLivros();
        form.reset()
    }
})
exibirLivros()