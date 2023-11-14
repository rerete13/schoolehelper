import g4f as gf


def gpt(message:str, gpt_model):
    response = gf.ChatCompletion.create(
        model=gpt_model,
        messages=[{"role": "user", "content": message}]
    )
    print(response)
    return response



gpt('hi', gpt_model=gf.models.gpt_4)