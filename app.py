import streamlit as st

st.title("IA para Intervenções Não-Farmacológicas")

st.markdown("Preencha abaixo com o perfil do paciente:")

perfil = st.text_area("Perfil do Paciente", height=300, placeholder="Ex: Homem, 58 anos, hipertenso, aposentado...")

if st.button("Gerar Recomendações"):
    if perfil.strip() == "":
        st.warning("Por favor, insira um perfil.")
    else:
        resposta = f'''
Perfil recebido: {perfil}

### Recomendações Personalizadas:

1. **Caminhada diária em área segura** – para controle da pressão arterial, estímulo ao bem-estar e sociabilidade.

2. **Grupo de meditação ou espiritualidade em UBS ou igreja local** – acessível e de impacto positivo na saúde mental.

3. **Cuidar de plantas ou jardinagem em casa** – alternativa relaxante e prática para pessoas com mobilidade reduzida.

*Estas sugestões são simuladas. No protótipo final, seriam geradas automaticamente por uma IA real.*
'''
        st.markdown(resposta)
