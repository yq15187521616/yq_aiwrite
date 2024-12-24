from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
import os

def generate_script(subject,number,genres,creativity,api_key):
    title_template = ChatPromptTemplate.from_messages([("human","请为{subject}这个主题的文章想一个中文标题")])
    script_template = ChatPromptTemplate.from_messages([("human",
             f"""你是一位机关单位的公文写作者。根据以下主题写一篇{genres}格式的文章。
             公文标题：{subject}，公文字数：{number}字，生成的文章的字数尽量遵循字数的要求。
             """)])
    model=ChatOpenAI(base_url='https://xiaoai.plus/v1',api_key="sk-G3lgDLS4deZnzfgYXOGFM9CHYXaODkhezwUDHwhWLhsPvCs8",
                     temperature=creativity)

    title_chain=title_template | model
    script_chain=script_template | model
    title=title_chain.invoke({"subject":subject}).content
    # print(title)

    # 搜索结果
    # search=WikipediaAPIWrapper(lang="zh")
    # search_result=search.run(subject)

    script=script_chain.invoke({"subject":subject,"number":number,"genres":genres}).content
    return title,script


# print(generate_script("考研",1,0.7,os.getenv("OPENAI_API_KEY")))


