/*=======================================
    < CHWM := CHAVIERWEBMÍDIA >
    < JS := CONTATOS DO SITE >
======================================= */


setTimeout(function () {

    const alerta = document.querySelector('.alert-success');

    if (alerta) {

        const alertaBootstrap = bootstrap.Alert.getOrCreateInstance(alerta);

        alertaBootstrap.close();
    }

}, 3000);