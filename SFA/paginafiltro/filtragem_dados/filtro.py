from ..models import Empresa
from django.db.models import Max, Min


lista_filtros_nomes = [
    {"nome": 'LPA', 'nome_tag': 'LPA'},
    {"nome": 'Crescimento Rec. 5 anos', 'nome_tag': 'crescimento_receita5'},
    {"nome": 'EBIT (12 meses)', 'nome_tag': 'EBIT12'},
    {"nome": 'P/L', 'nome_tag': 'PL'},
    {"nome": 'Patrimônio Líquido', 'nome_tag': 'patrim_liq'},
    {"nome": 'Lucro Líquido (12 Meses)', 'nome_tag': 'Lucro_liq12'},
    {"nome": 'P/VP', 'nome_tag': 'PVP'},
    {"nome": 'Dívida Bruta', 'nome_tag': 'div_bruta'},
    {"nome": 'Receita Líquida (3 meses)', 'nome_tag': 'receita_liq3'},
    {"nome": 'Dividend Yield', 'nome_tag': 'dividend_yield'},
    {"nome": 'Dívida Líquida', 'nome_tag': 'div_liquida'},
    {"nome": 'EBIT (3 Meses)', 'nome_tag': 'EBIT3'},
    {"nome": 'VPA', 'nome_tag': 'VPA'},
    {"nome": 'Receita Líquida (12 meses)', 'nome_tag': 'receita_liq12'},
    {"nome": 'Lucro Líquido (3 Meses)', 'nome_tag': 'lucro_liq3'},
    {"nome": 'Volume médio', 'nome_tag': 'volume'}
]

setores = [
    'Agropecuária',
    'Água e Saneamento',
    'Alimentos',
    'Bebidas',
    'Comércio',
    'Comércio e Distribuição',
    'Computadores e Equipamentos',
    'Construção e Engenharia',
    'Diversos',
    'Embalagens',
    'Energia Elétrica',
    'Equipamentos Elétricos',
    'Exploração de Imóveis',
    'Financeiro',
    'Fumo',
    'Gás',
    'Holdings Diversificadas',
    'Hoteis e Restaurantes',
    'Madeira e Papel',
    'Máquinas e Equipamentos',
    'Materiais Diversos',
    'Material de Transporte',
    'Mídia',
    'Mineração',
    'Outros',
    'Petróleo, Gás e Biocombustíveis',
    'Previdência e Seguros',
    'Prods. de Uso Pessoal e de Limpeza',
    'Programas e Serviço',
    'Químicos',
    'Saúde',
    'Securitizadoras de Recebíveis',
    'Serviços',
    'Serviços Financeiros Diversos',
    'Siderurgia e Metalurgia',
    'Tecidos, Vestuário e Calçados',
    'Telefonia Fixa',
    'Telefonia Móvel',
    'Transporte',
    'Utilidades Domésticas',
    'Viagens e Lazer',
]

lista_filtros = [
    'LPA',
    'crescimento_receita5',
    'EBIT12',
    'patrim_liq',
    'PL',
    'patrim_liq',
    'Lucro_liq12',
    'PVP',
    'div_bruta',
    'receita_liq3',
    'dividend_yield',
    'div_liquida',
    'EBIT3',
    'VPA',
    'receita_liq12',
    'lucro_liq3',
    'volume']

# Filtro de dados pra pegar valor maximos e minimos


def get_max_min_dado(filtro):
    empresa_req = Empresa.objects.all()
    max = int(empresa_req.aggregate(Max(filtro))[filtro+'__max'])
    min = int(empresa_req.aggregate(Min(filtro))[filtro+'__min'])
    return {'max': max, 'min': min}


def get_lista_min_max_dados():
    # resultado = {}
    for filtro in lista_filtros_nomes:
        filtro['limite_valores'] = get_max_min_dado(filtro['nome_tag'])
    return lista_filtros_nomes

# funcoes que filtram do banco de dados

dados = None
valid = False


def get_dados_banco_dados():
    global dados
    dados = Empresa.objects.all()


def isolar_dados_do_banco_por_categoria(option, valor, tag):
    global valid
    global dados

    if(option == 'Maior'):
        d = {tag+'__gte': valor}
        valid = True
        dados = dados.filter(**d)
    elif(option == 'Menor'):
        d = {tag+'__lte': valor}
        valid = True
        dados = dados.filter(**d)
    else:
        return


def print_dados(dados):
    for d in dados:
        print(d)
        print({'LPA': d.LPA, 'Crescimento:': d.crescimento_receita5})


def filtrar_por_setor(setor):
    global dados
    global valid

    if setor == 'Nenhum':
        return
    else:
        valid = True
        dados = dados.filter(setor=setor)

def fitrar_dados(r_value):
    global dados

    get_dados_banco_dados()
    filtrar_por_setor(r_value['setor'])

    for filtro in lista_filtros:
        isolar_dados_do_banco_por_categoria(
            r_value[filtro+'_option'], r_value[filtro], filtro)

    if valid:
        return dados
    else:
        return False
