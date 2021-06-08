import yaml
import os
def yml2txt():
    for path in os.listdir("PeaceSheep\chatterbot"):
        if path[-1] == 't':
            continue
        yml_path = os.path.join(os.path.join(os.getcwd() ,"PeaceSheep\chatterbot"),path)
       # os.remove(yml_path)
        f = open(yml_path,'r',encoding='utf-8')

        cont = f.read()

        x = yaml.load(cont)
        file_handle=open(yml_path[:-4]+'.txt',mode='w',encoding='utf-8')
        for conversation in x['conversations']:
            file_handle.write(conversation[0]+'\n')
            file_handle.write(conversation[1]+'\n')
if __name__ == "__main__":
    yml2txt()