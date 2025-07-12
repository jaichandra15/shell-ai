# ai_shell/nl_parser.py
import groq  # Official Groq SDK
import os
def prompt_to_command(prompt: str) -> str:
    client = groq.Groq(api_key=os.getenv("GROQ_API_KEY"))

    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",  # or any other Groq-supported model
            messages=[
                {
                    "role": "system",
                    "content": "You are an AI assistant that safely translates natural language instructions into secure Linux shell commands. Never return harmful or destructive commands.only return the command directly executable in a Linux shell without any additional text or explanation."
                },
                {
                    "role": "user",
                    "content": f"Translate this to a safe Linux shell command: {prompt}"
                }
            ],
            temperature=0.2,
            max_tokens=60,
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"Error generating command: {str(e)}"
