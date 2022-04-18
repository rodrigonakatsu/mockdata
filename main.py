#!/usr/bin/python
import random
from faker import Faker
from datetime import datetime


fake = Faker('pt_BR')
nome = fake.name()
empresa = fake.company()

#Codigo da empresa
def codigoEmpresa():
    companyid = fake.company_id()
    newid = companyid[:5]
    return newid



def cnpj():
    numerocnpj = fake.cnpj()
    print(numerocnpj)
    return numerocnpj

def bandeiraECodigo():
    bandeiras = [('American Express', '1'), ('Diners Club / Carte Blanche', '2'), ('Discover', '3'), ('JCB 15 digit', '4'),('JCB 16 digit', '5'),('Maestro', '6'),('Mastercard', '7'),('VISA 13 digit', '8'),('VISA 16 digit', '9' ),('VISA 19 digit', '10')]
    randomBand = random.choice(bandeiras)
    return randomBand

def splitbandeiraEcodigo():
    band = bandeiraECodigo()
    x = band[0]
    y= band[1]
    return x,y

def bandeira():
    bandeira = splitbandeiraEcodigo()
    return bandeira

print(bandeira())

def codigoProduct():
    number = random.sample(1,5000)
    return number

def produto():
    teste = bandeira()
    status = [" Venda", " Cancelamento", " Finalizado"]
    a = random.choice(status)
    final = teste + a
    return final

def codRubrica():
    number = random.randint(0000, 9999)
    return number

def rubrica():
    rub = ['Bruto Cessao If Masterm Em R$','Bruto Cessao IF Visa Em R$','Cancelamento De Venda','Chargeback','Compensação De Valores Em Aberto','Desagendamento De Pagamento','Liq Cessao If Amex Em R$','Liq Cessao If EloEm R$']
    choice = random.choice(rub)
    return choice

def codGrupoRubrica():
    number = random.randrange(1,9)
    return number

def grupoRubrica():
    grupos = ['Vendas','Cancelamentos', 'ChargeBack']
    choice = random.choice(grupos)
    return choice

def dataVencimento():
    data = fake.date_between(start_date='today', end_date='+1M')
    print(data.strftime('%d/%m/%Y'))
    return data.strftime('%d/%m/%Y')
    
def dataLancamento():
    datalanc = fake.date('%d/%m/%Y') 
    return datalanc

def dataVencimentoOriginal():
    dataVencimento()

def parcelas():
    parcela = ['1/1','1/2','2/2','1/3','2/3','3/3','1/4','2/4','3/4','4/4']
    random = random.choice(parcela)
    return random
    
def codigoMoeda():
    identificador = ['BRL', 'USD', 'EUR']   
    random = random.choice(identificador)
    return random

def simbolo():
    simbolos = ['R$', '$','€']
    return simbolos

def numeroCartao():
    cartao = fake.credit_card_number()
    return cartao

def nsu():
    number = random.randint(10000000,99999999)
    return nsu()
