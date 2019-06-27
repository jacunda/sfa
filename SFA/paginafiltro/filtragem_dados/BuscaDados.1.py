from .models import Empresa
import urllib
from bs4 import BeautifulSoup

lista_empresas = [{"url": 'http://www.fundamentus.com.br/detalhes.php?papel=vale3'},
                  {"url": 'http://www.fundamentus.com.br/detalhes.php?papel=bbdc4'},
                  {"url": 'http://www.fundamentus.com.br/detalhes.php?papel=petr3'},
                  {"url": 'http://www.fundamentus.com.br/detalhes.php?papel=abev3'}
                  ]

'''
LPA
Crescimento Rec. 5 anos
EBIT (12 meses)
P/L
Patrimônio Líquido
Lucro Líquido (12 Meses)
P/VP
Dívida Bruta
Receita Líquida (3 meses)
Dividend Yeld
Dívida Líquida
EBIT (3 Meses)
VPA
Receita Líquida (12 meses)
Lucro Líquido (3 Meses)
Volume médio
Setor
 +++

LPA
crescimento_receita5
EBIT12
patrim_liq
PL
patrim_liq
Lucro_liq12
PVP
div_bruta
receita_liq3
dividend_yield
div_liquida
EBIT3
VPA
receita_liq12
lucro_liq3
volume
'''

