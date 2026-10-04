/*=======================================
    < CHWM := CHAVIERWEBMÍDIA >
    < JS := CHATBOT DO SITE >
======================================= */


const chwmButton = document.getElementById(
    "chwmChatbotButton"
);

const chwmChatbot = document.getElementById(
    "chwmChatbot"
);

const chwmClose = document.getElementById(
    "chwmChatbotClose"
);

const chwmMessages = document.getElementById(
    "chwmChatbotMessages"
);

const chwmInput = document.getElementById(
    "chwmChatbotInput"
);

const chwmSend = document.getElementById(
    "chwmChatbotSend"
);

const chwmCsrfToken = document.getElementById(
    "chwmCsrfToken"
);


// ==========================================
// VARIÁVEIS DO ATENDIMENTO
// ==========================================

let chwmAtendimentoId = null;

let chwmEtapa = "nome";

let chwmAtendimentoFinalizado = false;


// ==========================================
// ABRIR CHATBOT
// ==========================================

chwmButton.addEventListener(
    "click",
    function () {

        chwmChatbot.classList.add(
            "ativo"
        );

        chwmInput.focus();
    }
);


// ==========================================
// FECHAR CHATBOT
// ==========================================

chwmClose.addEventListener(
    "click",
    function () {

        chwmChatbot.classList.remove(
            "ativo"
        );
    }
);


// ==========================================
// ADICIONAR MENSAGEM AO CHAT
// ==========================================

function chwmMensagem(
    texto,
    tipo
) {

    const mensagem =
        document.createElement("div");

    mensagem.classList.add(
        "chwm-message",
        tipo
    );

    const bolha =
        document.createElement("div");

    bolha.classList.add(
        "chwm-bubble"
    );

    bolha.innerHTML = texto;

    mensagem.appendChild(
        bolha
    );

    chwmMessages.appendChild(
        mensagem
    );

    chwmMessages.scrollTop =
        chwmMessages.scrollHeight;
}


// ==========================================
// MENU FINAL
// ==========================================

function chwmMostrarMenuFinal() {

    chwmMensagem(
        `
        <strong>O que você deseja fazer agora?</strong>
        <br><br>

        <strong>1</strong>️⃣ Voltar ao início
        <br>

        <strong>2</strong>️⃣ Nova mensagem
        <br>

        <strong>3</strong>️⃣ Encerrar atendimento
        `,
        "bot"
    );

    chwmEtapa =
        "menu_final";

    chwmInput.disabled =
        false;

    chwmSend.disabled =
        false;

    chwmInput.placeholder =
        "Digite 1, 2 ou 3...";
}


// ==========================================
// MENU PRINCIPAL
// ==========================================

function chwmMostrarMenuPrincipal() {

    chwmMensagem(
        `
        <strong>Como podemos ajudar?</strong>
        <br><br>

        <strong>1</strong>️⃣ Solicitar orçamento
        <br>

        <strong>2</strong>️⃣ Conhecer nossos serviços
        <br>

        <strong>3</strong>️⃣ Criar um site
        <br>

        <strong>4</strong>️⃣ Criar uma Landing Page
        <br>

        <strong>5</strong>️⃣ Criar um Sistema Web
        <br>

        <strong>6</strong>️⃣ Falar sobre outro projeto
        <br>

        <strong>7</strong>️⃣ Encerrar atendimento
        `,
        "bot"
    );

    chwmEtapa =
        "menu_principal";

    chwmInput.disabled =
        false;

    chwmSend.disabled =
        false;

    chwmInput.placeholder =
        "Digite uma opção...";
}


// ==========================================
// PROCESSAR MENU FINAL
// ==========================================

