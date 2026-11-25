document.addEventListener("DOMContentLoaded", () => {

    const modais = {
        senha: document.getElementById("modal-senha"),
        email: document.getElementById("modal-email"),
        excluir: document.getElementById("modal-excluir"),
    };

    const botoesAbrir = {
        senha: document.getElementById("btn-alterar-senha"),
        email: document.getElementById("btn-alterar-email"),
        excluir: document.getElementById("btn-excluir-conta"),
    };

    function abrirModal(modal) {
        if (modal) modal.hidden = false;
    }

    function fecharModal(modal) {
        if (!modal) return;

        modal.hidden = true;

        const form = modal.querySelector("form");
        if (form) form.reset();
    }

    Object.entries(botoesAbrir).forEach(([chave, botao]) => {
        botao?.addEventListener("click", () => {
            abrirModal(modais[chave]);
        });
    });

    document.querySelectorAll(".modal .cancelar").forEach((botao) => {
        botao.addEventListener("click", () => {
            fecharModal(botao.closest(".modal"));
        });
    });

    Object.values(modais).forEach((modal) => {
        modal?.addEventListener("click", (event) => {
            if (event.target === modal) {
                fecharModal(modal);
            }
        });
    });

    document.addEventListener("keydown", (event) => {
        if (event.key === "Escape") {
            Object.values(modais).forEach((modal) => {
                if (modal && !modal.hidden) {
                    fecharModal(modal);
                }
            });
        }
    });

});