# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 16:35:05 2022

@author: matheus.renda
"""
import pandas as pd
###############
# Criando o Tabuleiro

tabuleiro = [["-","-","-"],["-","-","-"],["-","-","-"]]
dt = pd.DataFrame(tabuleiro)
###############
# Jogadores e parâmetros

User1 = "X"
User2 = "O"
start = [True]
jgd = 1
GameOver = 0
log = []
###############
# Condicionais para Vitoria

def Win():
    if (dt.sum(axis = 0)[0] == "XXX" or dt.sum(axis = 0)[1] == "XXX" or dt.sum(axis = 0)[2] == "XXX" 
    or dt.sum(axis = 1)[0] == "XXX" or dt.sum(axis = 1)[1] == "XXX" or dt.sum(axis = 1)[2] == "XXX" 
    or (dt[0][0] == "X" and dt[1][1] == "X" and dt[2][2] == "X")
    or (dt[2][0] == "X" and dt[1][1] == "X" and dt[0][2] == "X")
    or dt.sum(axis = 0)[0] == "OOO" or dt.sum(axis = 0)[1] == "OOO" or dt.sum(axis = 0)[2] == "OOO" 
    or dt.sum(axis = 1)[0] == "OOO" or dt.sum(axis = 1)[1] == "OOO" or dt.sum(axis = 1)[2] == "OOO" 
    or (dt[0][0] == "O" and dt[1][1] == "O" and dt[2][2] == "O")
    or (dt[2][0] == "O" and dt[1][1] == "O" and dt[0][2] == "O")):
        print("\n"*30)
        print("### Ganhou!!! ###")
        print('### Jogador ' + User1 + ' ###') if jgd == 1 else print('### Jogador ' + User2 + ' ###')
        start[0] = False
    else:
        None
###############
# Jogadas e posicionamento de simbulos 

def vez(jgr):
    
    print("\n"*30)
    print('### Jogador ' + User1 + ' ###') if jgr == 1 else print('### Jogador ' + User2 + ' ###')
    print("="*30)
    print(dt)
    print("="*30)
    inpC = int(input ('Selecione Coluna: '))
    inpL = int(input ('Selecione Linha: '))
    
    if dt[inpC][inpL] == "-":
        if jgr == 1:
            dt[inpC][inpL] = User1
            log.append([User1,inpC,inpL])
        else:
            dt[inpC][inpL] = User2
            log.append([User2,inpC,inpL])
    else:
        print("\n"*30)
        print('### Espaço já ocupado, perdeu! :[  ###')
        print('### Jogador ' + User1 + ' ###') if jgr == 1 else print('### Jogador ' + User2 + ' ###')
        start[0] = False       
###############
# Rodando o jogo
        
while start[0] == True:
    
    GameOver += 1
    vez(jgd)
    Win()
    
    if jgd == 1:
        jgd = jgd+1      
    else:
        jgd = jgd-1

    if GameOver == 9:
        start[0] = False
        print("\n"*30)
        print('### Empate... ###')



