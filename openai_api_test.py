from openai import OpenAI
import sys


with open("blog_text.txt", "r") as file:
    text = file.read()

prompt = f"""You are a copy editor at a prestigious British newspaper.
            Please find spelling and grammar errors, subject verb disagreements, and tense errors and provide corrections for the text delimited by ***.
            If there are no corrections to be made, say so. I prefer British English spelling.
            Please only arrange the errors, reasons, and corrections concisely into a markdown table with the changes highlighted in bold.
            Go through each sentence in your head before highlighting errors and think step-by-step.
            
            ***
            {text}
            ***
            
            """
model = "gpt-3.5-turbo"


def format(markdown_text):
    markdown_text = markdown_text.replace("\n", "\r")
    return markdown_text


def error_check():
    try:
        client = OpenAI(api_key=sys.argv[1])
        completion = client.chat.completions.create(
            model=model, messages=[{"role": "user", "content": prompt}]
        )
    except Exception as e:
        return f"An error occurred: {e}"
    return format(completion.choices[0].message.content)


output = error_check()
print(output.replace("\r", "\n\r"))

with open("output.md", "w") as file:
    file.write(output)
