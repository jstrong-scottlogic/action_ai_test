from openai import OpenAI
import sys


with open("blog_text.txt", "r") as file:
    text = file.read()

prompt = f"""You are a copy editor at a prestigious British newspaper.
            Please find spelling and grammar errors, subject verb disagreements, and tense errors and provide corrections for the text delimited by ***.
            If there are no corrections to be made, say so. I prefer British English spelling.
            Please only arrange the errors, reasons, and corrections concisely into a markdown table with the changes highlighted in bold.
            Go through each sentence in your head before highlighting errors and think step-by-step.
            If there are no errors output only: NO_ERRORS_FOUND_SL_BLOG
            
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
        api_key = sys.argv[1]
        client = OpenAI(api_key=sys.argv[1])
        completion = client.chat.completions.create(
            model=model, messages=[{"role": "user", "content": prompt}]
        )
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
    return format(completion.choices[0].message.content)


output = error_check()

if "NO_ERRORS_FOUND_SL_BLOG" in output:
    print("No errors found in the blog.")
    sys.exit(0)

# To print normally
print(output)
sys.exit(1)

# To print in terminal
# print(output.replace("\r", "\n\r"))


# To make file
# with open("output.md", "w") as file:
#     file.write(output)
