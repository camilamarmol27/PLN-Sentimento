import streamlit as st
from deep_translator import GoogleTranslator
from textblob import TextBlob

# Configuração da página do Streamlit
st.set_page_config(
    page_title="Analisador de Sentimentos Offline",
    page_icon="📊",
    layout="centered",
)

# Título e descrição explicando a versão offline
st.title("📊 Analisador de Sentimentos Offline")
st.markdown(
    """
    Este aplicativo realiza análise de sentimentos **totalmente offline** utilizando bibliotecas tradicionais de Processamento de Linguagem Natural (PLN):
    - **deep-translator**: Traduz automaticamente textos em português para o inglês de forma invisível.
    - **TextBlob**: Processa o texto em inglês e calcula a polaridade do sentimento.
    """
)

st.divider()

# Área de entrada de texto para o usuário
texto_usuario = st.text_area(
    "Digite ou cole o texto que deseja analisar (suporta português e inglês):",
    placeholder="Ex: Eu adorei este aplicativo, ele é simplesmente fantástico!",
    height=150,
)

# Botão de análise
if st.button("Analisar", type="primary"):
    if not texto_usuario.strip():
        st.warning("Por favor, insira algum texto antes de clicar em analisar.")
    else:
        with st.spinner("Analisando sentimento..."):
            try:
                # Tradução invisível para o inglês (o TextBlob funciona melhor em inglês)
                # O GoogleTranslator detecta automaticamente o idioma de origem
                texto_traduzido = GoogleTranslator(
                    source="auto", target="en"
                ).translate(texto_usuario)

                # Análise de polaridade com TextBlob
                blob = TextBlob(texto_traduzido)
                polaridade = blob.sentiment.polarity

                # Classificação baseada na polaridade (-1 a 1)
                if polaridade > 0.05:
                    sentimento = "Positivo"
                    st.success(
                        f"**Sentimento Detectado:** {sentimento} (Polaridade: {polaridade:.2f})"
                    )
                elif polaridade < -0.05:
                    sentimento = "Negativo"
                    st.error(
                        f"**Sentimento Detectado:** {sentimento} (Polaridade: {polaridade:.2f})"
                    )
                else:
                    sentimento = "Neutro"
                    st.warning(
                        f"**Sentimento Detectado:** {sentimento} (Polaridade: {polaridade:.2f})"
                    )

                # Expansor opcional para fins de transparência técnica
                with st.expander("Detalhes técnicos da análise"):
                    st.write(f"**Texto Original:** {texto_usuario}")
                    st.write(f"**Texto Traduzido (para o TextBlob):** {texto_traduzido}")
                    st.write(f"**Pontuação de Polaridade:** {polaridade}")
                    st.caption(
                        "A polaridade varia de -1.0 (muito negativo) a 1.0 (muito positivo)."
                    )

            except Exception as e:
                st.error(
                    f"Ocorreu um erro durante o processamento da análise: {e}"
                )

# Rodapé simples
st.markdown("---")
st.caption(
    "Desenvolvido com Python, Streamlit, TextBlob e Deep Translator — Licença MIT."
)
