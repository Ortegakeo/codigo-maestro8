import tkinter as tk
from tkinter import messagebox, font, Scrollbar, Text, Frame

# ============================================================
# CODEFORGE BIOMÉDICO MASTER STUDY
# Autor: ñauñauñau 🧬
#
# OBJETIVO:
#  - Tener un banco gigante de códigos clínicos/matemáticos
#    exactamente en el estilo que les piden en evaluaciones.
#  - Cada código ya viene con:
#      * manejo de error try/except
#      * comentarios claros
#      * variables entendibles
#      * loops simples
#  - Todo offline, sin librerías externas raras.
#
# CATEGORÍAS:
#   Glucosa
#   IMC / Riesgo metabólico
#   Presión arterial
#   Frecuencia cardíaca
#   HOMA-IR
#   EVA / Dolor
#   ADN / Genómica
#   Pacientes y Camas UCI
#   Mini Base de Datos de Enfermedades
#   Herramientas base (listas, for, while, try/except)
#
# NIVELES:
#   Básico     -> 1 solo cálculo / clasificación
#   Normal     -> promedio / conteos básicos
#   Medio      -> porcentajes, tabulación, alerta riesgo
#   Complejo   -> lógica clínica tipo ficha hospital real
#
# INTERFAZ:
#   - Izquierda: botones de (Tema - Nivel)
#   - Derecha arriba: explicación humana tipo compañero
#   - Derecha abajo: código completo listo para copiar
#
# BOTÓN copiar: copia el código al portapapeles
#
# ============================================================

