#Faça um sistema de conversão de celciús para kelvin e vice e versa.
import dearpygui.dearpygui as dpg

dpg.create_context()

def calcular_Conversão():
    # Obtém os valores inseridos nos campos de texto da interface
    
    Opção = dpg.get_value("Opção") 
    temperatura = dpg.get_value("temperatura") #Variavel usada para o usúario escolher.


    try:
        Opção = int(Opção) #Variavel usada para o usúario escolher.
        temperatura = float(temperatura) #Variavel usada para o usúario escolher.

        if Opção == 1:
            Converter = temperatura + 273.15
            dpg.set_value("resultado", f"Calculo final da conversão: {Converter:,.2f}")
        elif Opção == 2:
            Converter = temperatura - 273.15
            dpg.set_value("resultado", f"Calculo final da conversão: {Converter:,.2f}")
        else:
             dpg.set_value("resultado", "erro Digite o codigo correto: ")

    except ValueError:
        # Define uma mensagem de erro se os valores inseridos não puderem ser convertidos para numéricos
        dpg.set_value("resultado", "Erro: Por favor, insira valores numéricos válidos")

dpg.create_viewport(title='Calculadora de Preco de Veeculos', width=700, height=300)

# Define a janela principal onde os elementos da interface serão colocados
with dpg.window(label="Calculadora FIPE", width=600, height=300):
    dpg.add_input_text(label="Opção", tag="Opção")
    dpg.add_input_text(label="temperatura", tag="temperatura")
    dpg.add_button(label="Calcular Conversão", callback=calcular_Conversão)
    dpg.add_text("", tag="resultado")

# Configura e mostra a janela
dpg.setup_dearpygui()
dpg.show_viewport()
# Inicia o loop de eventos da interface, onde a aplicação efetivamente roda e espera por interações do usuário
dpg.start_dearpygui()
# Destroi o contexto da aplicação após o fechamento da janela, liberando recursos
dpg.destroy_context()
