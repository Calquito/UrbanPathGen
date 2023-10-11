import re

# Función para calcular el promedio de los segundos
def calcular_promedio(texto):
    # Buscar todas las coincidencias en el texto usando una expresión regular
    resultados = re.findall(r'Execution time: (\d+\.\d+) seconds', texto)
    
    # Convertir los resultados a números flotantes y calcular el promedio
    if resultados:
        segundos = [float(segundo) for segundo in resultados]
        promedio = sum(segundos) / len(segundos)
        return promedio
    else:
        return 0.0  # Si no se encuentra ninguna coincidencia, el promedio es 0.0

# Ejemplo de uso
texto = """Dron 0 moving towards right
Execution time: 0.334330 seconds
Dron 2 moving towards right
Execution time: 0.346115 seconds
Dron 5 moving towards left
Execution time: 0.341311 seconds
Dron 3 moving towards left
Execution time: 0.357724 seconds
Dron 4 moving towards right
Execution time: 0.355763 seconds
Dron 1 moving towards left
Execution time: 0.137666 seconds
Current dron height: 1.1589658588368401
Execution time: 0.092296 seconds
Current dron height: 1.1589658588368401
Execution time: 0.136524 seconds
Dron 2 moving towards right
Execution time: 0.231533 seconds
Current dron height: 1.1589658588368401
Execution time: 0.251870 seconds
Current dron height: 1.1589658588368401
Execution time: 0.272434 seconds
Dron 1 moving towards left
Execution time: 0.156900 seconds
Dron 0 turning towards 61.063380281690144
Execution time: 0.153931 seconds
Dron 3 turning towards 40.13028169014085
Execution time: 0.304413 seconds
Dron 2 turning towards 26.34507042253521
Execution time: 0.364566 seconds
Dron 5 turning towards 61.063380281690144
Execution time: 0.359581 seconds
Dron 4 turning towards 61.063380281690144
Execution time: 0.385255 seconds
Dron 1 moving towards left
Execution time: 0.343104 seconds
Dron 0 turning towards 42.683098591549296
Execution time: 0.186393 seconds
Dron 3 turning towards 42.683098591549296
Execution time: 0.235804 seconds
Dron 1 moving towards left
Execution time: 0.439182 seconds
Dron 2 moving towards right
Execution time: 0.372588 seconds
Dron 4 turning towards 42.683098591549296
Execution time: 0.429308 seconds
Dron 5 turning towards 42.683098591549296
Execution time: 0.560494 seconds
Dron 0 turning towards 53.81338028169014
Execution time: 0.130813 seconds
Dron 1 moving towards left
Execution time: 0.200673 seconds
Dron 3 turning towards 53.91549295774647
Execution time: 0.229463 seconds
Dron 2 moving towards right
Execution time: 0.242663 seconds
Dron 4 turning towards 53.81338028169014
Execution time: 0.292790 seconds
Dron 5 turning towards 53.81338028169014
Execution time: 0.329742 seconds
Dron 0 turning towards 30.02112676056338
Execution time: 0.144477 seconds
Dron 1 moving towards left
Execution time: 0.193300 seconds
Dron 3 turning towards 30.02112676056338
Execution time: 0.204345 seconds
Dron 2 turning towards 47.176056338028175
Execution time: 0.272145 seconds
Dron 4 turning towards 30.02112676056338
Execution time: 0.370347 seconds
Dron 5 turning towards 30.02112676056338
Execution time: 0.432182 seconds
Dron 1 moving towards left
Execution time: 0.078375 seconds
Dron 0 turning towards 45.235915492957744
Execution time: 0.153022 seconds
Dron 3 turning towards 45.235915492957744
Execution time: 0.246420 seconds
Dron 2 moving towards right
Execution time: 0.156324 seconds
Dron 4 turning towards 45.95070422535211
Execution time: 0.232275 seconds
Dron 5 turning towards 45.235915492957744
Execution time: 0.268026 seconds
Dron 1 moving towards left
Execution time: 0.081327 seconds
Dron 3 turning towards 11.33450704225352
Execution time: 0.142577 seconds
Dron 0 turning towards 11.33450704225352
Execution time: 0.129941 seconds
Dron 4 turning towards 11.33450704225352
Execution time: 0.138334 seconds
Dron 5 turning towards 11.33450704225352
Execution time: 0.149081 seconds
Dron 2 turning towards 38.70070422535211
Execution time: 0.227924 seconds
Dron 1 moving towards left
Execution time: 0.100944 seconds
Dron 3 turning towards -2.348591549295775
Execution time: 0.112045 seconds
Dron 0 turning towards -2.348591549295775
Execution time: 0.157811 seconds
Dron 4 turning towards -2.348591549295775
Execution time: 0.137260 seconds
Dron 5 turning towards -2.348591549295775
Execution time: 0.175729 seconds
Dron 2 turning towards 21.954225352112672
Execution time: 0.160886 seconds
Dron 1 moving towards left
Execution time: 0.102701 seconds
Dron 3 turning towards 2.246478873239437
Execution time: 0.125934 seconds
Dron 0 turning towards 2.246478873239437
Execution time: 0.159805 seconds
Dron 4 turning towards 2.246478873239437
Execution time: 0.126671 seconds
Dron 5 turning towards 2.246478873239437
Execution time: 0.142861 seconds
Current dron height: 1.7402066559497038
Execution time: 0.090861 seconds
Dron 1 turning towards -15.9046875
Execution time: 0.103114 seconds
Dron 3 turning towards -0.8169014084507042
Execution time: 0.099913 seconds
Dron 0 turning towards -0.8169014084507042
Execution time: 0.111527 seconds
Dron 4 turning towards -0.8169014084507042
Execution time: 0.107901 seconds
Dron 5 turning towards -0.8169014084507042
Execution time: 0.132664 seconds
Dron 1 moving towards left
Execution time: 0.079501 seconds
Dron 2 turning towards 12.968309859154928
Execution time: 0.134037 seconds
Dron 3 turning towards -8.169014084507042
Execution time: 0.086767 seconds
Dron 0 turning towards -8.169014084507042
Execution time: 0.107268 seconds
Dron 4 turning towards -8.169014084507042
Execution time: 0.109749 seconds
Dron 5 turning towards -8.169014084507042
Execution time: 0.103165 seconds
Dron 1 moving towards left
Execution time: 0.096899 seconds
Dron 2 turning towards 8.985915492957748
Execution time: 0.127808 seconds
Dron 3 moving towards left
Execution time: 0.087260 seconds
Dron 0 moving towards right
Execution time: 0.092721 seconds
Dron 4 moving towards right
Execution time: 0.137206 seconds
Dron 5 moving towards left
Execution time: 0.095306 seconds
Dron 1 moving towards left
Execution time: 0.098053 seconds
Dron 2 turning towards 61.16549295774648
Execution time: 0.136059 seconds
Dron 3 moving towards left
Execution time: 0.086695 seconds
Dron 0 moving towards right
Execution time: 0.095903 seconds
Dron 1 moving towards left
Execution time: 0.147083 seconds
Dron 4 moving towards right
Execution time: 0.183635 seconds
Dron 5 moving towards left
Execution time: 0.203152 seconds
Dron 2 turning towards -3.1654929577464785
Execution time: 0.140700 seconds
Dron 3 turning towards 13.478873239436618
Execution time: 0.086101 seconds
Dron 0 turning towards 13.478873239436618
Execution time: 0.101430 seconds
Dron 1 moving towards left
Execution time: 0.097673 seconds
Dron 4 turning towards 13.478873239436618
Execution time: 0.101501 seconds
Dron 2 moving towards right
Execution time: 0.179673 seconds
Dron 5 turning towards 16.235915492957748
Execution time: 0.229851 seconds
Dron 3 turning towards -0.4084507042253521
Execution time: 0.100940 seconds
Dron 1 moving towards left
Execution time: 0.087464 seconds
Dron 0 turning towards -0.4084507042253521
Execution time: 0.151136 seconds
Dron 4 turning towards -0.4084507042253521
Execution time: 0.134660 seconds
Dron 5 turning towards 0.4084507042253521
Execution time: 0.178660 seconds
Dron 2 moving towards right
Execution time: 0.176177 seconds
Dron 3 turning towards 30.12323943661972
Execution time: 0.108753 seconds
Dron 1 moving towards left
Execution time: 0.082348 seconds
Dron 0 turning towards 30.12323943661972
Execution time: 0.142319 seconds
Dron 4 turning towards 30.12323943661972
Execution time: 0.121878 seconds
Dron 5 turning towards 30.838028169014084
Execution time: 0.154869 seconds
Dron 2 moving towards right
Execution time: 0.192231 seconds
Dron 1 moving towards left
Execution time: 0.113249 seconds
Dron 3 turning towards 28.387323943661972
Execution time: 0.273082 seconds
Dron 0 turning towards 28.387323943661972
Execution time: 0.131632 seconds
Dron 5 turning towards 28.387323943661972
Execution time: 0.189929 seconds
Dron 4 turning towards 28.387323943661972
Execution time: 0.264786 seconds
Dron 2 moving towards right
Execution time: 0.295683 seconds
Dron 1 moving towards left
Execution time: 0.099628 seconds
Dron 3 moving towards left
Execution time: 0.105444 seconds
Dron 0 moving towards right
Execution time: 0.108958 seconds
Dron 5 moving towards left
Execution time: 0.154916 seconds
Dron 4 moving towards right
Execution time: 0.168754 seconds
Dron 2 turning towards 44.316901408450704
Execution time: 0.132927 seconds
Dron 1 moving towards left
Execution time: 0.100631 seconds
Dron 3 turning towards 62.08450704225352
Execution time: 0.146351 seconds
Dron 5 turning towards 62.08450704225352
Execution time: 0.106943 seconds
Dron 4 turning towards 62.08450704225352
Execution time: 0.156153 seconds
Dron 0 turning towards 62.08450704225352
Execution time: 0.172674 seconds
Dron 2 turning towards -2.5528169014084505
Execution time: 0.194476 seconds
Dron 1 moving towards left
Execution time: 0.154247 seconds
Dron 3 moving towards left
Execution time: 0.099425 seconds
Dron 5 moving towards left
Execution time: 0.093235 seconds
Dron 4 moving towards right
Execution time: 0.159635 seconds
Dron 0 moving towards right
Execution time: 0.090885 seconds
Dron 2 moving towards right
Execution time: 0.123705 seconds
Dron 1 moving towards left
Execution time: 0.158629 seconds
Dron 3 moving towards left
Execution time: 0.088237 seconds
Dron 5 moving towards left
Execution time: 0.076951 seconds
Dron 4 moving towards right
Execution time: 0.102779 seconds
Dron 0 moving towards right
Execution time: 0.099927 seconds
Dron 1 moving towards left
Execution time: 0.112515 seconds
Dron 2 moving towards right
Execution time: 0.158682 seconds
Dron 3 turning towards 56.774647887323944
Execution time: 0.134635 seconds
Dron 5 turning towards 56.774647887323944
Execution time: 0.101992 seconds
Dron 4 turning towards 56.774647887323944
Execution time: 0.165351 seconds
Dron 0 turning towards 58.0
Execution time: 0.186547 seconds
Dron 1 moving towards left
Execution time: 0.158934 seconds
Dron 2 turning towards 11.94718309859155
Execution time: 0.269167 seconds
Dron 3 turning towards 32.982394366197184
Execution time: 0.122097 seconds
Dron 5 turning towards 32.982394366197184
Execution time: 0.113971 seconds
Dron 1 moving towards left
Execution time: 0.143814 seconds
Dron 4 turning towards 32.982394366197184
Execution time: 0.287025 seconds
Dron 0 turning towards 32.982394366197184
Execution time: 0.329264 seconds
Current dron height: 1.9774477976284237
Execution time: 0.200689 seconds
Dron 3 turning towards 56.87676056338029
Execution time: 0.203256 seconds
Dron 5 turning towards 56.87676056338029
Execution time: 0.151875 seconds
Dron 1 moving towards left
Execution time: 0.093512 seconds
Dron 4 turning towards 56.87676056338029
Execution time: 0.196859 seconds
Dron 0 turning towards 58.91901408450704
Execution time: 0.199340 seconds
Current dron height: 2.2384130534750155
Execution time: 0.261121 seconds
Dron 3 moving towards left
Execution time: 0.175826 seconds
Dron 5 moving towards left
Execution time: 0.175090 seconds
Dron 1 moving towards left
Execution time: 0.206374 seconds
Dron 4 moving towards right
Execution time: 0.167449 seconds
Dron 0 moving towards right
Execution time: 0.246547 seconds
Current dron height: 2.4934472807796393
Execution time: 0.266649 seconds
Dron 3 moving towards left
Execution time: 0.191226 seconds
Dron 1 moving towards left
Execution time: 0.088828 seconds
Dron 5 moving towards left
Execution time: 0.090124 seconds
Dron 4 moving towards right
Execution time: 0.080232 seconds
Dron 0 moving towards right
Execution time: 0.166400 seconds
Dron 2 moving towards right
Execution time: 0.175347 seconds
Dron 3 moving towards left
Execution time: 0.103532 seconds
Dron 1 moving towards left
Execution time: 0.109299 seconds
Dron 5 moving towards left
Execution time: 0.089759 seconds
Dron 4 moving towards right
Execution time: 0.080862 seconds
Dron 2 moving towards right
Execution time: 0.114433 seconds
Dron 0 moving towards right
Execution time: 0.164754 seconds
Dron 1 moving towards left
Execution time: 0.167347 seconds
Dron 3 moving towards left
Execution time: 0.154691 seconds """


promedio = calcular_promedio(texto)
print(f"El promedio de los segundos es: {promedio:.6f}")