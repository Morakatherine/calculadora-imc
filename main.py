from nicegui import ui

def calculoIMC():
    try:
        peso_num = float(peso.value)
        altura_num = float(altura.value)
        
        if peso_num <= 0 or altura_num <= 0:
            resultado.text = "Ingresa valores mayores a 0"
            mensaje.text = ""
            return

        imc = peso_num / (altura_num ** 2)
        resultado.text = f'Tu IMC es: {imc:.2f}'

        if imc < 18.5:
            mensaje_texto = "Bajo de peso"
        elif imc < 25:
            mensaje_texto = "Peso normal"
        elif imc < 30:
            mensaje_texto = "Sobrepeso"
        else:
            mensaje_texto = "Obesidad"
            
        mensaje.text = mensaje_texto
        
    except:
        resultado.text = "Ingresa números válidos"
        mensaje.text = ""

def limpiar():
    peso.value = ''
    altura.value = ''
    resultado.text = 'Resultado: 0'
    mensaje.text = ''

with ui.column().classes('w-full h-screen items-center justify-center'):
    with ui.card().style('width:400px; background-color:#0B233B;').classes('items-center gap-4'):
        ui.label('INDICE DE MASA CORPORAL').style('color:white; font-size:22px; font-weight:bold')
        ui.icon('monitor_weight', size='80px').props('color=white')
        
        peso = ui.input('Ingresa tu peso en Kg').props('dark outlined').style('width:350px')
        altura = ui.input('Ingresa tu estatura en metros').props('dark outlined').style('width:350px')
        
        with ui.row().classes('w-full justify-center no-wrap').style('gap:16px'):
            ui.button('Calcular', icon='calculate', color='green', on_click=calculoIMC).style('color:white; width:140px')
            ui.button('LIMPIAR', icon='delete', color='red', on_click=limpiar).style('color:white; width:140px')
            
        resultado = ui.label('Resultado: 0').style('color:white; font-size:20px; font-weight:bold')
        mensaje = ui.label('').style('color:#FFEB3B; font-size:18px')

ui.run()