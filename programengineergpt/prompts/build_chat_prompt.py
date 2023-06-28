
def build_user_prompt(question, references):
    context = []
    for document, filename in references:
        context.append(f"From file: {filename} Data: {document}\n")
    prompt = {
        'role': 'user', 
        'content': f"""
Context:
{' '.join(context)}

Assess the following context to answer the users question.

Question:
{question}
"""
    }
    return [prompt]
