classificacao = ('Botafogo','Palmeiras','Flamengo','Bahia', 'Cruzeiro','Sao Paulo','Fortaleza',
                  'Athelico-Pr','Bragatino','Atletico-Mg','Vasco','Inter',
                   'Juventude','Criciuma','Cuiaba','Vitoria','Corinthians',
                    'Gremio','Atletico-go','Fluminense' )
print(f'Os 5 primeiros colocados são: {classificacao [0:5]}')

print(f'Os 4 ultumos colocados são: {classificacao[-4:]}')

alfabeto = sorted(classificacao, key=str.lower)  # Ordena ignorando maiúsculas/minúsculas

print(f'O Cuiaba está na posição {classificacao.index('Cuiaba')+1}')