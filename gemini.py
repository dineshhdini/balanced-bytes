from pathlib import Path
import textwrap
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown
import langchain

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

MODEL_CONFIG = {
  "temperature": 0.2,
  "top_p": 1,
  "top_k": 32,
  "max_output_tokens": 4096,
}

## Safety Settings of Model
safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  }
]



"""## LOAD GEMINI MODEL WITH MODEL CONFIGURATIONS"""

model = genai.GenerativeModel(model_name = "gemini-pro-vision",
                              generation_config = MODEL_CONFIG,
                              safety_settings = safety_settings)

def image_format(image_path):
    img = Path(image_path)

    if not img.exists():
        raise FileNotFoundError(f"Could not find image: {img}")

    image_parts = [
        {
            "mime_type": "image/png", ## Mime type are PNG - image/png. JPEG - image/jpeg. WEBP - image/webp
            "data": img.read_bytes()
        }
    ]
    return image_parts

def gemini_output(image_path, system_prompt, user_prompt):

    image_info = image_format(image_path)
    input_prompt= [system_prompt, image_info[0], user_prompt]
    response = model.generate_content(input_prompt)
    return response.text


import os
os.getenv('AIzaSyBH44mYvw6rGCTT5bOYEmIi8RcjgrQpxLs')

genai.configure(api_key="AIzaSyBH44mYvw6rGCTT5bOYEmIi8RcjgrQpxLs")

system_prompt = """
               You are a specialist in nutritional facts.
               Input images in the form of wrappers of packaged good will be provided to you,
               and your task is to respond with the text document of all the ingredients present in it give it in a list format.
               take the nutritional facts table part and return how much quantity of the specific nutrients present in that food
               """

image_path = "lays.jpg"

user_prompt = "Give me the information about it"





student_description= gemini_output(image_path, system_prompt, user_prompt)
prompt = f'''


Please extract the following information from the given text and return it is as a JSON object and each heading is a variable  :
note all the ingredients,explain only the complex ingredients in a very very  simple terms .Give side effects of the semi-complex and complex ingredients
give me all the nutritional value and names 


this is the body of text to extract the information from:
{student_description}
'''


model = genai.GenerativeModel('gemini-pro')

responce = model.generate_content(prompt)

to_markdown(responce.text)

print(responce.text)

