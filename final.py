import streamlit as st

import streamlit as st

st.image("viva_melhor_logo.png", width=150)
st.title("Viva Melhor")

st.set_page_config(page_title="Intervenções Não-Farmacológicas Personalizada", layout="centered")

import streamlit as st
st.title("VIVA MELHOR")
import streamlit as st
from PIL import Image
from streamlit.columns import columns
col1, col2 = st.columns([1, 4])
with col1:  
  st.image("viva_melhor_logo.png", width=80)
with col2: 
  st.title("Viva Melhor")

st.markdown("Preencha abaixo com o **perfil de vida do paciente** (idade, doenças, contexto social, hábitos, etc):")

perfil = st.text_area("📝 Perfil do Paciente", height=300, placeholder="Ex: Mulher, 67 anos, hipertensa, mora sozinha, aposentada...")

def gerar_resposta(perfil):
    perfil = perfil.lower()

    if any(p in perfil for p in ["67 anos", "idosa", "idoso", "osteoporose", "dor", "sozinha"]):
        return """
### 🔍 Recomendações Personalizadas:
1. **Grupo de convivência na USF Ur 03 ou CRAS Ibura** – combate solidão e estimula interação social.
2. **Atividades como jardinagem e leitura** – exigem pouco esforço físico e melhoram o humor.
3. **Alongamento e fisioterapia leve em casa** – ajudam com dor articular e funcionalidade.  

*→ Protótipo: simulação baseada em palavras-chave. No futuro, será IA real com linguagem natural.*
"""

    elif any(p in perfil for p in ["depressão", "ansioso", "triste", "isolado", "psiquiátrico" ]):
        return """
### 🔍 Recomendações Personalizadas:
1. **Mindfulness guiado com app gratuito (ex: Lojong)** – melhora ansiedade e foco.
2. **Grupos comunitários presenciais (ex: rodas de conversa na UBS)** – reforça vínculo e acolhimento.
3. **Escrita terapêutica ou diário emocional** – técnica simples com bom impacto em saúde mental.

*→ Protótipo: simulação baseada em palavras-chave. No futuro, será IA real com linguagem natural.*
"""

    elif any(p in perfil for p in ["jovem", "20 anos", "universitário", "estudante", "moradora da ur 03"]):
        return """
### 🔍 Recomendações Personalizadas:
1. **Atividade física regular (musculação ou esportes coletivos)** – aumenta energia e autoestima. Há também atividades físicas possíveis de serem realizadas no COMPAZ Paulo Freire, localizado no bairro do ibura, bem como Academia da cidade na redondeza.
2. **Aplicativos de rotina e foco (ex: Forest, Notion)** – para organização e disciplina.
3. **Voluntariado em ONG local** – fortalece propósito e integração social.

*→ Protótipo: simulação baseada em palavras-chave. No futuro, será IA real com linguagem natural.*
"""

    else:
        return """
### 🔍 Recomendações Gerais:
1. **Exercício leve adaptado à realidade do paciente** – caminhada, dança, ou alongamento funcional.
2. **Grupos comunitários locais ou atividades manuais** – reforçam autonomia e bem-estar.
3. **Apps de acompanhamento de humor, rotina ou sono** – podem ajudar a construir hábitos saudáveis.

*Viva Melhor: sua rotina inspira nossa solução*

*→ Protótipo: simulação baseada em palavras-chave. No futuro, será IA real com linguagem natural.*
"""

if st.button("💡 Gerar Recomendações"):
    if perfil.strip() == "":
        st.warning("Por favor, insira um perfil do paciente.")
    else:
        st.markdown(gerar_resposta(perfil))

