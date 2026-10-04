const botao = document.querySelector('#botao')
const titulo = document.querySelector('#titulo')
botao.addEventListener('click',clicou)
function clicou(){
	alert('clicou')
	titulo.innerText = 'novo titulo porraaaaaaaaa'
}
