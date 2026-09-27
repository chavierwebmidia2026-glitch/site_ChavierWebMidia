/*=======================================
    < CHWM := CHAVIERWEBMÍDIA >
    < JS := SCRIPTS QUALIFICAÇÕES SITE >
    =======================================*/




/*Modal imagem ampliar pagina quanlificações*/

function ampliarImagem(imagem) {
    document.getElementById("imagemAmpliada").src = imagem;

    const modal = new bootstrap.Modal(
        document.getElementById("modalImagem")
    );

    modal.show();
}