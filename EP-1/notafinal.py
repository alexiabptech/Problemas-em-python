def nota_final(Q, AI, AF, EP1, EP2, PF):
    # Q = média dos quizzess (a menor dos 5 é descartada)
    # Ni = 0.4 * AI + 0.5 * AF + 0.1 * Q
    # Ng = 0.1 * EP1 + 0.2 * EP2 + 0.7 * PF
    # Nf = (Ni + Ng)/2 if Ni >= 5 and Ng >= 5 
    # Nf =  min(Ni, Ng) if Ni < 5 or Ng < 5 

    Ni = (0.4 * AI) + (0.5 * AF) + (0.1 * Q) 
    Ng = (0.1 * EP1) + (0.2 * EP2) + (0.7 * PF)
    
    if Q < 0 or Q > 10 or AI < 0 or AI > 10 or AF < 0 or AF > 10 or EP1 < 0 or EP1 > 10 or EP2 < 0 or EP2 > 10 or PF < 0 or PF > 10:
        return 0

    if Ni >= 5 and Ng >= 5:
        Nf = (Ni + Ng)/2
        return Nf
    if Ni < 5 or Ng < 5: 
        Nf = min(Ni , Ng)
        return Nf