LESSONS = {
    # ========================================================
    # G L U C O S A
    # ========================================================
    "Glucosa - Básico": {
        "explain":
            "Glucosa en ayunas de UN paciente.\n"
            "Clasifica en Normal / Prediabetes / Diabetes.\n"
            "Incluye try/except para que no se caiga si alguien escribe letras.\n"
            "⚕️ Esto es lo más clásico del certamen.",
        "code": """\
# Clasificación de glucosa en ayunas
# Criterio:
#   <100 mg/dL  -> Normal
#   100-125     -> Prediabetes
#   >=126       -> Diabetes

try:
    glucosa = float(input("Ingrese glucosa en ayunas (mg/dL): "))

    if glucosa < 100:
        print("Clasificación: Normal")
    elif glucosa < 126:
        print("Clasificación: Prediabetes")
    else:
        print("Clasificación: Diabetes")

except:
    print("Error: Debe ingresar un número válido (ej: 110.5)")
"""
    },

    "Glucosa - Normal": {
        "explain":
            "Múltiples pacientes.\n"
            "Calcula promedio, máximo y mínimo.\n"
            "Esto lo usan para describir un grupo.\n"
            "Incluye acumulador manual (suma) en for.",
        "code": """\
# Promedio, máximo y mínimo de glucosa en un grupo

try:
    n = int(input("¿Cuántos pacientes vas a ingresar?: "))

    glucosas = []
    for i in range(n):
        while True:
            try:
                g = float(input(f"Glucosa paciente {i+1} (mg/dL): "))
                glucosas.append(g)
                break
            except:
                print("Valor inválido. Ingresa número.")

    # Cálculo promedio, min, max SIN romperse
    suma = 0
    minimo = glucosas[0]
    maximo = glucosas[0]

    for g in glucosas:
        suma += g
        if g < minimo:
            minimo = g
        if g > maximo:
            maximo = g

    promedio = suma / len(glucosas)

    print("\\nResumen del grupo:")
    print("Promedio:", round(promedio,1), "mg/dL")
    print("Mínimo:", minimo, "mg/dL")
    print("Máximo:", maximo, "mg/dL")

except:
    print("Error inesperado. Revisa los datos.")
"""
    },

    "Glucosa - Medio": {
        "explain":
            "Clasifica cada paciente y cuenta cuántos son Normal / Prediabetes / Diabetes.\n"
            "Entrega porcentajes. Eso ya parece informe de salud pública.",
        "code": """\
# Distribución de estados glicémicos en el grupo

try:
    total = int(input("¿Cuántos pacientes en total?: "))

    normal = 0
    predi = 0
    diab = 0

    for i in range(total):
        while True:
            try:
                g = float(input(f"Glucosa paciente {i+1} (mg/dL): "))
                break
            except:
                print("Ingresa número válido por favor.")

        if g < 100:
            normal += 1
        elif g < 126:
            predi += 1
        else:
            diab += 1

    print("\\nResultados:")
    print("Normal:", normal, f"({normal/total*100:.1f}%)")
    print("Prediabetes:", predi, f"({predi/total*100:.1f}%)")
    print("Diabetes:", diab, f"({diab/total*100:.1f}%)")

except:
    print("No se pudo procesar el grupo.")
"""
    },

    "Glucosa - Complejo": {
        "explain":
            "Arma una tabla paciente a paciente.\n"
            "Muestra quién necesita 'ALERTA' (diabético).\n"
            "Esto es MUY parecido a una pauta de certamen largo.",
        "code": """\
# Tabla de glucosa por paciente + alerta

try:
    n = int(input("¿Cuántos pacientes?: "))

    nombres = []
    glucosas = []
    estados = []
    alertas = []

    for i in range(n):
        nombre = input(f"Nombre del paciente {i+1}: ")

        # forzar que la glucosa sea numérica
        while True:
            try:
                g = float(input("Glucosa (mg/dL): "))
                break
            except:
                print("Dato inválido, usa número.")

        # clasificar
        if g < 100:
            estado = "Normal"
            alerta = "OK"
        elif g < 126:
            estado = "Prediabetes"
            alerta = "Control"
        else:
            estado = "Diabetes"
            alerta = "ALERTA"

        nombres.append(nombre)
        glucosas.append(g)
        estados.append(estado)
        alertas.append(alerta)

    print("\\nPACIENTE\\tGLUCOSA\\tESTADO\\tSEGUIMIENTO")
    print("-------------------------------------------------")
    for i in range(nombres.__len__()):
        print(nombres[i], "\\t", glucosas[i], "\\t", estados[i], "\\t", alertas[i])

except:
    print("Error general al procesar pacientes.")
"""
    },

    # ========================================================
    # I M C  /  R I E S G O   M E T A B Ó L I C O
    # ========================================================
    "IMC - Básico": {
        "explain":
            "Calcula IMC de una persona.\n"
            "IMC = peso / talla^2.\n"
            "Incluye try/except.",
        "code": """\
# Cálculo de IMC individual

try:
    peso = float(input("Peso (kg): "))
    talla = float(input("Talla (m): "))

    imc = peso / (talla**2)
    print("IMC:", round(imc,2))

except:
    print("Dato inválido. Recuerda usar números (ej: 70.5)")
"""
    },

    "IMC - Normal": {
        "explain":
            "IMC + clasificación nutricional estándar (Bajo peso / Normal / Sobrepeso / Obesidad).",
        "code": """\
# IMC + Clasificación nutricional

try:
    peso = float(input("Peso (kg): "))
    talla = float(input("Talla (m): "))

    imc = peso / (talla**2)

    if imc < 18.5:
        clase = "Bajo peso"
    elif imc < 25:
        clase = "Normal"
    elif imc < 30:
        clase = "Sobrepeso"
    else:
        clase = "Obesidad"

    print("IMC:", round(imc,2), "| Estado:", clase)

except:
    print("Error en ingreso. Usa números válidos.")
"""
    },

    "IMC - Medio": {
        "explain":
            "Ingresa varios pacientes.\n"
            "Para cada uno: peso, talla, cintura, sexo.\n"
            "Evalúa riesgo metabólico por cintura (hombre >102 cm, mujer >88 cm).",
        "code": """\
# Perfil metabólico simple: IMC + riesgo por cintura

try:
    n = int(input("¿Cuántos pacientes?: "))

    for i in range(n):
        nombre = input(f"Nombre Paciente {i+1}: ")

        while True:
            try:
                peso = float(input("Peso (kg): "))
                talla = float(input("Talla (m): "))
                cintura = float(input("Perímetro cintura (cm): "))
                sexo = input("Sexo (MASCULINO/FEMENINO): ").upper()
                break
            except:
                print("Error. Ingresa números donde corresponde.")

        imc = peso / (talla**2)

        # Clasificación IMC
        if imc < 18.5:
            estado_imc = "Bajo peso"
        elif imc < 25:
            estado_imc = "Normal"
        elif imc < 30:
            estado_imc = "Sobrepeso"
        else:
            estado_imc = "Obesidad"

        # Riesgo por cintura
        if sexo == "MASCULINO":
            riesgo_cintura = "RIESGO" if cintura > 102 else "OK"
        else:
            riesgo_cintura = "RIESGO" if cintura > 88 else "OK"

        print("----- Resumen Paciente -----")
        print("Nombre:", nombre)
        print("IMC:", round(imc,1), "-", estado_imc)
        print("Cintura:", cintura, "cm |", riesgo_cintura)

except:
    print("Fallo en el registro de pacientes.")
"""
    },

    "IMC - Complejo": {
        "explain":
            "Calcula % de pacientes con sobrepeso/obesidad.\n"
            "Sirve para 'estado nutricional del grupo' en un pabellón / sala.",
        "code": """\
# % de pacientes en sobrepeso/obesidad dentro del grupo

try:
    total = int(input("¿Cuántos pacientes vas a evaluar?: "))

    sobrepeso_obesos = 0

    for i in range(total):
        while True:
            try:
                peso = float(input("Peso (kg): "))
                talla = float(input("Talla (m): "))
                break
            except:
                print("Dato inválido.")

        imc = peso / (talla**2)

        if imc >= 25:
            sobrepeso_obesos += 1

    porcentaje = (sobrepeso_obesos / total) * 100
    print("Sobrepeso+Obesidad:", round(porcentaje,1), "% del grupo")

except:
    print("Error general al analizar el grupo.")
"""
    },

    # ========================================================
    # P R E S I Ó N   A R T E R I A L
    # ========================================================
    "Presión - Básico": {
        "explain":
            "Toma presión ANTES y DESPUÉS de tratamiento de un paciente.\n"
            "Entrega cuánto bajó (reducción mmHg).",
        "code": """\
# Reducción de presión arterial en un paciente

try:
    presion_antes = float(input("Presión antes (mmHg): "))
    presion_despues = float(input("Presión después (mmHg): "))

    reduccion = presion_antes - presion_despues
    print("Reducción:", reduccion, "mmHg")

except:
    print("Error en los datos ingresados.")
"""
    },

    "Presión - Normal": {
        "explain":
            "Clasifica el resultado del tratamiento antihipertensivo:\n"
            " - Efectiva (≥20mmHg)\n"
            " - Moderada (10-19)\n"
            " - Nula (<10).",
        "code": """\
# Efectividad del tratamiento antihipertensivo

try:
    a = float(input("Presión antes (mmHg): "))
    d = float(input("Presión después (mmHg): "))

    dif = a - d

    if dif >= 20:
        clase = "Efectiva"
    elif dif >= 10:
        clase = "Moderada"
    else:
        clase = "Nula"

    print("Reducción:", dif, "mmHg |", clase)

except:
    print("Error: ingrese sólo números.")
"""
    },

    "Presión - Medio": {
        "explain":
            "Analiza un GRUPO.\n"
            "Calcula el promedio de reducción de presión.\n"
            "Esto es típico en taller grupal.",
        "code": """\
# Promedio de reducción de presión arterial en un grupo

try:
    n = int(input("¿Cuántos pacientes?: "))

    reducciones = []

    for i in range(n):
        while True:
            try:
                a = float(input("Antes (mmHg): "))
                d = float(input("Después (mmHg): "))
                reducciones.append(a-d)
                break
            except:
                print("Dato inválido, intenta otra vez.")

    total_red = 0
    for r in reducciones:
        total_red += r

    promedio = total_red / len(reducciones)

    print("Reducción promedio:", round(promedio,1), "mmHg")

except:
    print("No se pudo calcular promedio.")
"""
    },

    "Presión - Complejo": {
        "explain":
            "Entrega tabla estilo ficha clínica.\n"
            "Muestra cada paciente con: Antes / Después / Reducción / Clasificación.",
        "code": """\
# Tabla de respuesta al tratamiento antihipertensivo

try:
    n = int(input("¿Cuántos pacientes vas a evaluar?: "))

    print("PAC\tANTES\tDESP\tREDUCCION\tCLASIFICACION")
    print("--------------------------------------------------")

    for i in range(n):
        while True:
            try:
                a = float(input("Presión antes: "))
                b = float(input("Presión después: "))
                break
            except:
                print("Debes usar números válidos.")

        redu = a - b

        if redu >= 20:
            etiqueta = "Efectiva"
        elif redu >= 10:
            etiqueta = "Moderada"
        else:
            etiqueta = "Nula"

        print(i+1, "\\t", a, "\\t", b, "\\t", redu, "\\t\\t", etiqueta)

except:
    print("Error procesando las mediciones.")
"""
    },

    # ========================================================
    # F R E C U E N C I A   C A R D Í A C A
    # ========================================================
    "FC - Básico": {
        "explain":
            "Frecuencia cardíaca única.\n"
            "<60 = Baja, 60-100 = Normal, >100 = Alta.\n"
            "Esto sale siempre.",
        "code": """\
# Clasificación frecuencia cardíaca individual

try:
    fc = float(input("Frecuencia cardíaca (bpm): "))

    if fc < 60:
        estado = "Baja"
    elif fc <= 100:
        estado = "Normal"
    else:
        estado = "Alta"

    print("Estado FC:", estado)

except:
    print("Valor inválido.")
"""
    },

    "FC - Normal": {
        "explain":
            "Toma varias FC y saca el promedio y % de normales.\n"
            "Esto ya es mini informe.",
        "code": """\
# Análisis grupal de frecuencia cardíaca

try:
    n = int(input("¿Cuántos pacientes?: "))

    datos = []
    for i in range(n):
        while True:
            try:
                valor = float(input(f"FC paciente {i+1} (bpm): "))
                datos.append(valor)
                break
            except:
                print("Ingresa un número, no letras.")

    # promedio
    suma = 0
    for f in datos:
        suma += f
    promedio = suma / len(datos)

    # % normales
    normales = 0
    for f in datos:
        if f >= 60 and f <= 100:
            normales += 1

    print("Promedio FC:", round(promedio,1), "bpm")
    print("% normales:", round(normales/len(datos)*100,1), "%")

except:
    print("Error en el análisis de FC.")
"""
    },

    "FC - Medio": {
        "explain":
            "Ordena las frecuencias de mayor a menor.\n"
            "Esto sirve para reportar las más críticas primero.",
        "code": """\
# Ordenar frecuencia cardíaca de mayor a menor

try:
    n = int(input("¿Cuántos valores?: "))

    fc_list = []
    for i in range(n):
        while True:
            try:
                valor = float(input(f"FC {i+1}: "))
                fc_list.append(valor)
                break
            except:
                print("Número inválido, intenta otra vez.")

    # ordenar descendente
    for i in range(len(fc_list)):
        for j in range(i+1, len(fc_list)):
            if fc_list[j] > fc_list[i]:
                aux = fc_list[i]
                fc_list[i] = fc_list[j]
                fc_list[j] = aux

    print("FC ordenadas (mayor a menor):", fc_list)

except:
    print("No se pudieron ordenar las FC.")
"""
    },

    "FC - Complejo": {
        "explain":
            "Incluye sexo y marca alerta si taquicardia.\n"
            "Imprime tipo ficha: Paciente, Sexo, FC, Estado.",
        "code": """\
# Ficha rápida de estado cardíaco

try:
    n = int(input("¿Cuántos pacientes?: "))

    print("PAC\tSEXO\tFC(bpm)\tESTADO")
    print("--------------------------------")

    for i in range(n):
        nombre_sexo = input("Sexo (MASCULINO/FEMENINO): ").upper()

        while True:
            try:
                fc = float(input("FC (bpm): "))
                break
            except:
                print("Ingresa solo números para FC.")

        if fc < 60:
            estado = "Bradicardia"
        elif fc <= 100:
            estado = "Normal"
        else:
            estado = "Taquicardia ⚠"

        print(i+1, "\\t", nombre_sexo, "\\t", fc, "\\t", estado)

except:
    print("Error en la ficha cardíaca.")
"""
    },

    # ========================================================
    # H O M A - I R
    # ========================================================
    "HOMA-IR - Básico": {
        "explain":
            "Calcula HOMA-IR = (glucosa * insulina)/405\n"
            "Te lo preguntan como indicador de resistencia a la insulina.",
        "code": """\
# Cálculo de HOMA-IR individual

try:
    glu = float(input("Glucosa (mg/dL): "))
    ins = float(input("Insulina (µU/mL): "))

    homa = (glu * ins) / 405
    print("HOMA-IR:", round(homa,2))

except:
    print("Error en los datos.")
"""
    },

    "HOMA-IR - Normal": {
        "explain":
            "Clasifica si hay resistencia a la insulina.\n"
            "Corte didáctico: HOMA >= 2.5 => Resistencia.",
        "code": """\
# Detección de resistencia a la insulina con HOMA-IR

try:
    glu = float(input("Glucosa (mg/dL): "))
    ins = float(input("Insulina (µU/mL): "))

    homa = (glu * ins) / 405

    if homa >= 2.5:
        print("HOMA-IR:", round(homa,2), "| Estado: Resistencia")
    else:
        print("HOMA-IR:", round(homa,2), "| Estado: Normal")

except:
    print("Error: use solo números.")
"""
    },

    "HOMA-IR - Medio": {
        "explain":
            "Ingresa muchos pacientes.\n"
            "Cuenta cuántos tienen resistencia.\n"
            "Te da el % con resistencia.",
        "code": """\
# % de pacientes con resistencia insulínica

try:
    n = int(input("¿Cuántos pacientes?: "))

    resistencia = 0

    for i in range(n):
        while True:
            try:
                glu = float(input("Glucosa (mg/dL): "))
                ins = float(input("Insulina (µU/mL): "))
                break
            except:
                print("Dato inválido, inténtalo de nuevo.")

        homa = (glu * ins) / 405
        if homa >= 2.5:
            resistencia += 1

    print("Resistencia insulínica:",
          round(resistencia/n*100,1), "% del grupo")

except:
    print("Error al evaluar el grupo.")
"""
    },

    "HOMA-IR - Complejo": {
        "explain":
            "Clasifica 3 niveles:\n"
            "OK / Riesgo / CRÍTICO (HOMA >=4.0).\n"
            "Esto ya suena ficha clínica endocrino/metabólica.",
        "code": """\
# Screening metabólico avanzado

try:
    n = int(input("Pacientes a evaluar: "))

    print("PAC\tGLU\tINS\tHOMA\tFLAG")
    print("---------------------------------")

    for i in range(n):
        while True:
            try:
                glu = float(input("Glucosa (mg/dL): "))
                ins = float(input("Insulina (µU/mL): "))
                break
            except:
                print("Usa números válidos.")

        homa = (glu * ins) / 405

        if homa >= 4.0:
            flag = "CRITICO"
        elif homa >= 2.5:
            flag = "RIESGO"
        else:
            flag = "OK"

        print(i+1, "\\t", glu, "\\t", ins, "\\t", round(homa,2), "\\t", flag)

except:
    print("Error analizando resistencia.")
"""
    },

    # ========================================================
    # E V A / D O L O R
    # ========================================================
    "EVA - Básico": {
        "explain":
            "Escala de dolor EVA 0-10.\n"
            "Leve <=3 / Moderado 4-6 / Severo >=7.",
        "code": """\
# Clasificación de dolor EVA

try:
    eva = float(input("Dolor (0 a 10): "))

    if eva <= 3:
        print("Dolor leve")
    elif eva <= 6:
        print("Dolor moderado")
    else:
        print("Dolor severo")

except:
    print("Ingresa un número de 0 a 10.")
"""
    },

    "EVA - Normal": {
        "explain":
            "Toma varios pacientes y calcula % con dolor severo.\n"
            "Esto se usa para priorizar analgesia.",
        "code": """\
# % de pacientes con dolor severo

try:
    n = int(input("Cantidad de pacientes: "))
    severos = 0

    for i in range(n):
        while True:
            try:
                eva = float(input("Dolor (0-10): "))
                break
            except:
                print("Ingresa número válido 0-10.")

        if eva >= 7:
            severos += 1

    print("% Dolor severo:", round(severos/n*100,1), "%")

except:
    print("No se pudo evaluar el dolor.")
"""
    },

    "EVA - Medio": {
        "explain":
            "Tabla paciente por paciente con ALERTA para dolor severo.\n"
            "Esto es triage.",
        "code": """\
# Tabla de dolor por paciente con ALERTA

try:
    n = int(input("Pacientes a evaluar: "))

    print("PAC\tEVA\tCLASIF\tFLAG")
    print("---------------------------")

    for i in range(n):
        while True:
            try:
                eva = float(input("Dolor (0-10): "))
                break
            except:
                print("Número inválido.")

        if eva <=3:
            clas="Leve"; flag="OK"
        elif eva <=6:
            clas="Moderado"; flag="OBSERVAR"
        else:
            clas="Severo"; flag="ALERTA"

        print(i+1, "\\t", eva, "\\t", clas, "\\t", flag)

except:
    print("Error procesando EVA.")
"""
    },

    "EVA - Complejo": {
        "explain":
            "Calcula el promedio de dolor general.\n"
            "Esto se usa como 'dolor promedio de sala'.",
        "code": """\
# Dolor promedio en sala

try:
    n = int(input("Pacientes en sala: "))

    suma = 0
    for i in range(n):
        while True:
            try:
                eva = float(input("Dolor (0-10): "))
                suma += eva
                break
            except:
                print("Debe ser número entre 0 y 10.")

    prom = suma / n
    print("Dolor promedio del grupo:", round(prom,1))

except:
    print("No se pudo calcular el promedio de dolor.")
"""
    },

    # ========================================================
    # A D N  /  G E N Ó M I C A
    # ========================================================
    "ADN - Básico": {
        "explain":
            "Cuenta A, C, G, T en una secuencia.\n"
            "Esto cae mucho en genómica básica.",
        "code": """\
# Conteo de nucleótidos

try:
    seq = input("Secuencia ADN: ").strip().upper()

    A = seq.count("A")
    C = seq.count("C")
    G = seq.count("G")
    T = seq.count("T")

    print("A:",A,"C:",C,"G:",G,"T:",T)

except:
    print("Error leyendo la secuencia.")
"""
    },

    "ADN - Normal": {
        "explain":
            "Calcula %GC.\n"
            "%GC = (G+C)/largo *100.\n"
            "Indicador de estabilidad térmica del ADN.",
        "code": """\
# Contenido GC en %

try:
    seq = input("Secuencia ADN: ").strip().upper()
    largo = len(seq)

    if largo == 0:
        print("Secuencia vacía.")
    else:
        gc = (seq.count("G")+seq.count("C")) / largo * 100
        print("GC %:", round(gc,2))

except:
    print("Error al calcular GC%.")
"""
    },

    "ADN - Medio": {
        "explain":
            "Valida si la secuencia es ADN real (solo A,C,G,T).\n"
            "Muy común como pregunta: 'rechazar secuencias inválidas'.",
        "code": """\
# Validación de secuencia ADN

try:
    seq = input("Secuencia ADN: ").strip().upper()

    valida = True
    for base in seq:
        if base not in "ACGT":
            valida = False
            break

    if valida:
        print("Secuencia válida (ADN).")
    else:
        print("ERROR: contiene símbolos que NO son ADN.")

except:
    print("Error al validar la secuencia.")
"""
    },

    "ADN - Complejo": {
        "explain":
            "Compara varias secuencias alineadas\n"
            "y detecta posiciones donde hay mutación.\n"
            "Esto es un clásico 'detectar mutaciones'.",
        "code": """\
# Detección de mutaciones entre múltiples secuencias

try:
    n = int(input("¿Cuántas secuencias vas a ingresar?: "))

    secuencias = []
    for i in range(n):
        s = input(f"Secuencia {i+1}: ").strip().upper()
        secuencias.append(s)

    # Usar el largo mínimo para evitar crash por longitudes distintas
    min_len = len(secuencias[0])
    for s in secuencias:
        if len(s) < min_len:
            min_len = len(s)

    print("\\nMutaciones encontradas (posicion 1-basada):")
    for pos in range(min_len):
        bases = []
        for s in secuencias:
            if s[pos] not in bases:
                bases.append(s[pos])
        if len(bases) > 1:
            print("Posición", pos+1, "->", bases)

except:
    print("Error analizando mutaciones.")
"""
    },

    # ========================================================
    # U C I / G E S T I Ó N   D E   C A M A S   Y   P A C I E N T E S
    # ========================================================
    "UCI - Camas Básico": {
        "explain":
            "Define cuántas camas hay en la UCI.\n"
            "Inicializa todas como vacías.\n"
            "Esta lógica es MUY vista.",
        "code": """\
# Inicializar camas de UCI

try:
    n = int(input("Número TOTAL de camas UCI: "))

    camas_nombre = [""] * n   # nombre paciente en cada cama
    camas_estado = [""] * n   # estado clínico/diagnóstico

    print("Camas inicializadas en blanco.")
    print("Total camas:", n)

except:
    print("Error inicializando UCI.")
"""
    },

    "UCI - Camas Normal": {
        "explain":
            "Permite hospitalizar un paciente en una cama específica.\n"
            "Esto simula 'ingreso a UCI cama X con estado Y'.",
        "code": """\
# Ingreso de paciente a cama UCI específica

try:
    n = int(input("Total camas UCI: "))
    camas_nombre = [""] * n
    camas_estado = [""] * n

    cama = int(input("¿Qué cama vas a usar? (0 a n-1): "))
    if 0 <= cama < n:
        nombre = input("Nombre paciente: ")
        estado = input("Estado (CRITICO / ESTABLE / CUIDADO): ")

        camas_nombre[cama] = nombre
        camas_estado[cama] = estado

        print("Paciente ingresado en cama", cama)
    else:
        print("Cama inválida.")

except:
    print("Error gestionando camas.")
"""
    },

    "UCI - Camas Medio": {
        "explain":
            "Da ALTA a una cama (la limpia/deja vacía).\n"
            "Esto es clásico: 'liberar cama'.",
        "code": """\
# Liberar (dar de alta) una cama UCI

try:
    n = int(input("Total camas UCI: "))

    camas_nombre = ["Paciente A","Paciente B","", "Paciente C"]
    camas_estado = ["CRITICO","ESTABLE","", "CUIDADO"]

    cama = int(input("¿Qué cama liberar? (0 a n-1): "))

    if 0 <= cama < n:
        camas_nombre[cama] = ""
        camas_estado[cama] = ""
        print("Cama", cama, "liberada.")
    else:
        print("Cama inválida.")

    print("\\nEstado actual de la UCI:")
    print("CAMA | NOMBRE           | ESTADO")
    print("-----+------------------+-----------")
    for i in range(n):
        print(i, "   |", camas_nombre[i], " "*(16-len(camas_nombre[i])), "|", camas_estado[i])

except:
    print("Error al liberar cama.")
"""
    },

    "UCI - Camas Complejo": {
        "explain":
            "Genera una tabla completa de la UCI listando cada cama.\n"
            "Formato tipo reporte de turno clínico.",
        "code": """\
# Listar todas las camas UCI en formato tabla

try:
    n = int(input("Total camas UCI: "))

    camas_nombre = []
    camas_estado = []

    for i in range(n):
        nom = input(f"Nombre paciente cama {i} (ENTER si vacía): ").strip()
        est = input(f"Estado cama {i} (CRITICO/ESTABLE/etc): ").strip()
        camas_nombre.append(nom)
        camas_estado.append(est)

    print("\\n===== ESTADO UCI =====")
    print("CAMA | PACIENTE               | ESTADO")
    print("-----+------------------------+-----------------")
    for i in range(n):
        nom = (camas_nombre[i] + " " * 24)[:24]
        est = (camas_estado[i] + " " * 15)[:15]
        print(f"{i:4d} | {nom} | {est}")

except:
    print("Error generando el reporte de UCI.")
"""
    },

    # ========================================================
    # B A S E   D E   D A T O S   D E   P A C I E N T E S
    # (enfermedad asignada a cada uno)
    # ========================================================
    "Base Pacientes - Básico": {
        "explain":
            "Crea listas paralelas con nombre y diagnóstico principal.\n"
            "Muestra todos. Esto ya es mini 'base de datos'.",
        "code": """\
# Mini base de datos de pacientes y diagnóstico

try:
    n = int(input("¿Cuántos pacientes cargarás?: "))

    nombres = []
    dx = []

    for i in range(n):
        nom = input("Nombre paciente: ")
        diag = input("Diagnóstico (ej: Neumonía, IAM, Sepsis): ")
        nombres.append(nom)
        dx.append(diag)

    print("\\nLISTADO DE PACIENTES:")
    for i in range(n):
        print("-", nombres[i], "=>", dx[i])

except:
    print("Error creando la base de pacientes.")
"""
    },

    "Base Pacientes - Normal": {
        "explain":
            "Permite buscar quiénes tienen una enfermedad específica.\n"
            "Ej: 'dame todos los que tienen Sepsis'.",
        "code": """\
# Buscar pacientes por diagnóstico

try:
    n = int(input("¿Cuántos pacientes registrarás?: "))

    nombres = []
    dx = []

    for i in range(n):
        nom = input("Nombre: ")
        diag = input("Diagnóstico: ").upper()
        nombres.append(nom)
        dx.append(diag)

    buscado = input("\\n¿Qué diagnóstico quieres filtrar?: ").upper()

    print("\\nPacientes con", buscado, ":")
    encontrado = False
    for i in range(n):
        if dx[i] == buscado:
            print("-", nombres[i])
            encontrado = True

    if not encontrado:
        print("Nadie con ese diagnóstico.")

except:
    print("Error al filtrar pacientes.")
"""
    },

    "Base Pacientes - Medio": {
        "explain":
            "Cuenta cuántos pacientes hay por diagnóstico.\n"
            "Eso es literalmente un mini censo de sala.",
        "code": """\
# Contar frecuencia de cada diagnóstico

try:
    n = int(input("¿Cuántos pacientes total?: "))

    dx = []

    for i in range(n):
        diag = input("Dx paciente (ej: SEPSIS, IAM): ").upper()
        dx.append(diag)

    # contar diagnósticos: haremos una lista de únicos
    unicos = []
    conteo = []

    for d in dx:
        if d not in unicos:
            unicos.append(d)
            conteo.append(1)
        else:
            idx = unicos.index(d)
            conteo[idx] += 1

    print("\\nRESUMEN DE DIAGNÓSTICOS:")
    for i in range(len(unicos)):
        print(unicos[i], "=>", conteo[i], "pacientes")

except:
    print("Error generando resumen de diagnósticos.")
"""
    },

    "Base Pacientes - Complejo": {
        "explain":
            "Ordena pacientes por prioridad clínica.\n"
            "Tú ingresas gravedad numérica (0=leve ... 10=crítico).\n"
            "Luego los ordena de más grave a menos grave.\n"
            "Esto es EXACTAMENTE estilo triage.",
        "code": """\
# TRIAGE: ordenar pacientes por gravedad reportada

try:
    n = int(input("¿Cuántos pacientes?: "))

    pacientes = []  # lista de tuplas (nombre, gravedad)

    for i in range(n):
        nom = input("Nombre paciente: ")

        while True:
            try:
                grav = float(input("Gravedad 0-10 (10 = crítico): "))
                break
            except:
                print("Ingresa número válido 0-10 por favor.")

        pacientes.append((nom, grav))

    # ordenar por gravedad descendente (crítico primero)
    for i in range(len(pacientes)):
        for j in range(i+1, len(pacientes)):
            if pacientes[j][1] > pacientes[i][1]:
                aux = pacientes[i]
                pacientes[i] = pacientes[j]
                pacientes[j] = aux

    print("\\nLISTA ORDENADA POR GRAVEDAD:")
    for p in pacientes:
        print(p[0], "->", p[1])

except:
    print("Error generando lista de prioridad clínica.")
"""
    },

    # ========================================================
    # H E R R A M I E N T A S   B A S E
    # ========================================================
    "Herramientas Base - Input Seguro": {
        "explain":
            "Plantilla ingreso() con try/except.\n"
            "La usas en todas las pruebas para no romper el programa con inputs malos.\n"
            "PUNTO ALTO EN LA RÚBRICA.",
        "code": """\
# Función universal ingreso() para capturar datos seguros

def ingreso(cartel, tipo="F"):
    while True:
        try:
            if tipo == "F":  # float
                num = float(input(cartel))
            elif tipo == "I":  # int
                num = int(input(cartel))
            else:  # texto libre
                num = input(cartel)
            return num
        except:
            print("❌ Valor inválido, intenta de nuevo.")

# Ejemplo de uso:
edad = ingreso("Edad del paciente: ", "I")
peso = ingreso("Peso (kg): ", "F")
nombre = ingreso("Nombre del paciente: ", "S")

print("Registro ok:", nombre, peso, "kg", edad, "años")
"""
    },

    "Herramientas Base - Bucles": {
        "explain":
            "Ejemplo claro de for y while.\n"
            "for: repetir N veces\n"
            "while: repetir hasta condición.\n"
            "Esto siempre lo preguntan de forma muy directa.",
        "code": """\
# Demostración de for y while

try:
    # FOR: pedir n números y sumar
    n = int(input("¿Cuántos números vas a sumar?: "))

    suma = 0
    for i in range(n):
        while True:
            try:
                x = float(input(f"Número {i+1}: "))
                suma += x
                break
            except:
                print("Ingresa un número válido.")
    print("Suma total =", suma)

    # WHILE: leer valores hasta que el usuario ingrese 0
    print("\\nIngresa valores (0 para terminar):")
    total = 0
    cuenta = 0
    while True:
        try:
            v = float(input("Valor: "))
        except:
            print("Dato inválido.")
            continue

        if v == 0:
            break

        total += v
        cuenta += 1

    if cuenta > 0:
        print("Promedio ingresado:", total/cuenta)
    else:
        print("No se ingresaron valores útiles.")

except:
    print("Error demostrando bucles.")
"""
    },

    "Herramientas Base - Listas Paralelas": {
        "explain":
            "Patrón de listas paralelas (misma posición = mismo paciente).\n"
            "Esto se usa en TODO: nombre[i], edad[i], imc[i] son la misma persona.",
        "code": """\
# Listas paralelas: mismo índice = misma persona

try:
    n = int(input("¿Cuántos pacientes?: "))

    nombres = []
    edades = []
    pesos = []

    for i in range(n):
        nom = input("Nombre: ")

        while True:
            try:
                ed = int(input("Edad: "))
                ps = float(input("Peso (kg): "))
                break
            except:
                print("Edad debe ser entera, peso numérico.")

        nombres.append(nom)
        edades.append(ed)
        pesos.append(ps)

    print("\\nTABLA PACIENTES")
    print("NOMBRE\\tEDAD\\tPESO")
    print("---------------------------")
    for i in range(n):
        print(nombres[i], "\\t", edades[i], "\\t", pesos[i])

except:
    print("Error creando las listas paralelas.")
"""
    },

    "Herramientas Base - Ordenamiento Manual": {
        "explain":
            "Ordenar una lista de menor a mayor SIN usar .sort().\n"
            "Esto te hace ver pro en la prueba.\n"
            "Se usa en triage, IMC, FC, etc.",
        "code": """\
# Ordenamiento ascendente manual (burbuja simple)

try:
    n = int(input("¿Cuántos valores?: "))

    datos = []
    for i in range(n):
        while True:
            try:
                x = float(input("Valor: "))
                datos.append(x)
                break
            except:
                print("Ingresa número válido.")

    # burbuja / intercambio
    for i in range(len(datos)):
        for j in range(i+1, len(datos)):
            if datos[j] < datos[i]:
                aux = datos[i]
                datos[i] = datos[j]
                datos[j] = aux

    print("Orden ascendente:", datos)
    print("Orden descendente:", datos[::-1])

except:
    print("Error ordenando datos.")
"""
    },
}

