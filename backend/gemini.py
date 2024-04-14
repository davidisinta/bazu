import google.generativeai as genai
import os

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])


model = genai.GenerativeModel('gemini-1.0-pro-latest')
response = model.generate_content("Why was napoleon defeated in russia?")
print(response.text)