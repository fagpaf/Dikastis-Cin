def derivada_polinomio(polinomio, ordem):
    def processar_termo(termo):
        # Separando o coeficiente e o expoente de um termo
        if 'x' not in termo:
            return [int(termo), 0]
        else:
            partes = termo.split('x')
            if partes[0] in ['', '+']:
                coeficiente = 1  # Coeficiente implícito positivo
            elif partes[0] == '-':
                coeficiente = -1  # Coeficiente implícito negativo
            else:
                coeficiente = int(partes[0])
            if '^' in partes[1]:
                expoente = int(partes[1].split('^')[1])
            else:
                expoente = 1
            return [coeficiente, expoente]

    def formatar_polinomio(termos):
        # Formatando os termos em uma string de polinômio
        termos_formatados = []
        for coeficiente, expoente in termos:
            if coeficiente == 0:
                continue
            if expoente == 0:
                termos_formatados.append(f"{coeficiente}")
            elif expoente == 1:
                termos_formatados.append(f"{coeficiente}x")
            else:
                termos_formatados.append(f"{coeficiente}x^{expoente}")
        # Concatenando os termos com sinais corretos
        return "+".join(termos_formatados).replace("+-", "-")

    def derivar_termo(termo):
        # calculando a derivada de um termo
        coeficiente, expoente = termo
        if expoente == 0:
            return [0, 0]
        else:
            return [coeficiente * expoente, expoente - 1]

    def derivar_iterativo(termos, ordem):
        # calculando a derivada usando for
        for c in range(ordem):
            termos = [derivar_termo(termo) for termo in termos]
            termos = [termo for termo in termos if termo[0] != 0]
        return termos

    # analisando as entradas
    polinomio = polinomio.replace('-', '+-')  # Tratando sinais negativos
    termos = polinomio.split('+')
    termos = [t.strip() for t in termos if t.strip()]
    termos_processados = [processar_termo(termo) for termo in termos]

    # calculando a derivada de ordem desejada
    derivada_final = derivar_iterativo(termos_processados, ordem)

    # printando a saída
    derivada_formatada = formatar_polinomio(derivada_final)
    print(f"A derivada de ordem {ordem} da função {polinomio.replace('+-', '-')} é:")
    if 'x' not in polinomio:
        print('0')
    else:
        print(derivada_formatada)
    

# entradas
polinomio = input().strip()
ordem = int(input())
derivada_polinomio(polinomio, ordem)