# ============================================================
# TKINTER APP
# ============================================================

class CodeForgeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CodeForge Biomédico Master Study 🧬")
        self.root.geometry("1300x780")
        self.root.configure(bg="#1a1a1a")

        self.font_title = font.Font(family="Consolas", size=13, weight="bold")
        self.font_btn   = font.Font(family="Consolas", size=10, weight="bold")
        self.font_text  = font.Font(family="Consolas", size=10)
        self.font_code  = font.Font(family="Consolas", size=10)

        self.current_key = None

        # Layout frames
        self.menu_frame = tk.Frame(self.root, bg="#1a1a1a", bd=1, relief="ridge")
        self.menu_frame.place(x=10, y=10, width=320, height=760)

        # contenedor con canvas + scrollbar para menú lateral
        self.menu_canvas = tk.Canvas(
            self.menu_frame,
            bg="#1a1a1a",
            highlightthickness=0,
            bd=0,
        )
        self.menu_canvas.pack(side="left", fill="both", expand=True)

        self.menu_scroll = tk.Scrollbar(
            self.menu_frame,
            orient="vertical",
            command=self.menu_canvas.yview,
        )
        self.menu_scroll.pack(side="right", fill="y")

        self.menu_canvas.configure(yscrollcommand=self.menu_scroll.set)

        self.menu_inner = tk.Frame(self.menu_canvas, bg="#1a1a1a")
        self.menu_window = self.menu_canvas.create_window(
            (0, 0), window=self.menu_inner, anchor="nw"
        )

        self.menu_inner.bind(
            "<Configure>",
            lambda event: self.menu_canvas.configure(
                scrollregion=self.menu_canvas.bbox("all")
            ),
        )

        self.menu_canvas.bind(
            "<Configure>",
            lambda event: self.menu_canvas.itemconfig(
                self.menu_window, width=event.width
            ),
        )

        # soporte para scroll con rueda del mouse
        self.menu_canvas.bind_all("<MouseWheel>", self._on_mousewheel_menu)
        self.menu_canvas.bind_all("<Button-4>", self._on_mousewheel_menu)
        self.menu_canvas.bind_all("<Button-5>", self._on_mousewheel_menu)

        self.right_top = tk.Frame(self.root, bg="#1a1a1a", bd=1, relief="ridge")
        self.right_top.place(x=340, y=10, width=950, height=200)

        self.right_bottom = tk.Frame(self.root, bg="#1a1a1a", bd=1, relief="ridge")
        self.right_bottom.place(x=340, y=220, width=950, height=550)

        # title / copy button in top panel
        self.label_title = tk.Label(
            self.right_top,
            text="Selecciona un código a la izquierda",
            bg="#1a1a1a",
            fg="#00ff99",
            font=self.font_title,
            anchor="w",
            justify="left",
        )
        self.label_title.pack(fill="x", padx=10, pady=10)

        # explanation text (top panel)
        self.exp_scroll = Scrollbar(self.right_top, orient="vertical")
        self.exp_text = Text(
            self.right_top,
            bg="#000000",
            fg="#00ffcc",
            insertbackground="#00ffcc",
            font=self.font_text,
            wrap="word",
            yscrollcommand=self.exp_scroll.set,
            borderwidth=2,
            relief="sunken",
            height=6
        )
        self.exp_scroll.config(command=self.exp_text.yview)
        self.exp_text.pack(side="left", fill="both", expand=True, padx=(10,0), pady=(0,10))
        self.exp_scroll.pack(side="right", fill="y", pady=(0,10))

        # code area + copy button (bottom panel)
        header_frame = tk.Frame(self.right_bottom, bg="#1a1a1a")
        header_frame.pack(fill="x")

        self.code_label = tk.Label(
            header_frame,
            text="Código listo para copiar / entregar",
            bg="#1a1a1a",
            fg="#00ffaa",
            font=self.font_title,
            anchor="w",
        )
        self.code_label.pack(side="left", padx=10, pady=10)

        self.copy_btn = tk.Button(
            header_frame,
            text="⧉ Copiar código",
            command=self.copy_code,
            bg="#2b2b2b",
            fg="#00ffcc",
            activebackground="#333333",
            activeforeground="#00ffaa",
            bd=1,
            relief="ridge",
            font=self.font_btn,
            cursor="hand2",
            padx=10,
            pady=4,
        )
        self.copy_btn.pack(side="right", padx=10, pady=10)

        self.code_scroll = Scrollbar(self.right_bottom, orient="vertical")
        self.code_text = Text(
            self.right_bottom,
            bg="#000000",
            fg="#00ffcc",
            insertbackground="#00ffcc",
            font=self.font_code,
            wrap="none",
            yscrollcommand=self.code_scroll.set,
            borderwidth=2,
            relief="sunken",
        )
        self.code_scroll.config(command=self.code_text.yview)
        self.code_text.pack(side="left", fill="both", expand=True, padx=(10,0), pady=(0,10))
        self.code_scroll.pack(side="right", fill="y", pady=(0,10))

        # fill initial text
        self.exp_text.insert(
            "end",
            "👋 Bienvenido/a a CodeForge Biomédico Master Study.\n\n"
            "1. A la izquierda tienes TODOS los temas simulables en la prueba.\n"
            "2. Cada bloque ya viene con try/except (para que tu programa no reviente si ingresan algo raro).\n"
            "3. 'Básico' es directo tipo 1 paciente.\n"
            "   'Complejo' ya parece informe clínico / ficha UCI / triage.\n"
            "4. Usa el botón ⧉ Copiar código para llevártelo.\n"
        )

        self.build_menu_buttons()

    def _on_mousewheel_menu(self, event):
        x_root = getattr(event, "x_root", None)
        y_root = getattr(event, "y_root", None)

        if x_root is not None and y_root is not None:
            widget = self.root.winfo_containing(x_root, y_root)
        else:
            widget = getattr(event, "widget", None)

        inside_menu = False
        while widget is not None:
            if widget in (self.menu_frame, self.menu_inner, self.menu_canvas):
                inside_menu = True
                break
            widget = getattr(widget, "master", None)

        if not inside_menu:
            return

        if hasattr(event, "delta") and event.delta:
            self.menu_canvas.yview_scroll(int(-event.delta / 120), "units")
        elif getattr(event, "num", None) == 4:
            self.menu_canvas.yview_scroll(-1, "units")
        elif getattr(event, "num", None) == 5:
            self.menu_canvas.yview_scroll(1, "units")

    def build_menu_buttons(self):
        # agrupamos por tema (lo que está antes del " - ")
        # ejemplo: "Glucosa - Básico" -> tema "Glucosa"
        temas = {}
        for key in LESSONS:
            tema = key.split(" - ")[0]
            if tema not in temas:
                temas[tema] = []
            temas[tema].append(key)

        # mostramos TODO visible:
        tk.Label(
            self.menu_inner,
            text="🧬 TEMAS / NIVELES",
            bg="#1a1a1a",
            fg="#00ff99",
            font=self.font_title,
            anchor="w"
        ).pack(fill="x", padx=8, pady=(8,4))

        for tema in sorted(temas.keys()):
            # etiqueta tema
            tk.Label(
                self.menu_inner,
                text=tema.upper(),
                bg="#1a1a1a",
                fg="#00ffcc",
                font=self.font_btn,
                anchor="w"
            ).pack(fill="x", padx=8, pady=(10,2))

            # botones de niveles
            # mantenemos el orden Básico, Normal, Medio, Complejo
            order = ["Básico","Normal","Medio","Complejo"]
            # construir lista ordenada según ese orden
            ordered_keys = []
            for level in order:
                for full_key in temas[tema]:
                    if (" - " + level) in full_key:
                        ordered_keys.append(full_key)

            for full_key in ordered_keys:
                b = tk.Button(
                    self.menu_inner,
                    text=full_key,
                    command=lambda k=full_key: self.show_lesson(k),
                    bg="#2b2b2b",
                    fg="#00ffcc",
                    activebackground="#333333",
                    activeforeground="#00ffaa",
                    bd=1,
                    relief="ridge",
                    font=self.font_text,
                    cursor="hand2",
                    wraplength=260,
                    justify="left",
                    anchor="w",
                    padx=6,
                    pady=4,
                )
                b.pack(fill="x", padx=10, pady=2)

    def show_lesson(self, key):
        self.current_key = key
        lesson = LESSONS[key]

        # título arriba
        self.label_title.config(
            text=f"{key}  |  Estudio y plantilla lista"
        )

        # explicación
        self.exp_text.config(state="normal")
        self.exp_text.delete("1.0", "end")
        self.exp_text.insert("end", lesson["explain"])
        self.exp_text.config(state="disabled")

        # código
        self.code_text.config(state="normal")
        self.code_text.delete("1.0", "end")
        self.code_text.insert("end", lesson["code"])
        self.code_text.config(state="normal")  # editable por ti mismo

    def copy_code(self):
        if self.current_key is None:
            messagebox.showinfo("Copiar", "Primero elige un código en el menú 😺")
            return
        code_str = self.code_text.get("1.0", "end-1c")
        self.root.clipboard_clear()
        self.root.clipboard_append(code_str)
        messagebox.showinfo("Copiado", "Código copiado al portapapeles 😼")


if __name__ == "__main__":
    root = tk.Tk()
    app = CodeForgeApp(root)
    root.mainloop()