function chwmProcessarMenuFinal(
    opcao
) {

    if (opcao === "1") {

        chwmMensagem(
            "1️⃣ Voltar ao início",
            "user"
        );

        chwmMensagem(
            `
            Claro! 😊
            <br><br>
            Vamos continuar seu atendimento.
            `,
            "bot"
        );

        chwmMostrarMenuPrincipal();

        return;
    }


    if (opcao === "2") {

        chwmMensagem(
            "2️⃣ Nova mensagem",
            "user"
        );

        chwmMensagem(
            `
            Perfeito! 😊
            <br><br>
            Digite sua nova mensagem:
            `,
            "bot"
        );

        chwmEtapa =
            "nova_mensagem";

        chwmInput.placeholder =
            "Digite sua mensagem...";

        return;
    }


    if (opcao === "3") {

        chwmMensagem(
            "3️⃣ Encerrar atendimento",
            "user"
        );

        chwmMensagem(
            `
            Obrigado pelo contato! 😊
            <br><br>
            A <strong>CHAVIERWEBMÍDIA</strong>
            agradece sua mensagem.
            <br><br>
            Quando precisar, estaremos à disposição.
            `,
            "bot"
        );

        chwmEtapa =
            "finalizado";

        chwmAtendimentoFinalizado =
            true;

        chwmInput.disabled =
            true;

        chwmSend.disabled =
            true;

        chwmInput.placeholder =
            "Atendimento encerrado.";

        return;
    }


    chwmMensagem(
        `
        ⚠️ Opção inválida.
        <br><br>
        Digite <strong>1</strong>, <strong>2</strong>
        ou <strong>3</strong>.
        `,
        "bot"
    );
}


// ==========================================
// PROCESSAR MENU PRINCIPAL
// ==========================================

function chwmProcessarMenuPrincipal(
    opcao
) {

    const servicos = {

        "1":
            "💰 Solicitar orçamento",

        "2":
            "📋 Conhecer nossos serviços",

        "3":
            "🌐 Criar um site",

        "4":
            "📄 Criar uma Landing Page",

        "5":
            "💻 Criar um Sistema Web",

        "6":
            "🚀 Falar sobre outro projeto"
    };


    if (opcao === "7") {

        chwmMensagem(
            "7️⃣ Encerrar atendimento",
            "user"
        );

        chwmMensagem(
            `
            Obrigado pelo contato! 😊
            <br><br>
            A <strong>CHAVIERWEBMÍDIA</strong>
            está à disposição quando precisar.
            `,
            "bot"
        );

        chwmEtapa =
            "finalizado";

        chwmAtendimentoFinalizado =
            true;

        chwmInput.disabled =
            true;

        chwmSend.disabled =
            true;

        chwmInput.placeholder =
            "Atendimento encerrado.";

        return;
    }


    if (!servicos[opcao]) {

        chwmMensagem(
            `
            ⚠️ Opção inválida.
            <br><br>
            Escolha uma opção de
            <strong>1 a 7</strong>.
            `,
            "bot"
        );

        return;
    }


    chwmMensagem(
        servicos[opcao],
        "user"
    );


    chwmMensagem(
        `
        Excelente escolha! 🚀
        <br><br>
        Agora conte um pouco mais sobre
        o que você precisa.
        <br><br>
        Nossa equipe poderá analisar
        sua necessidade.
        `,
        "bot"
    );


    chwmEtapa =
        "nova_mensagem";

    chwmInput.placeholder =
        "Conte sobre seu projeto...";
}


// ==========================================
// ENVIAR PARA DJANGO
// ==========================================

