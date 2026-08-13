def formatar_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))

    if len(cpf) == 11:
        return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

    return cpf


def formatar_telefone(telefone):
    telefone = ''.join(filter(str.isdigit, telefone))

    if len(telefone) == 11:
        return f"({telefone[:2]}) {telefone[2:7]}-{telefone[7:]}"

    return telefone