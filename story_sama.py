from openai import OpenAI

def gen_story(topic):
    api_key = open(".env", mode= "r").read()
    client = OpenAI(api_key=api_key)
    completion = client.chat.completions.create(
        model = "gpt-4o-mini",
        messages= [
            {"role": "user",
             "content": f"Please generate a funny story on the given topic {topic}, only write the story, nothing else."}
        ]
    )
    story = completion.choices[0].message.content
    return story


#print(gen_story("stinky"))