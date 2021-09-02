
with open("./../dataset/pib_municipio_2010_a_2018.txt", "r", encoding='utf8') as file:
    file = file.readlines()

    content = []
    names = []


    # Pega o nome de cada município
    for line in file[1:]:
        line = line.strip().split(";")

        if line[0] == "2018":
            if line[2] not in names:
                names.append(line[2])


    # Pega as informações de cada cidade e armazena com seu respectivo município
    for name in names:
        city = {"municipio": name, "city": []}

        for line in file[1:]:
            line = line.strip().split(";")

            if line[0] == "2018":
                if line[2] == name:
                    city["city"].append({"name": line[3], "pib": float(line[9])})

        content.append(city)


# Organiza a lista das cidades pegas e armazena junto com o município a cidade com o maior PIB
for index, element in enumerate(content):
    lista = element["city"]

    aux = True

    while aux:
        aux = False

        for i in range(1, len(lista)):
            if lista[i]["pib"] > lista[i - 1]["pib"]:
                lista[i], lista[i - 1] = lista[i - 1], lista[i]
                aux = True
    
    content[index]["city"] = lista[0]


# Organiza na lista como deve ficar cada linha armazenada dna saída
output = []

for index, line in enumerate(content):
    pos = "0" + str(index + 1)
    output.append(f"{pos[-2:]}º -> Cidade: {line['city']['name']}; Município: {line['municipio']}; PIB: {line['city']['pib']}")


# Salva no txt cada linha formatada
with open("./saida_q1.txt", "w", encoding='utf8') as file:
    file.write("\n".join(output))