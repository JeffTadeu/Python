
try:
    numero1 = input("Qual o primeiro número? ");
    numero2 = input("Qual o segundo número? ");
    operacao = input("Qual das operações a seguir você irá realizar?: '+', '-', '*' ou '/': ");

    if len(operacao) > 1:
        while len(operacao) > 1:
            print("Operação digita errada, tente novamente");
            operacao = input("Qual das operações a seguir você irá realizar?: '+', '-', '*' ou '/': ");
    
    num1 = float(numero1);
    num2 = float(numero2);

    conta = '';


    if operacao == '+':
        conta = num1 + num2;
        print(f'O resultado da sua conta é de {conta}');
    elif operacao == '-':
        conta = num1 - num2;
        print(f'O resultado da sua conta é de {conta}');
    elif operacao == '*':
        conta = num1 * num2;
        print(f'O resultado da sua conta é de {conta}');
    else:
        conta = num1 / num2;
        print(f'O resultado da sua conta é de {conta}');
    
    sair = input("Deseja sair? ").lower();

    while sair != "nao" and sair != "sim":
        print("Por favor, digite 'sim' ou 'nao' ");
        sair = input("Deseja sair? ");

    while sair == "não" or sair == "nao":

        conta = '';

        numero1 = input("Qual o primeiro número? ");
        numero2 = input("Qual o segundo número? ");
        operacao = input("Qual das operações a seguir você irá realizar?: '+', '-', 'x' ou '/': ");

        num1 = float(numero1);
        num2 = float(numero2);

        if operacao == '+':
            conta = num1 + num2;
            print(f'O resultado da sua conta é de {conta}');
        elif operacao == '-':
            conta = num1 - num2;
            print(f'O resultado da sua conta é de {conta}');
        elif operacao == '*':
            conta = num1 * num2;
            print(f'O resultado da sua conta é de {conta}');
        elif operacao == '/':
            conta = num1 / num2;
            print(f'O resultado da sua conta é de {conta}');
        else:
            print("Você nao digitou nenhuma operação disponível acima");

        sair = input("Deseja sair?");
        sair = sair.lower();

        while sair != "nao" and sair != "sim":
            print("Por favor, digite 'sim' ou 'nao' ");
            sair = input("Deseja sair? ").lower;
            
except:
    print("Você digitou informações erradas, siga corretamente as instruções das perguntas. Reinicie o programa.");

