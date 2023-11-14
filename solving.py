import g4f as gf


def gpt(message:str, gpt_model, provider):
    response = gf.ChatCompletion.create(
        model=gpt_model,
        provider=provider,
        messages=[{"role": "user", "content": message}]
    )
    print(response)
    return response



