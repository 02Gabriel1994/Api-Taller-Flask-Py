 // Espera 5 segundos y luego oculta la alerta
 setTimeout(function() {
    var flashMessage = document.getElementById('flashMessage');
    if (flashMessage) {
        flashMessage.style.display = 'none';
    }
}, 5000); // 5000 milisegundos = 5 segundos