#lista_resultados = []
def inserir_Dados_no_Banco():

    for emp in lista_empresas:

        url = emp['url']

        html = urllib.request.urlopen(url)
        bsObj = BeautifulSoup(html.read(), 'html.parser')
        bsObj = bsObj.find_all(class_='txt')

        varl = [
            (bsObj[1].get_text(strip=True).replace('.', '').replace('-', '0')),
            float(bsObj[3].get_text(strip=True).replace(
                '.', '').replace(',', '.').replace('-', '0')),
            (bsObj[5].get_text(strip=True).replace('.', '').replace('-', '0')),
            (bsObj[7].get_text(strip=True).replace('.', '').replace('-', '0')),
            (bsObj[9].get_text(strip=True).replace('.', '').replace('-', '0')),
            float(bsObj[11].get_text(strip=True).replace(
                ',', '.').replace(',', '.').replace('-', '0')),
            (bsObj[13].get_text(strip=True).replace(
                ',', '.').replace('-', '0')),
            float(bsObj[15].get_text(strip=True).replace(
                '.', '').replace(',', '.').replace('-', '0')),
            (bsObj[17].get_text(strip=True).replace(
                '.', '').replace('-', '0')),
            float(bsObj[19].get_text(strip=True).replace(
                '.', '').replace('-', '0')),

            float(bsObj[21].get_text(strip=True).replace(
                '.', '').replace('-', '0')),
            (bsObj[23].get_text(strip=True).replace(
                '.', '').replace('-', '0')),
            float(bsObj[25].get_text(strip=True).replace(
                '.', '').replace('-', '0')),
            float(bsObj[27].get_text(strip=True).replace(
                '.', '').replace('-', '0')),

            float(bsObj[32].get_text(strip=True).replace(
                '%', '').replace(',', '.').replace('-', '0')),
            float(bsObj[37].get_text(strip=True).replace(
                '%', '').replace(',', '.').replace('-', '0')),
            float(bsObj[42].get_text(strip=True).replace(
                '%', '').replace(',', '.').replace('-', '0')),
            float(bsObj[47].get_text(strip=True).replace(
                '%', '').replace(',', '.').replace('-', '0')),
            float(bsObj[52].get_text(strip=True).replace(
                '%', '').replace(',', '.').replace('-', '0')),
            float(bsObj[57].get_text(strip=True).replace(
                '%', '').replace(',', '.').replace('-', '0')),
            float(bsObj[62].get_text(strip=True).replace(
                '%', '').replace(',', '.').replace('-', '0')),
            float(bsObj[67].get_text(strip=True).replace(
                '%', '').replace(',', '.').replace('-', '0')),
            float(bsObj[72].get_text(strip=True).replace(
                '%', '').replace(',', '.').replace('-', '0')),
            float(bsObj[77].get_text(strip=True).replace(
                '%', '').replace(',', '.').replace('-', '0')),
            float(bsObj[82].get_text(strip=True).replace(
                '%', '').replace(',', '.').replace('-', '0')),
            float(bsObj[34].get_text(strip=True).replace(
                '%', '').replace(',', '.').replace('-', '0')),
            float(bsObj[39].get_text(strip=True).replace(
                '%', '').replace(',', '.').replace('-', '0')),
            float(bsObj[44].get_text(strip=True).replace(
                '%', '').replace(',', '.').replace('-', '0')),
            float(bsObj[49].get_text(strip=True).replace(
                '%', '').replace(',', '.').replace('-', '0')),
            float(bsObj[54].get_text(strip=True).replace(
                '%', '').replace(',', '.').replace('-', '0')),
            float(bsObj[59].get_text(strip=True).replace(
                '%', '').replace(',', '.').replace('-', '0')),
            float(bsObj[64].get_text(strip=True).replace(
                '%', '').replace(',', '.').replace('-', '0')),
            float(bsObj[69].get_text(strip=True).replace(
                '%', '').replace(',', '.').replace('-', '0')),
            float(bsObj[74].get_text(strip=True).replace(
                '%', '').replace(',', '.').replace('-', '0')),
            float(bsObj[79].get_text(strip=True).replace(
                '%', '').replace(',', '.').replace('-', '0')),

            float(bsObj[87].get_text(strip=True).replace(
                '.', '').replace('-', '0')),
            float(bsObj[91].get_text(strip=True).replace(
                '.', '').replace('-', '0')),
            float(bsObj[95].get_text(strip=True).replace(
                '.', '').replace('-', '0')),
            float(bsObj[89].get_text(strip=True).replace(
                '.', '').replace('-', '0')),
            float(bsObj[93].get_text(strip=True).replace(
                '.', '').replace('-', '0')),
            float(bsObj[97].get_text(strip=True).replace(
                '.', '').replace('-', '0')),

            float(bsObj[102].get_text(strip=True).replace(
                '.', '').replace('-', '0')),
            float(bsObj[106].get_text(strip=True).replace(
                '.', '').replace('-', '0')),
            float(bsObj[110].get_text(strip=True).replace(
                '.', '').replace('-', '0')),
            float(bsObj[104].get_text(strip=True).replace(
                '.', '').replace('-', '0')),
            float(bsObj[108].get_text(strip=True).replace(
                '.', '').replace('-', '0')),
            float(bsObj[112].get_text(strip=True).replace(
                '.', '').replace('-', '0'))
        ]

        for v in varl:
            print(v)

        Empresa.objects.create(

            papel=(bsObj[1].get_text(strip=True).replace(
                '.', '').replace('-', '0')),
            cotacao=float(bsObj[3].get_text(strip=True).replace(
                '.', '').replace(',', '.').replace('-', '0')),
            tipo=(bsObj[5].get_text(strip=True).replace(
                '.', '').replace('-', '0')),
            data=(bsObj[7].get_text(strip=True).replace(
                '.', '').replace('-', '0')),
            empresa=(bsObj[9].get_text(strip=True).replace(
                '.', '').replace('-', '0')),
            min52=float(bsObj[11].get_text(strip=True).replace(
                ',', '.').replace(',', '.').replace('-', '0')),
            setor=(bsObj[13].get_text(strip=True).replace(
                ',', '.').replace('-', '0')),
            max52=float(bsObj[15].get_text(strip=True).replace(
                '.', '').replace(',', '.').replace('-', '0')),
            subsetor=(bsObj[17].get_text(strip=True).replace(
                '.', '').replace('-', '0')),
            volume=int(bsObj[19].get_text(strip=True).replace(
                '.', '').replace('-', '0')),

            valor_de_mercado=int(bsObj[21].get_text(
                strip=True).replace('.', '').replace('-', '0')),
            ultimo_balanco=(bsObj[23].get_text(
                strip=True).replace('.', '').replace('-', '0')),
            valor_firma=int(bsObj[25].get_text(
                strip=True).replace('.', '').replace('-', '0')),
            num_acoes=int(bsObj[27].get_text(
                strip=True).replace('.', '').replace('-', '0')),

            PL=float(bsObj[32].get_text(strip=True).replace(
                '%', '').replace(',', '.').replace('-', '0')),
            PVP=float(bsObj[37].get_text(strip=True).replace(
                '%', '').replace(',', '.').replace('-', '0')),
            PEBIT=float(bsObj[42].get_text(strip=True).replace(
                '%', '').replace(',', '.').replace('-', '0')),
            PSR=float(bsObj[47].get_text(strip=True).replace(
                '%', '').replace(',', '.').replace('-', '0')),
            PAtivos=float(bsObj[52].get_text(strip=True).replace(
                '%', '').replace(',', '.').replace('-', '0')),
            PCap_Giro=float(bsObj[57].get_text(strip=True).replace(
                '%', '').replace(',', '.').replace('-', '0')),
            PAtivCircLiq=float(bsObj[62].get_text(strip=True).replace(
                '%', '').replace(',', '.').replace('-', '0')),
            dividend_yield=float(bsObj[67].get_text(strip=True).replace(
                '%', '').replace(',', '.').replace('-', '0')),
            ev_ebit=float(bsObj[72].get_text(strip=True).replace(
                '%', '').replace(',', '.').replace('-', '0')),
            giro_ativos=float(bsObj[77].get_text(strip=True).replace(
                '%', '').replace(',', '.').replace('-', '0')),
            crescimento_receita5=float(bsObj[82].get_text(strip=True).replace(
                '%', '').replace(',', '.').replace('-', '0')),
            LPA=float(bsObj[34].get_text(strip=True).replace(
                '%', '').replace(',', '.').replace('-', '0')),
            VPA=float(bsObj[39].get_text(strip=True).replace(
                '%', '').replace(',', '.').replace('-', '0')),
            marg_bruta=float(bsObj[44].get_text(strip=True).replace(
                '%', '').replace(',', '.').replace('-', '0')),
            marg_EBIT=float(bsObj[49].get_text(strip=True).replace(
                '%', '').replace(',', '.').replace('-', '0')),
            marg_liquida=float(bsObj[54].get_text(strip=True).replace(
                '%', '').replace(',', '.').replace('-', '0')),
            EBIT_ATIVO=float(bsObj[59].get_text(strip=True).replace(
                '%', '').replace(',', '.').replace('-', '0')),
            ROIC=float(bsObj[64].get_text(strip=True).replace(
                '%', '').replace(',', '.').replace('-', '0')),
            ROE=float(bsObj[69].get_text(strip=True).replace(
                '%', '').replace(',', '.').replace('-', '0')),
            liquidez_corr=float(bsObj[74].get_text(strip=True).replace(
                '%', '').replace(',', '.').replace('-', '0')),
            diBrPat=float(bsObj[79].get_text(strip=True).replace(
                '%', '').replace(',', '.').replace('-', '0')),

            ativo=int(bsObj[87].get_text(strip=True).replace(
                '.', '').replace('-', '0')),
            disponibilidades=int(bsObj[91].get_text(
                strip=True).replace('.', '').replace('-', '0')),
            ativo_circulante=int(bsObj[95].get_text(
                strip=True).replace('.', '').replace('-', '0')),
            div_bruta=int(bsObj[89].get_text(
                strip=True).replace('.', '').replace('-', '0')),
            div_liquida=int(bsObj[93].get_text(
                strip=True).replace('.', '').replace('-', '0')),
            patrim_liq=int(bsObj[97].get_text(
                strip=True).replace('.', '').replace('-', '0')),

            receita_liq12=int(bsObj[102].get_text(
                strip=True).replace('.', '').replace('-', '0')),
            EBIT12=int(bsObj[106].get_text(strip=True).replace(
                '.', '').replace('-', '0')),
            Lucro_liq12=int(bsObj[110].get_text(
                strip=True).replace('.', '').replace('-', '0')),
            receita_liq3=int(bsObj[104].get_text(
                strip=True).replace('.', '').replace('-', '0')),
            EBIT3=int(bsObj[108].get_text(strip=True).replace(
                '.', '').replace('-', '0')),
            lucro_liq3=int(bsObj[112].get_text(
                strip=True).replace('.', '').replace('-', '0'))
        )


