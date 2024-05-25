import dearpygui.dearpygui as dpg

dpg.create_context()

def calcular_IMC():
    peso = dpg.get_value("peso")
    altura = dpg.get_value("altura")

    try:
        imc = peso / (altura * 2)

        if imc < float(18) and imc > 0:
            resultado = "Seu peso está abaixo do normal"
        elif imc > float(18) and imc < float(24.9):
            resultado = "Seu peso está normal"
        elif imc > float(24.9) and imc < float(29.9):
            resultado = "Sobrepeso"
        elif imc > float(29.9) and imc < float(34.9):
            resultado = "Obesidade Grau I"
        elif imc > float(34.9) and imc < float(39.9):
            resultado = "Obesidade Grau II"
        elif imc > float(39.9) and imc < float(40):
            resultado = "Obesidade Grau III"
        else:
            resultado = "Erro: Opção incorreta"  # Correção: Alterado o nome da variável

        dpg.set_value("resultado", f"Seu IMC é: {imc:.2f} - {resultado}")  # Correção: Exibe o IMC e a categoria correspondente
    except ValueError:
        dpg.set_value("resultado", "Erro: Por favor, insira valores numéricos válidos")

dpg.create_viewport(title='Calculadora de IMC', width=700, height=300)

with dpg.window(label="Calculadora IMC", width=600, height=300):
    dpg.add_input_text(label="Altura: ", tag="altura")
    dpg.add_input_text(label="Peso: ", tag="peso")
    dpg.add_button(label="Calcular IMC", callback=calcular_IMC)
    dpg.add_text("", tag="resultado")

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()