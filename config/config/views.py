from django.http import HttpResponse
from django.shortcuts import render

from openai import OpenAI
import os
import base64
from dotenv import load_dotenv
from .forms import ChatForm




load_dotenv()
api_key = os.getenv("deepseek_apikey")


def index(request):  
    response = None
    response_text = ""
    if request.method == "POST":
        form = ChatForm(request.POST)
        if form.is_valid():
            user_input = request.POST.get("user_input", "")
            dream_category = request.POST.get("dream_category", "freud")
              
            prompts = {
            "freud": "Sen bir bilim insanısın ve rüya yorumlama konusunda uzmansın. Kullanıcının rüyasını analiz et ve bilimsel bir yorum yap.Burada Freud'un Psikanalitik Teorisine dayanarak yapacaksın..",
            "jung": "Sen bir bilim insanısın ve rüya yorumlama konusunda uzmansın. Kullanıcının rüyasını analiz et ve bilimsel bir yorum yap.Burada Jung'un Arketipler ve Kolektif Bilinçaltı Teorisine dayanarak yapacaksın..",
            "aktivasyon":  "Sen bir bilim insanısın ve rüya yorumlama konusunda uzmansın. Kullanıcının rüyasını analiz et ve bilimsel bir yorum yap.Burada Aktivasyon-Sentez Hipotezi Teorisine dayanarak yapacaksın..",
            "bilissel": "Sen bir bilim insanısın ve rüya yorumlama konusunda uzmansın. Kullanıcının rüyasını analiz et ve bilimsel bir yorum yap. Burada Bilişsel Teoriye dayanarak yapacaksın..",
            "tehdit": "Sen bir bilim insanısın ve rüya yorumlama konusunda uzmansın. Kullanıcının rüyasını analiz et ve bilimsel bir yorum yap. Burada Tehdit Simülasyonu Teorisine dayanarak yapacaksın.."
            }

            selected_prompt = prompts.get(dream_category, prompts["freud"])

            client = OpenAI(
                base_url="https://openrouter.ai/api/v1",
                api_key=api_key
                )
            AI_Response = client.chat.completions.create(
                model="deepseek/deepseek-r1-distill-llama-70b:free",
                temperature=0,
                max_tokens=700,
                messages=[
                    {"role": "system", "content": selected_prompt},
                    {"role": "user", "content": user_input},
                ]
            )
            response_text = AI_Response.choices[0].message.content
    else:
        form = ChatForm()
          
    return render(request, "blog.html", {"form": form, "response": response_text})