#!/usr/bin/python
import random
from faker import Faker
from datetime import datetime


fake = Faker()
nome = fake.name()
empresa = fake.company()

def bandeira():
    bandeiras = ["Mastercard", "Visa", "Elo", "American" "Express", "Hipercard"]
    a = random.choice(bandeiras)
    return a

def codigoBandeira():
    number = random.randint(1,10)
    return number


def codigo5digitos():
    number = random.randint(00000, 99999)
    print(number)
    return number
    

def generate_cnpj():
    cnpj = [random.randrange(10) for _ in range(8)] + [0, 0, 0, 1]

    for _ in range(2):
        value = sum(v * (i % 8 + 2) for i, v in enumerate(reversed(cnpj)))
        digit = 11 - value % 11
        cnpj.append(digit if digit < 10 else 0)

    return "".join(str(x) for x in cnpj)

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
    print(number)
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
    return data.strftime('%d/%m/%Y')
    
def dataLancamento():
    datalanc = fake.date('%d/%m/%Y') 
    return datalanc

