import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_llm_response(prompt, model="gpt-4o-mini", max_tokens=500):
    """
    Generates a response using the specified LLM model.
    """
    try:
        completion = openai.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are an expert travel assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=max_tokens,
            temperature=0.7,
        )

        response = completion.choices[0].message.content.strip()
        
        if not response:
            return "No plan generated."  # Yanıt boşsa
        return response

    except Exception as e:
        return f"Error generating plan: {str(e)}"  # Hata mesajını döndür
