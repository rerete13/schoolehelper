import g4f as gf


def gpt(message:str):
    response = gf.ChatCompletion.create(
        model=gf.models.gpt_4,
        messages=[{"role": "user", "content": message}]
    )
    print(response)
    return response



gpt('hi')