async function chwmEnviarParaDjango(
    texto,
    etapa
) {

    try {

        const resposta =
            await fetch(
                "/chatbot/mensagem/",
                {
                    method: "POST",

                    headers: {
                        "Content-Type":
                            "application/json",

                        "X-CSRFToken":
                            chwmCsrfToken.value
                    },

                    body: JSON.stringify(
                        {
                            mensagem:
                                texto,

                            atendimento_id:
                                chwmAtendimentoId,

                            etapa:
                                etapa
                        }
                    )
                }
            );


        const dados =
            await resposta.json();


        // ==================================
        // ERRO DE VALIDAÇÃO
        // ==================================

        if (!resposta.ok) {

            chwmMensagem(
                dados.erro ||
                `
                ⚠️ Não foi possível processar
                sua mensagem.
                `,
                "bot"
            );

            chwmInput.focus();

            return;
        }


        // ==================================
        // ATUALIZA ID
        // ==================================

        chwmAtendimentoId =
            dados.atendimento_id;


        // ==================================
        // MOSTRA RESPOSTA DO BOT
        // ==================================

        chwmMensagem(
            dados.resposta,
            "bot"
        );


        // ==================================
        // AVANÇA ETAPA
        // ==================================

        if (etapa === "nome") {

            chwmEtapa =
                "whatsapp";
        }

        else if (
            etapa === "whatsapp"
        ) {

            chwmEtapa =
                "email";
        }

        else if (
            etapa === "email"
        ) {

            chwmEtapa =
                "servico";
        }

        else if (
            etapa === "servico"
        ) {

            chwmEtapa =
                "mensagem";
        }

        else if (
            etapa === "mensagem"
        ) {

            chwmMostrarMenuFinal();
        }

    }

    catch (erro) {

        console.error(
            "Erro no chatbot:",
            erro
        );

        chwmMensagem(
            `
            ❌ Não foi possível conectar
            ao atendimento.
            <br><br>
            Tente novamente.
            `,
            "bot"
        );

        chwmInput.focus();
    }
}


// ==========================================
// ENVIAR MENSAGEM
// ==========================================

function chwmEnviarMensagem() {

    const texto =
        chwmInput.value.trim();


    // ======================================
    // NÃO ENVIA VAZIO
    // ======================================

    if (texto === "") {

        return;
    }


    // ======================================
    // ATENDIMENTO ENCERRADO
    // ======================================

    if (
        chwmAtendimentoFinalizado
    ) {

        return;
    }


    // ======================================
    // MENU FINAL
    // ======================================

    if (
        chwmEtapa === "menu_final"
    ) {

        chwmMensagem(
            texto,
            "user"
        );

        chwmInput.value = "";

        chwmProcessarMenuFinal(
            texto
        );

        return;
    }


    // ======================================
    // MENU PRINCIPAL
    // ======================================

    if (
        chwmEtapa === "menu_principal"
    ) {

        chwmMensagem(
            texto,
            "user"
        );

        chwmInput.value = "";

        chwmProcessarMenuPrincipal(
            texto
        );

        return;
    }


    // ======================================
    // NOVA MENSAGEM
    // ======================================

    if (
        chwmEtapa === "nova_mensagem"
    ) {

        chwmMensagem(
            texto,
            "user"
        );

        chwmInput.value = "";

        chwmEnviarParaDjango(
            texto,
            "mensagem"
        );

        return;
    }


    // ======================================
    // FLUXO NORMAL
    // ======================================

    chwmMensagem(
        texto,
        "user"
    );

    chwmInput.value = "";


    chwmEnviarParaDjango(
        texto,
        chwmEtapa
    );
}


// ==========================================
// BOTÃO ENVIAR
// ==========================================

chwmSend.addEventListener(
    "click",
    chwmEnviarMensagem
);


// ==========================================
// ENTER
// ==========================================

chwmInput.addEventListener(
    "keydown",
    function (evento) {

        if (
            evento.key === "Enter"
        ) {

            evento.preventDefault();

            chwmEnviarMensagem();
        }
    }
);


// ==========================================
// FECHAR CLICANDO FORA
// ==========================================

document.addEventListener(
    "click",
    function (evento) {

        if (

            chwmChatbot.classList.contains(
                "ativo"
            )

            &&

            !chwmChatbot.contains(
                evento.target
            )

            &&

            !chwmButton.contains(
                evento.target
            )

        ) {

            chwmChatbot.classList.remove(
                "ativo"
            );
        }
    }
);