function numeroAleatorio(){
	return Math.round(100000 + Math.random()*899999);
}

function getHora(){
	var data = new Date();
	var hora = data.getHours();
	return hora;
};

function saudacao(){

	var hora = getHora();
	var mensagem = '';

	if ( hora >= 0 & hora < 6){
		mensagem = "Ótima madrugada";
	} else {
		if ( hora >= 6 & hora <12 ){
			mensagem = "Bom dia";	
		} else {
			if(hora >= 12 & hora < 18){
				mensagem = "Boa tarde";
			}else{
				mensagem = "Boa noite";
			}
		}
	}

	var saudacao = document.getElementById('saudacao');
	saudacao.textContent = mensagem;
}

function geraSenhaAleatoria(){
	var senha = numeroAleatorio();
	var senhaUsuario = document.getElementById("senhaUsuario");
	senhaUsuario.value = senha;
}

function checkPassword(){
	var senha = password.value;
	if (senha.length < 4){
		mensagemPassword.textContent = 'Senha curta!';
		event.preventDefault();
	}else{
		mensagemPassword.textContent ='';
	}
}

var password = document.getElementById('inputPassword');

var mensagemPassword = document.getElementById('feedbackPassword');

var formLogin = document.getElementById('form-login');

window.addEventListener('load', geraSenhaAleatoria, false);

window.addEventListener('DOMContentLoaded', saudacao, false);

password.addEventListener('blur',checkPassword,false);

formLogin.addEventListener('submit',checkPassword,false);