from ..models import Empresa
import urllib
import urllib.request
from bs4 import BeautifulSoup

_lista_empresas = ['http://www.fundamentus.com.br/detalhes.php?papel=petr4',
                'http://www.fundamentus.com.br/detalhes.php?papel=vale3',
                'http://www.fundamentus.com.br/detalhes.php?papel=bbdc4',
                'http://www.fundamentus.com.br/detalhes.php?papel=petr3',
                'http://www.fundamentus.com.br/detalhes.php?papel=abev3',
                'http://www.fundamentus.com.br/detalhes.php?papel=bbas3',
                'http://www.fundamentus.com.br/detalhes.php?papel=b3sa3',
                'http://www.fundamentus.com.br/detalhes.php?papel=itsa4',
                'http://www.fundamentus.com.br/detalhes.php?papel=lren3',
                'http://www.fundamentus.com.br/detalhes.php?papel=itub4',
                'http://www.fundamentus.com.br/detalhes.php?papel=ugpa3',
                'http://www.fundamentus.com.br/detalhes.php?papel=suzb3',
                'http://www.fundamentus.com.br/detalhes.php?papel=bbdc3',
                'http://www.fundamentus.com.br/detalhes.php?papel=rail3',
                'http://www.fundamentus.com.br/detalhes.php?papel=jbss3',
                'http://www.fundamentus.com.br/detalhes.php?papel=vivt4',
                'http://www.fundamentus.com.br/detalhes.php?papel=rent3',
                'http://www.fundamentus.com.br/detalhes.php?papel=sanb11',
                'http://www.fundamentus.com.br/detalhes.php?papel=krot3',
                'http://www.fundamentus.com.br/detalhes.php?papel=eqtl3',
                'http://www.fundamentus.com.br/detalhes.php?papel=brfs3',
                'http://www.fundamentus.com.br/detalhes.php?papel=brkm5',
                'http://www.fundamentus.com.br/detalhes.php?papel=ggbr4',
                'http://www.fundamentus.com.br/detalhes.php?papel=pcar4',
                'http://www.fundamentus.com.br/detalhes.php?papel=embr3',
                'http://www.fundamentus.com.br/detalhes.php?papel=radl3',
                'http://www.fundamentus.com.br/detalhes.php?papel=wege3',
                'http://www.fundamentus.com.br/detalhes.php?papel=cmig4',
                'http://www.fundamentus.com.br/detalhes.php?papel=cmig3',
                'http://www.fundamentus.com.br/detalhes.php?papel=lame4',
                'http://www.fundamentus.com.br/detalhes.php?papel=mglu3',
                'http://www.fundamentus.com.br/detalhes.php?papel=ciel3',
                'http://www.fundamentus.com.br/detalhes.php?papel=sbsp3',
                'http://www.fundamentus.com.br/detalhes.php?papel=brml3',
                'http://www.fundamentus.com.br/detalhes.php?papel=klbn11',
                'http://www.fundamentus.com.br/detalhes.php?papel=hype3',
                'http://www.fundamentus.com.br/detalhes.php?papel=egie3',
                'http://www.fundamentus.com.br/detalhes.php?papel=timp3',
                'http://www.fundamentus.com.br/detalhes.php?papel=elet3',
                'http://www.fundamentus.com.br/detalhes.php?papel=csna3',
                'http://www.fundamentus.com.br/detalhes.php?papel=estc3',
                'http://www.fundamentus.com.br/detalhes.php?papel=btow3',
                'http://www.fundamentus.com.br/detalhes.php?papel=brdt3',
                'http://www.fundamentus.com.br/detalhes.php?papel=natu3',
                'http://www.fundamentus.com.br/detalhes.php?papel=cvcb3',
                'http://www.fundamentus.com.br/detalhes.php?papel=elet6',
                'http://www.fundamentus.com.br/detalhes.php?papel=brap4',
                'http://www.fundamentus.com.br/detalhes.php?papel=csan3',
                'http://www.fundamentus.com.br/detalhes.php?papel=mult3',
                'http://www.fundamentus.com.br/detalhes.php?papel=flry3',
                'http://www.fundamentus.com.br/detalhes.php?papel=taee11',
                'http://www.fundamentus.com.br/detalhes.php?papel=enbr3',
                'http://www.fundamentus.com.br/detalhes.php?papel=usim5',
                'http://www.fundamentus.com.br/detalhes.php?papel=cyre3',]
# tratamento na parte de pegar os dados - corrigir inconsistencias

