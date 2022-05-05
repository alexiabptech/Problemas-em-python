def compromisso_no_periodo(grade, dia_semana, periodo_dia):
    #grade horaria == dia da semana
    #dia_semana == [0,1,2,3,4]
    #periodo do dia == [0,1, 2, 3]
    #primeiro pega opeíodo do dia, na horizontal, e depois o dia da semana, na vertical
    i = dia_semana #coluna
    j = periodo_dia #linha
    
    if grade[j][i] == '':
        return 'Livre'
    else:
        return grade[j][i]
             
# no grade[0][0], temos 'gde'
#   ['GDE',     'Tópicos', 'NatDes', 'Tópicos',   ''         ],
#    ['DesSoft', 'GDE',     'DesSoft', 'InstruMed', 'NatDes'   ]
# no grade[1][2] temos dessoft