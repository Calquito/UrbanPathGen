import re

# Función para calcular el promedio de los segundos
def calcular_promedio(texto):
    # Buscar todas las coincidencias en el texto usando una expresión regular
    resultados = re.findall(r'Inference time: (\d+\.\d+) seconds', texto)
    
    # Convertir los resultados a números flotantes y calcular el promedio
    if resultados:
        segundos = [float(segundo) for segundo in resultados]
        promedio = sum(segundos) / len(segundos)
        return promedio
    else:
        return 0.0  # Si no se encuentra ninguna coincidencia, el promedio es 0.0

# Ejemplo de uso
texto = """
Drone 1 is reading camera and not taking screenshots
Drone 0 is reading video and not taking screenshots
Drone 2 is reading video and not taking screenshots
Drone 3 is reading video and not taking screenshots
Inference time: 0.559608 seconds
Dron 1 turning towards left
Inference time: 0.485509 seconds
Dron 1 turning towards left
Inference time: 0.475857 seconds
Dron 1 turning towards left
Inference time: 0.469815 seconds
Dron 1 turning towards left
Inference time: 0.538123 seconds
Dron 1 turning towards left
Inference time: 0.773974 seconds
Dron 0 turning towards right
Inference time: 0.824478 seconds
Dron 2 turning towards right
Inference time: 0.893226 seconds
Dron 3 turning towards left
Inference time: 0.806055 seconds
Dron 1 turning towards left
Inference time: 0.471170 seconds
Dron 1 turning towards left
Inference time: 0.479252 seconds
Dron 1 turning towards left
Inference time: 0.469541 seconds
Dron 1 turning towards left
Inference time: 0.709960 seconds
Dron 0 turning towards right
Inference time: 0.805717 seconds
Dron 1 turning towards left
Inference time: 0.994158 seconds
Dron 2 turning towards right
Inference time: 0.903260 seconds
Dron 3 turning towards left
Inference time: 0.695724 seconds
Dron 1 turning towards left
Inference time: 0.482510 seconds
Dron 1 turning towards left
Inference time: 0.482597 seconds
Dron 1 turning towards left
Inference time: 0.489281 seconds
Dron 1 turning towards left
Inference time: 0.492949 seconds
Dron 0 turning towards -0.8169014084507042
Inference time: 0.903010 seconds
Inference time: 0.894402 seconds
Dron 1 turning towards left
Dron 2 turning towards 37.271126760563384
Inference time: 0.942827 seconds
Dron 3 turning towards 37.271126760563384
Inference time: 0.566645 seconds
Dron 1 turning towards left
Inference time: 0.489207 seconds
Dron 1 turning towards left
Inference time: 0.493631 seconds
Dron 1 turning towards left
Inference time: 0.499234 seconds
Dron 1 turning towards left
Inference time: 0.484901 seconds
Dron 0 turning towards 33.901408450704224
Inference time: 0.785678 seconds
Dron 2 turning towards -1.2253521126760563
Inference time: 0.976120 seconds
Dron 1 turning towards left
Inference time: 0.968156 seconds
Dron 3 turning towards -1.2253521126760563
Inference time: 0.529481 seconds
Dron 1 turning towards left
Inference time: 0.500102 seconds
Dron 1 turning towards left
Inference time: 0.490655 seconds
Dron 1 turning towards left
Inference time: 0.555603 seconds
Dron 1 turning towards left
Inference time: 0.623102 seconds
Dron 0 turning towards 15.52112676056338
Inference time: 0.915819 seconds
Dron 2 turning towards 3.676056338028169
Inference time: 1.204739 seconds
Dron 3 turning towards 3.676056338028169
Inference time: 1.241811 seconds
Dron 1 turning towards left
Inference time: 0.694118 seconds
Dron 1 turning towards left
Inference time: 0.534593 seconds
Dron 1 turning towards left
Inference time: 0.524360 seconds
Dron 1 turning towards left
Inference time: 0.766768 seconds
Dron 0 turning towards 26.651408450704224
Inference time: 0.882980 seconds
Dron 1 turning towards left
Inference time: 1.132055 seconds
Dron 2 turning towards 2.859154929577465
Inference time: 1.060958 seconds
Dron 3 turning towards 2.859154929577465
Inference time: 1.029288 seconds
Dron 1 turning towards left
Inference time: 0.602393 seconds
Dron 1 turning towards left
Inference time: 0.500780 seconds
Dron 1 turning towards left
Inference time: 0.531276 seconds
Dron 1 turning towards left
Inference time: 0.603926 seconds
Dron 0 turning towards 2.859154929577465
Inference time: 1.014158 seconds
Dron 1 turning towards left
Inference time: 1.213200 seconds
Dron 2 turning towards 16.746478873239436
Inference time: 1.171118 seconds
Dron 3 turning towards 16.746478873239436
Inference time: 1.036867 seconds
Dron 1 turning towards left
Inference time: 0.590686 seconds
Dron 1 turning towards left
Inference time: 0.489130 seconds
Dron 1 turning towards left
Inference time: 0.481786 seconds
Dron 1 turning towards left
Inference time: 0.461761 seconds
Dron 0 turning towards 18.073943661971832
Inference time: 0.894797 seconds
Dron 1 turning towards left
Inference time: 0.916232 seconds
Dron 2 turning towards right
Inference time: 1.025725 seconds
Dron 3 turning towards left
Inference time: 0.797011 seconds
Dron 1 turning towards left
Inference time: 0.503365 seconds
Dron 1 turning towards left
Inference time: 0.485591 seconds
Dron 1 turning towards left
Inference time: 0.504350 seconds
Dron 1 turning towards left
Inference time: 0.522640 seconds
Dron 0 turning towards -15.827464788732394
Inference time: 0.814243 seconds
Dron 2 turning towards 11.538732394366198
Inference time: 0.997397 seconds
Dron 1 turning towards left
Inference time: 1.078978 seconds
Dron 3 turning towards 11.538732394366198
Inference time: 0.752210 seconds
Dron 1 turning towards left
Inference time: 0.513713 seconds
Dron 1 turning towards left
Inference time: 0.492495 seconds
Dron 1 turning towards left
"""

promedio = calcular_promedio(texto)
print(f"El promedio de los segundos es: {promedio:.6f}")