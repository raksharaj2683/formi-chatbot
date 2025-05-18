from jinja2 import Template
import os

PROMPT_DIR = "prompts"

def load_prompt(state_name, context={}):
    path = os.path.join(PROMPT_DIR, f"{state_name}.txt")
    if not os.path.exists(path):
        return f"Prompt file for '{state_name}' not found."

    with open(path, 'r') as f:
        raw_prompt = f.read()

    # Render the Jinja2 template with the given context
    try:
        template = Template(raw_prompt)
        return template.render(**context)
    except Exception as e:
        return f"Error rendering prompt: {str(e)}"
