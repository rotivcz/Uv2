
import streamlit as st
from fpdf import FPDF
import os

def gerar_laudo_uveite(dados):
    nome = dados.get("nome", "Paciente")
    idade = dados.get("idade", "")
    sexo = dados.get("sexo", "")
    sintomas = ", ".join(dados.get("sintomas", []))
    tipo_uveite = dados.get("tipo_uveite", "Não especificado")
    exames = ", ".join(dados.get("exames_solicitados", []))
    tratamento = ", ".join(dados.get("tratamento", []))
    encaminhamentos = ", ".join(dados.get("encaminhamentos", []))
    hipoteses = ", ".join(dados.get("hipoteses", []))

    laudo = f"""Laudo Oftalmológico - Uveíte
----------------------------------
Paciente: {nome}
Idade: {idade} anos
Sexo: {sexo}

Queixa principal: sintomas de uveíte incluindo {sintomas}.
Classificação: Uveíte do tipo {tipo_uveite}.

Exames solicitados: {exames}.
Hipóteses diagnósticas: {hipoteses}.

Conduta inicial: {tratamento}.
Encaminhamentos: {encaminhamentos}.
"""
    return laudo.strip()

def exportar_pdf(nome_arquivo, texto):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)
    for linha in texto.split('\n'):
        pdf.multi_cell(0, 10, linha)
    caminho = f"{nome_arquivo}.pdf"
    pdf.output(caminho)
    return caminho

st.set_page_config(page_title="Laudo de Uveíte", layout="centered")
st.title("Gerador de Laudo para Uveíte")

nome = st.text_input("Nome do Paciente")
idade = st.number_input("Idade", min_value=0, max_value=120, step=1)
sexo = st.selectbox("Sexo", ["", "Feminino", "Masculino"])
sintomas = st.multiselect("Sintomas", ["visão borrada", "dor ocular", "fotofobia", "moscas volantes", "hiperemia"])
tipo_uveite = st.selectbox("Tipo de Uveíte", ["", "anterior", "intermediária", "posterior", "panuveíte"])
exames = st.multiselect("Exames Solicitados", ["Lâmpada de fenda", "Tonometria", "OCT", "Angiografia", "FAN", "HLA-B27", "PPD", "VDRL", "USG modo B"])
hipoteses = st.multiselect("Hipóteses Diagnósticas", ["Toxoplasmose", "Herpesvírus", "Tuberculose", "HLA-B27", "Sarcoidose", "Idiopática"])
tratamento = st.multiselect("Conduta Inicial", ["colírio de corticoide", "midriático", "prednisona 40mg/dia", "antibiótico", "antiviral"])
encaminhamentos = st.multiselect("Encaminhamentos", ["Reumatologista", "Infectologista", "Neurologista"])

if st.button("Gerar Laudo"):
    dados = {
        "nome": nome,
        "idade": idade,
        "sexo": sexo,
        "sintomas": sintomas,
        "tipo_uveite": tipo_uveite,
        "exames_solicitados": exames,
        "hipoteses": hypotheses,
        "tratamento": tratamento,
        "encaminhamentos": encaminhamentos
    }
    laudo = gerar_laudo_uveite(dados)
    st.text_area("Laudo Gerado", laudo, height=350)

    nome_arquivo = f"laudo_uveite_{nome.replace(' ', '_')}"
    caminho_pdf = exportar_pdf(nome_arquivo, laudo)
    with open(caminho_pdf, "rb") as f:
        st.download_button("📄 Baixar Laudo em PDF", data=f, file_name=f"{nome_arquivo}.pdf")
