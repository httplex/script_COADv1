from bs4 import BeautifulSoup

from.extractors.activity import extrai_atividade
from.extractors.conditions import extrai_condicoes_especificas
from.extractors.coordinates import extrai_coordenadas
from.extractors.metadata import (
    estrai_data_assinatura,
    extrai_data_documento,
    extrai_numero_autorizacao,
    extrai_numero_processo,
    extrai_numero_sei,
)
from.extractors.parties import extrai_cpf_cnpj, extrai_interessado
from.extractors.uc import extrai_uc
from.shemas.document_data import DocumentData
from.utils.path_utils import extrai_sei_do_caminho

def parse_document(file_path: str) -> DocumentData:
    soup = BeautifulSoup(html, "lxml")

    numero_sei = extrai_numero_sei(soup)
    if not numero_sei:
        numero_sei = None

    return DocumentData(
        numero_autorizacao=extrai_numero_autorizacao(soup),
        numero_processo=extrai_numero_processo(soup),
        numero_sei=numero_sei,
        ucs_envolvidas=extrai_uc(soup),
        atividade=extrai_atividade(soup),
        interessado=extrai_interessado(soup),
        cpf_cnpj=extrai_cpf_cnpj(soup),
        condicoes_especificas=extrai_condicoes_especificas(soup),
        data_assinatura=extrai_data_assinatura(soup),
        data_documento=extrai_data_documento(soup),
        coordenadas_brutas=extrai_coordenadas(soup),
    )

def parse_html_document(caminho_html: str) -> DocumentData:
    with open(caminho_html, "r", encoding="utf-8", errors="ignore") as file:
        html = file.read()

    doc = parse_document(html)

    if not doc.numero_sei:
        doc.numero_sei = extrai_sei_do_caminho(caminho_html)
    
    return doc

def parse_html_document_as_dict(caminho_html: str) -> dict:
    return parse_html_document(caminho_html).dict()