"""
     PL =  float(bsObj[32].get_text(strip=True).replace('%', '').replace(',', '.')),
    PVP =  float(bsObj[37].get_text(strip=True).replace('%', '').replace(',', '.')),
    PEBIT =  float(bsObj[42].get_text(strip=True).replace('%', '').replace(',', '.')),
    PSR =  float(bsObj[47].get_text(strip=True).replace('%', '').replace(',', '.')),
    PAtivos =  float(bsObj[52].get_text(strip=True).replace('%', '').replace(',', '.')),
    PCap_Giro =  float(bsObj[57].get_text(strip=True).replace('%', '').replace(',', '.')),
    PAtivCircLiq =  float(bsObj[62].get_text(strip=True).replace('%', '').replace(',', '.')),
    dividend_yield =  float(bsObj[67].get_text(strip=True).replace('%', '').replace(',', '.')),
    ev_ebit =  float(bsObj[72].get_text(strip=True).replace('%', '').replace(',', '.')),
    giro_ativos =  float(bsObj[77].get_text(strip=True).replace('%', '').replace(',', '.')),
    crescimento_receita5 =  float(bsObj[82].get_text(strip=True).replace('%', '').replace(',', '.')),
    LPA =  float(bsObj[34].get_text(strip=True).replace('%', '').replace(',', '.')),
    VPA =  float(bsObj[39].get_text(strip=True).replace('%', '').replace(',', '.')),
    marg_bruta =  float(bsObj[44].get_text(strip=True).replace('%', '').replace(',', '.')),
    marg_EBIT =  float(bsObj[49].get_text(strip=True).replace('%', '').replace(',', '.')),
    marg_liquida =  float(bsObj[54].get_text(strip=True).replace('%', '').replace(',', '.')),
    EBIT_ATIVO =  float(bsObj[59].get_text(strip=True).replace('%', '').replace(',', '.')),
    ROIC =  float(bsObj[64].get_text(strip=True).replace('%', '').replace(',', '.')),
    ROE =  float(bsObj[69].get_text(strip=True).replace('%', '').replace(',', '.')),
    liquidez_corr =  float(bsObj[74].get_text(strip=True).replace('%', '').replace(',', '.')),
    diBrPat =  float(bsObj[79].get_text(strip=True).replace('%', '').replace(',', '.')),
"""