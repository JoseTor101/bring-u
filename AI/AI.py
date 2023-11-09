import sys
sys.path.append("../Lib")
sys.path.append("../pytesseract")

import pytesseract
from pytesseract import Output
import os
import cv2
import numpy as np
import base64
import openai
import json
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv('openAI.env')
openai.api_key  = os.environ['openAI_api_key']

# If you don't have tesseract executable in your PATH, include the following:
#pytesseract.pytesseract.tesseract_cmd = r'<full_path_to_your_tesseract_executable>'
pytesseract.pytesseract.tesseract_cmd = r'AI\Tesseract-OCR\tesseract.exe'
#
#ai_confidence = 50
#confidence_reached_results = []
#path = "AI/media/test.png"
#config = r"--psm 6 --oem 3 -l spa"
##config = r"--psm 6 --oem 3 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.,/()-&"
#
#img = cv2.imread(path)
#height, width, _ = img.shape
#
## VISUALIZATION:
##print(pytesseract.get_languages())
#data = pytesseract.image_to_data(img, config=config, output_type=Output.DICT)
#amount_boxes = len(data['text'])
#for i in range(amount_boxes):
#    if float(data['conf'][i]) > ai_confidence:
#        confidence_reached_results.append(data['text'][i])
#        (x, y, width, height) = (data['left'][i], data['top'][i], data['width'][i], data['height'][i])
#        img = cv2.rectangle(img, (x, y), (x + width, y + height), (0, 255, 0), 2)
#        img = cv2.putText(img, data['text'][i], (x, y+height+10), cv2.FONT_HERSHEY_PLAIN, 0.8, (255, 0, 0), 1, cv2.LINE_AA)
#
##cv2.imshow("img", img)
##cv2.waitKey(0)
## VISUALIZATION ENDED
#
## PRINT RESULTS WITH ENOUGH CONFIDENCE
##print(confidence_reached_results)s
#result = ""
#for word in confidence_reached_results:
#    result += word + " "
#result.strip()
#
#print(result)

def read_image_from_dataUri(image_data):
    ai_confidence = 20
    confidence_reached_results = []
    config = r'--oem 3 --psm 6 -c tessedit_char_whitelist=0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz$'


    # Assuming image_data contains the image data as a base64-encoded string or data URI
    # For example, image_data = "data:image/png;base64,..."

    # Split the data URI to get the image data part (after the comma)
    data_uri_parts = image_data.split(',')

    # Extract the image data (the second part)
    image_data_base64 = data_uri_parts[1]

    # Decode the base64 image data into a binary format
    image_binary = base64.b64decode(image_data_base64)

    # Convert the binary image data into a NumPy array
    image_np = np.frombuffer(image_binary, dtype=np.uint8)

    # Read the image using cv2
    img = cv2.imdecode(image_np, cv2.IMREAD_COLOR)

    #height, width, _ = img.shape
#
    #data = pytesseract.image_to_data(img, config=config, output_type=Output.DICT)
    #amount_boxes = len(data['text'])
    #for i in range(amount_boxes):
    #    if float(data['conf'][i]) > ai_confidence:
    #        confidence_reached_results.append(data['text'][i])
    #        (x, y, width, height) = (data['left'][i], data['top'][i], data['width'][i], data['height'][i])
    #        img = cv2.rectangle(img, (x, y), (x + width, y + height), (0, 255, 0), 2)
    #        img = cv2.putText(img, data['text'][i], (x, y+height+10), cv2.FONT_HERSHEY_PLAIN, 0.8, (255, 0, 0), 1, cv2.LINE_AA)
#
    #cv2.imshow("img", img)
    #cv2.waitKey(0)
    #result = ""
    #for word in confidence_reached_results:
    #    result += word + " "
    #result.strip()

    result = pytesseract.image_to_string(img, config=config)
    print(result)
    print("-------------------------------------------------------------")
    #print(result)

    prompt = "Vas a recibir un texto que otra IA analizo de una imagen. El texto está desordenado y se obtiene de fotos de menus de restaurantes. El texto contiene un nombre, precio y posiblemente una descripcion. asi que necesito que lo comprendas, lo corrijas (Ejemplo: Corregir de 'papxS a la frncesa' a 'papas a la francesa) de ser necesario y lo separes en 3 categorias: Nombre, Precio, Descripcion (Si la hay). El formato que me tienes que devolver debe estar separador con guiones bajos entre las categorias nombre, precio, descripcion (_) y separar con punto y coma (;) los productos entre si, nada mas. Ejemplo: Jugo de Naranja_5000_Delicioso Jugo de la casa;Pastel de yuca en combo_5000_Pastel de yuca hecho a mano y gaseosa de 12oz;Pechuga de la casa_10000_Delicioso pedazo de pechuga con gaseosa de litro y medio."
    extraInstructions = "Instrucciones extra: No me devuelvas nada que no sea el texto arreglado con el formato especificado como por ejemplo tu saludo o algo por el estilo, Tampoco incluyas los titulos del menú (Ejemplo: entradas, plato fuerte, etc), Tampoco incluyas simbolos como los del precio en el resultado (Ejemplo: $, /, ', etc) o simbolos que supongas no se analizaron bien por la otra IA."
    
    fullPrompt = prompt + extraInstructions + "\nTexto a analizar: \n" + result

    print(get_completion(fullPrompt))

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]