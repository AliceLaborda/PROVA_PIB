with open("./../dataset/pib_municipio_2010_a_2018.txt", "r", encoding='utf8') as file:
    file = file.readlines()

    vib = []
    # Pega a soma do Valor Interno Bruto da cidade de Manaus e armazena o resultado na lista VIB
    for line in file[1:]:
        line = line.strip().split(";")

        if line[3] == "Manaus":
            soma = float(line[4]) + float(line[5]) + float(line[6]) + float(line[7]) + float(line[8])
            vib.append(soma)


# Salva no txt a media dos valores da lista VIB
with open("./saida_q2.txt", "w", encoding='utf8') as file:
    file.write(f"Valor Interno Bruto: {(sum(vib) / len(vib)):.2f}")
