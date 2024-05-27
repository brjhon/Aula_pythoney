import dearpygui.dearpygui as dpg

dpg.create_context()

def calcular_IMC():
    peso = dpg.get_value("peso")
    altura = dpg.get_value("altura")

    try:
        peso = float("peso")
        altura = float ("altura")
        imc = peso / (altura ** 2)

        if imc < float(18) and imc > 0:
            resultado = "Seu peso esta normalizado"
        elif imc > float(18) and imc < float(24.9) :
            resultado = "Seu peso esta normalizado"
        elif imc > float(24.9) and imc < float(29.9) :
            resultado = "Seu peso esta em Sobrepeso"
        elif imc > float(29.9) and imc < float(34.9) :
            resultado = "Sobrepeso grau I"
        elif imc > float(34.9) and imc< float(39.9) :
            resultado = "Sobrepeso grau II"
        elif imc > float(39.9) and imc< float(40) :
            resultado = "Sobrepeso grau III"
        else:
            peso_quantidade = "Erro: Opção incorreta"

        dpg.set_value("resultado", f"Preço final do veículo: R${imc:,.2f}")
    except ValueError:

        dpg.set_value("resultado", "Erro: Por favor, insira valores numéricos válidos")

dpg.create_viewport(title='Calculadora de Preco de IMC', width=700, height=300)

with dpg.window(label="Calculadora IMC", width=600, height=300):
    dpg.add_input_text(label="Altura: ", tag="altura")
    dpg.add_input_text(label="peso: ", tag="peso")
    dpg.add_button(label="Calcular IMC", callback=calcular_IMC)
    dpg.add_text("", tag="resultado")


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()