import google.generativeai as genai
import PIL.Image

genai.configure(api_key="AIzaSyBJi4xHOMKw1DYvt8r0q4ZD7NuVaP0uL6k")

def analyze_image(image_path):

    img = PIL.Image.open(image_path)


    model = genai.GenerativeModel(model_name="gemini-1.5-flash")

    response = model.generate_content(["O que tem na foto?", img])

    return response.text

if __name__ == "__main__":
    image_path = 'C:\Users\62129532024.1\Documents\GitHub\Aula_pythoney\Pythone\SQL\image.png'  
    analysis_result = analyze_image(image_path)
    print("Resultado da análise:", analysis_result)