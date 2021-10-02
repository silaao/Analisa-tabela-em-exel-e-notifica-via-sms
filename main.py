import pandas as pd
from twilio.rest import Client


#Abrir os arquivos Exel.xlsx

lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    # print(mes)
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    # print(tabela_vendas)
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print("o mês com mais de 55 mil é: " f'{mes}. Vendedor: {vendedor}. Vendas: {vendas}')

        # Your Account SID from twilio.com/console
        account_sid = "ACd76f455ac2aad5a20d86ff3eb390ef7c"
        # Your Auth Token from twilio.com/console
        auth_token = "1ca029a2c788dc60ba4a2d11644c944d"

        client = Client(account_sid, auth_token)

        message = client.messages.create(
            to="+5592994867984",
            from_="+18783099281",
            body="o mês com mais de 55 mil é: " f'{mes}. Vendedor: {vendedor}. Vendas: {vendas}')

        print(message.sid)

#verificar na tabela vendas de todos os 6 meses se tem algum valor maior que 55 mil