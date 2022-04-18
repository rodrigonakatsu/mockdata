#!/usr/bin/python
import random
from faker import Faker
from datetime import datetime
import csv

fake = Faker('pt_BR')
nome = fake.name()

#Codigo da empresa
def codigoEmpresa():
    companyid = fake.company_id()
    print(companyid)
    return companyid


def empresa():
    empresa = fake.company()
    return empresa

def bandeira():
    bandeiras = ["Mastercard", "Visa", "Elo", "American Express", "Hipercard"]
    a = random.choice(bandeiras)
    return a

def codigoBandeira():
    number = random.randint(1,9)
    return number
    
def fakedate():
    print(fake.date())


def cnpj():
    numerocnpj = fake.cnpj()
    print(numerocnpj)
    return numerocnpj



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

def cc():
    re = fake.credit_card_provider()
    return re

with open('testcsv', 'a', newline='') as csvfile:
    csv = csv.writer(csvfile)
    #for i in range(0,5000):
        #csv.writerow([cc()])
        #csv.writerow([empresa()])
        #codigoBandeira()
        #csv.writerow([bandeira()])
        #codigoProduct()
        #csv.writerow([produto()])

def ofi():
    o = fake.credit_card_full()
    print(o)
    return o
ofi()
