pip install streamlit
pip install openai


import streamlit as st
import openai

# Initialisation de l'API de ChatGPT
openai.api_key = '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'

# Fonction pour traduire le texte avec ChatGPT
def translate_text(text, target_language='en'):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=f"Translate the following text from French to {target_language}: \"{text}\"",
        max_tokens=100,
        temperature=0.7,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=None,
        n=1,
        log_level="info"
    )
    translation = response.choices[0].text.strip()
    return translation

# Interface utilisateur Streamlit
def main():
    st.title("Traduction de texte")
    text_input = st.text_input("Entrez le texte à traduire en anglais", value='')

    if st.button("Traduire"):
        if text_input:
            translation = translate_text(text_input)
            st.success(f"Traduction : {translation}")

if __name__ == '__main__':
    main()

