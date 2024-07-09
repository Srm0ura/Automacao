'''No pyton, assim como qualquer linguagem de programação, vc precisa do passo a passo de como fazer a determinada tarefa
É oque chamamos de "Lógica de programação". Para essa automação, precisamos de 5 passos
1 - Entrar no sistema da empresa
2- Fazer login
3 - Importar a base de dados
4 - Cadastrar o produto
5 - Repetir o passo 4 até finalizar a lista de produtos do passo 3'''

# para começar temos que instalar o Pyautogui - no Terminal - pip install pyautogui
#pyautogui é uma ferramenta que automatiza o seu mouse e teclado. Então é perfeito para automatizações repetitivas.
# Agora importar ele para o nosso codigo para começar a programação

'''Comando que iremos utilizar:
pyautogui.click  - Para usar o clique do mouse
pyautogui.white  - Para escrever um texto
pyautogui.press  - Para apertar um tecla expecifica
pyautogui.hotkey - Para combinações de teclas (ctrl + f4)
pyautogui.scroll - Para rolar a tela.'''

import pyautogui
import time

pyautogui.PAUSE = 1.5

# 1 - Entrar no sistema da empresa
# 1.1 - Abrir o Navegador
pyautogui.press("win")
pyautogui.write("Edger")
pyautogui.press("enter")

#Devido o python ser muito Eficiente, precisamos de uma pausa para alguns comandos, pois se não, o codigo da erro devido a velocidade
# 1.2 - Entrar no Site
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(1)

#2- Fazer login
#2.1 - Clicar na parte do email e senha - Precisaremos criar um codigo auxiliar para ajudar nessa etapa
#Email
pyautogui.click(x=909, y=504)
pyautogui.hotkey("ctrl," "a")
pyautogui.write("meuemail@gmail.com")

# Senha
pyautogui.press("tab")
pyautogui.hotkey("ctrl," "a")
pyautogui.write("1234567")
pyautogui.press("enter")

time.sleep(0.5)

# 3 - Importar a base de dados
# Para importar uma base de dados vamos usar uma ferramenta chamada "Pandas" - Pois é a melhor para trabalhar com uma base de dados. - pip install pandas openpyxl numpy- 
import pandas

produtos = pandas.read_csv("produtos.csv")
 
#4 - Cadastrar o produto
for linha in produtos.index:
    #4.1 codigo
    pyautogui.click (x=811, y= 361)
    codigo = str(produtos.loc[linha,"codigo"]) # Transformei ela em um texto
    pyautogui.write (codigo)
    #4.2 - marca
    marca = str(produtos.loc[linha,"marca"])
    pyautogui.press ("tab")
    pyautogui.write (marca)
    #4.3 - tipo
    tipo = str(produtos.loc[linha,"tipo"])
    pyautogui.press ("tab")
    pyautogui.write (tipo)
    #4.4 - categoria
    categoria = str(produtos.loc[linha,"categoria"])
    pyautogui.press ("tab")
    pyautogui.write (categoria)
    #4.5 - preço
    preco = str(produtos.loc[linha,"preco_unitario"])
    pyautogui.press ("tab")
    pyautogui.write (preco)
    #4.6 - custo
    custo = str(produtos.loc[linha,"custo"])
    pyautogui.press ("tab")
    pyautogui.write (custo)
    #4.7 - observação
    obs = str(produtos.loc[linha,"obs"])
    if obs != "nan":
        pyautogui.write (obs)
    #Enviar
    pyautogui.press ("tab")
    pyautogui.press ("enter")

    #Scroll na tela - Numero positivo = Pra cimaa - Numero negativo = Pra baixo
    pyautogui.scroll ("5000")

#5 - Repetir o passo 4 até finalizar a lista de produtos do passo 3