import google.generativeai as genai

genai.configure(api_key="gemini_ai_key")

try:
    models = genai.list_models()
    for m in models:
        print(m.name, m.supported_generation_methods)
except Exception as e:
    print("❗API 金鑰錯誤或未啟用:", e)
