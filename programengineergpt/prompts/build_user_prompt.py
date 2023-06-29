#!/usr/bin/env python3


def build_user_prompt(question, references):
    context = "\n".join([f"From file: {ref[0]} Data: {ref[1]}" for ref in references])
    return {
        "role": "user",
        "content": f"""Context:\n{context}\n\nAssess the following context to answer the users question.\n\nQuestion:\n{question}""",
    }