lista_empresas = [
                'http://www.fundamentus.com.br/detalhes.php?papel=petr4', 
                'http://www.fundamentus.com.br/detalhes.php?papel=vale3', 
                'http://www.fundamentus.com.br/detalhes.php?papel=bbdc4', 
                'http://www.fundamentus.com.br/detalhes.php?papel=petr3', 
                'http://www.fundamentus.com.br/detalhes.php?papel=abev3', 
                'http://www.fundamentus.com.br/detalhes.php?papel=bbas3',
                'http://www.fundamentus.com.br/detalhes.php?papel=b3sa3',
                'http://www.fundamentus.com.br/detalhes.php?papel=itsa4',
                'http://www.fundamentus.com.br/detalhes.php?papel=lren3',
                'http://www.fundamentus.com.br/detalhes.php?papel=itub4',
                'http://www.fundamentus.com.br/detalhes.php?papel=ugpa3',
                'http://www.fundamentus.com.br/detalhes.php?papel=suzb3',
                'http://www.fundamentus.com.br/detalhes.php?papel=bbdc3',
                'http://www.fundamentus.com.br/detalhes.php?papel=rail3',
                'http://www.fundamentus.com.br/detalhes.php?papel=jbss3',
                'http://www.fundamentus.com.br/detalhes.php?papel=vivt4',
                'http://www.fundamentus.com.br/detalhes.php?papel=rent3',
                'http://www.fundamentus.com.br/detalhes.php?papel=bbse3',
                'http://www.fundamentus.com.br/detalhes.php?papel=sanb11',
                'http://www.fundamentus.com.br/detalhes.php?papel=krot3',
                'http://www.fundamentus.com.br/detalhes.php?papel=eqtl3',
                'http://www.fundamentus.com.br/detalhes.php?papel=brfs3',
                'http://www.fundamentus.com.br/detalhes.php?papel=brkm5',
                'http://www.fundamentus.com.br/detalhes.php?papel=ggbr4',
                'http://www.fundamentus.com.br/detalhes.php?papel=pcar4',
                'http://www.fundamentus.com.br/detalhes.php?papel=embr3',
                'http://www.fundamentus.com.br/detalhes.php?papel=radl3',
                'http://www.fundamentus.com.br/detalhes.php?papel=wege3',
                'http://www.fundamentus.com.br/detalhes.php?papel=cmig4',
                'http://www.fundamentus.com.br/detalhes.php?papel=cmig3',
                'http://www.fundamentus.com.br/detalhes.php?papel=lame4',
                'http://www.fundamentus.com.br/detalhes.php?papel=mglu3',
                'http://www.fundamentus.com.br/detalhes.php?papel=ciel3',
                'http://www.fundamentus.com.br/detalhes.php?papel=sbsp3',
                'http://www.fundamentus.com.br/detalhes.php?papel=brml3',
                'http://www.fundamentus.com.br/detalhes.php?papel=klbn11',
                'http://www.fundamentus.com.br/detalhes.php?papel=hype3',
                'http://www.fundamentus.com.br/detalhes.php?papel=egie3',
                'http://www.fundamentus.com.br/detalhes.php?papel=timp3',
                'http://www.fundamentus.com.br/detalhes.php?papel=elet3',
                'http://www.fundamentus.com.br/detalhes.php?papel=csna3',
                'http://www.fundamentus.com.br/detalhes.php?papel=estc3',
                'http://www.fundamentus.com.br/detalhes.php?papel=btow3',
                'http://www.fundamentus.com.br/detalhes.php?papel=brdt3',
                'http://www.fundamentus.com.br/detalhes.php?papel=natu3',
                'http://www.fundamentus.com.br/detalhes.php?papel=cvcb3',
                'http://www.fundamentus.com.br/detalhes.php?papel=elet6',
                'http://www.fundamentus.com.br/detalhes.php?papel=brap4',
                'http://www.fundamentus.com.br/detalhes.php?papel=csan3',
                'http://www.fundamentus.com.br/detalhes.php?papel=mult3',
                'http://www.fundamentus.com.br/detalhes.php?papel=flry3',
                'http://www.fundamentus.com.br/detalhes.php?papel=taee11',
                'http://www.fundamentus.com.br/detalhes.php?papel=enbr3',
                'http://www.fundamentus.com.br/detalhes.php?papel=usim5',
                'http://www.fundamentus.com.br/detalhes.php?papel=cyre3',
                'http://www.fundamentus.com.br/detalhes.php?papel=ccro3',
                'http://www.fundamentus.com.br/detalhes.php?papel=cpfe3',
                'http://www.fundamentus.com.br/detalhes.php?papel=qual3',
                'http://www.fundamentus.com.br/detalhes.php?papel=mrve3',
                'http://www.fundamentus.com.br/detalhes.php?papel=goau4',
                'http://www.fundamentus.com.br/detalhes.php?papel=igta3',
                'http://www.fundamentus.com.br/detalhes.php?papel=goll4',
                'http://www.fundamentus.com.br/detalhes.php?papel=smls3',
                'http://www.fundamentus.com.br/detalhes.php?papel=mrfg3',
                'http://www.fundamentus.com.br/detalhes.php?papel=ecor3',
                'http://www.fundamentus.com.br/detalhes.php?papel=vvar3',
                'http://www.fundamentus.com.br/detalhes.php?papel=logg3',
                'http://www.fundamentus.com.br/detalhes.php?papel=azul4',
                'http://www.fundamentus.com.br/detalhes.php?papel=alsc3',
                'http://www.fundamentus.com.br/detalhes.php?papel=crfb3',
                'http://www.fundamentus.com.br/detalhes.php?papel=pcar4',
                'http://www.fundamentus.com.br/detalhes.php?papel=cesp6',
                'http://www.fundamentus.com.br/detalhes.php?papel=engi11',
                'http://www.fundamentus.com.br/detalhes.php?papel=sled3',
                'http://www.fundamentus.com.br/detalhes.php?papel=bidi4',
                'http://www.fundamentus.com.br/detalhes.php?papel=prio3',
                'http://www.fundamentus.com.br/detalhes.php?papel=alup11',
                'http://www.fundamentus.com.br/detalhes.php?papel=amar3',
                'http://www.fundamentus.com.br/detalhes.php?papel=baza3',
                'http://www.fundamentus.com.br/detalhes.php?papel=abcb4',
                'http://www.fundamentus.com.br/detalhes.php?papel=arzz3',
                'http://www.fundamentus.com.br/detalhes.php?papel=irbr3',
                'http://www.fundamentus.com.br/detalhes.php?papel=gndi3',
                'http://www.fundamentus.com.br/detalhes.php?papel=bpac11',
                'http://www.fundamentus.com.br/detalhes.php?papel=sapr11',
                'http://www.fundamentus.com.br/detalhes.php?papel=hapv3',
                'http://www.fundamentus.com.br/detalhes.php?papel=crfb3',
                'http://www.fundamentus.com.br/detalhes.php?papel=hgtx3',
                'http://www.fundamentus.com.br/detalhes.php?papel=tots3',
                'http://www.fundamentus.com.br/detalhes.php?papel=qgep3',
                'http://www.fundamentus.com.br/detalhes.php?papel=pssa3',
                'http://www.fundamentus.com.br/detalhes.php?papel=btow3',
                'http://www.fundamentus.com.br/detalhes.php?papel=ligt3',
                'http://www.fundamentus.com.br/detalhes.php?papel=taee11',
                'http://www.fundamentus.com.br/detalhes.php?papel=sula11',
                'http://www.fundamentus.com.br/detalhes.php?papel=linx3',
                'http://www.fundamentus.com.br/detalhes.php?papel=lcam3',
                'http://www.fundamentus.com.br/detalhes.php?papel=csmg3',
                'http://www.fundamentus.com.br/detalhes.php?papel=caml3',
                'http://www.fundamentus.com.br/detalhes.php?papel=mdia3',
                'http://www.fundamentus.com.br/detalhes.php?papel=sapr4',
                'http://www.fundamentus.com.br/detalhes.php?papel=rapt4',
                'http://www.fundamentus.com.br/detalhes.php?papel=odpv3',
                'http://www.fundamentus.com.br/detalhes.php?papel=slce3',
                'http://www.fundamentus.com.br/detalhes.php?papel=cple6',
                'http://www.fundamentus.com.br/detalhes.php?papel=brsr6',
                'http://www.fundamentus.com.br/detalhes.php?papel=eztc3',
                'http://www.fundamentus.com.br/detalhes.php?papel=gfsa3',
                'http://www.fundamentus.com.br/detalhes.php?papel=beef3',
                'http://www.fundamentus.com.br/detalhes.php?papel=itub3',
                'http://www.fundamentus.com.br/detalhes.php?papel=pomo4',
                'http://www.fundamentus.com.br/detalhes.php?papel=bkbr3',
                'http://www.fundamentus.com.br/detalhes.php?papel=grnd3',
                'http://www.fundamentus.com.br/detalhes.php?papel=seer3',
                'http://www.fundamentus.com.br/detalhes.php?papel=dtex3',
                'http://www.fundamentus.com.br/detalhes.php?papel=tend3',
                'http://www.fundamentus.com.br/detalhes.php?papel=mypk3',
                'http://www.fundamentus.com.br/detalhes.php?papel=alpa4',
                'http://www.fundamentus.com.br/detalhes.php?papel=tupy3',
                'http://www.fundamentus.com.br/detalhes.php?papel=movi3'
]

