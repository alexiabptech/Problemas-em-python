def pais_campeao(quadro):
    # Passo 1 - Definição de algumas referências que vão ser necessárias ao decorrer do código
    referencia_pais = ''    
    referencia_ouro = -1    
    referencia_prata = -1    
    referencia_bronze = -1    
    # Passo 2 - Percorre o dicionário (os paises)    
    for pais in quadro:
        medalhas_do_pais = quadro[pais]
        qtde_de_ouros_do_pais = medalhas_do_pais['ouro']
        qtde_de_pratas_do_pais = medalhas_do_pais['prata']
        qtde_de_bronzes_do_pais = medalhas_do_pais['bronze']

        # Passo 3 - Checa o condicional, pro caso do pais ganhar da minha referência
                
        if qtde_de_ouros_do_pais > referencia_ouro:
            referencia_pais = pais            
            referencia_ouro = qtde_de_ouros_do_pais            
            referencia_prata = qtde_de_pratas_do_pais            
            referencia_bronze = qtde_de_bronzes_do_pais  

            # Passo 4 - Checa o empate pelos ouros  
                  
        elif qtde_de_ouros_do_pais == referencia_ouro:
            # Passo 5 - Critério de desempate (usando as pratas)            
            if qtde_de_pratas_do_pais > referencia_prata:
                referencia_pais = pais                
                referencia_prata = qtde_de_pratas_do_pais                
                referencia_bronze = qtde_de_bronzes_do_pais            
                # Passo 6 - Checa o empate pelos bronzes            
                
            elif qtde_de_pratas_do_pais == referencia_prata:
            # Passo 7 - Critério de desempate (usando os bronzes)                
                if qtde_de_bronzes_do_pais > referencia_bronze:
                    referencia_pais = pais                    
                    referencia_bronze = qtde_de_bronzes_do_pais    
    return referencia_pais