def get_dado_inteiro(dado):
    if dado.get_text(strip=True) == '-':
        return None
    else:
        return int(dado.get_text(strip=True).replace('.', ''))


def get_dado_decimal(dado):
    if dado.get_text(strip=True) == '-':
        return None
    else:
        return float(dado.get_text(strip=True).replace('%', '').replace(',', '.'))


def get_dado_string(dado):
    if dado.get_text(strip=True) == '-':
        return None
    else:
        return dado.get_text(strip=True)

# funcao principal - puxa todos os dados e salva os mesmos no banco de dados

def _inserir_dado_no_banco(bsObj):

    Empresa.objects.create(

        # text
        papel=get_dado_string(bsObj[1]),
        # text
        tipo=get_dado_string(bsObj[5]),
        # text
        data=get_dado_string(bsObj[7]),
        # text
        empresa=get_dado_string(bsObj[9]),
        # text
        setor=get_dado_string(bsObj[13]),
        # text
        subsetor=get_dado_string(bsObj[17]),
        # text
        ultimo_balanco=get_dado_string(bsObj[23]),

        cotacao=get_dado_decimal(bsObj[3]),

        min52=get_dado_decimal(bsObj[11]),

        max52=get_dado_decimal(bsObj[15]),

        volume=get_dado_inteiro(bsObj[19]),

        valor_de_mercado=get_dado_inteiro(bsObj[21]),

        valor_firma=get_dado_inteiro(bsObj[25]),
        num_acoes=get_dado_inteiro(bsObj[27]),

        PL=get_dado_decimal(bsObj[32]),
        PVP=get_dado_decimal(bsObj[37]),
        PEBIT=get_dado_decimal(bsObj[42]),
        PSR=get_dado_decimal(bsObj[47]),
        PAtivos=get_dado_decimal(bsObj[52]),
        PCap_Giro=get_dado_decimal(bsObj[57]),
        PAtivCircLiq=get_dado_decimal(bsObj[62]),
        dividend_yield=get_dado_decimal(bsObj[67]),
        ev_ebit=get_dado_decimal(bsObj[72]),
        giro_ativos=get_dado_decimal(bsObj[77]),
        crescimento_receita5=get_dado_decimal(bsObj[82]),
        LPA=get_dado_decimal(bsObj[34]),
        VPA=get_dado_decimal(bsObj[39]),
        marg_bruta=get_dado_decimal(bsObj[44]),
        marg_EBIT=get_dado_decimal(bsObj[49]),
        marg_liquida=get_dado_decimal(bsObj[54]),
        EBIT_ATIVO=get_dado_decimal(bsObj[59]),
        ROIC=get_dado_decimal(bsObj[64]),
        ROE=get_dado_decimal(bsObj[69]),
        liquidez_corr=get_dado_decimal(bsObj[74]),
        diBrPat=get_dado_decimal(bsObj[79]),

        ativo=get_dado_inteiro(bsObj[87]),
        disponibilidades=get_dado_inteiro(bsObj[91]),
        ativo_circulante=get_dado_inteiro(bsObj[95]),
        div_bruta=get_dado_inteiro(bsObj[89]),
        div_liquida=get_dado_inteiro(bsObj[93]),
        patrim_liq=get_dado_inteiro(bsObj[97]),

        receita_liq12=get_dado_inteiro(bsObj[102]),
        EBIT12=get_dado_inteiro(bsObj[106]),
        Lucro_liq12=get_dado_inteiro(bsObj[110]),
        receita_liq3=get_dado_inteiro(bsObj[104]),
        EBIT3=get_dado_inteiro(bsObj[108]),
        lucro_liq3=get_dado_inteiro(bsObj[112])
    )

def inserir_dados_no_banco():
    for emp in lista_empresas:
        try:
            html = urllib.request.urlopen(emp)
            bsObj = BeautifulSoup(html.read(), 'html.parser')
            bsObj = bsObj.find_all(class_='txt')
            _inserir_dado_no_banco(bsObj)
        except:
            print("Houve erro ao carregar o link: ")
            print(emp)
        

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
