import openai
import json

class GPT():
    ''''''''''
    with open('secrets.json') as f:
        file = json.load(f)
        apy_key = file['api_key']
    '''
    with open('api.json')as f:
        file = json.load(f)
        api_key = file['api']
        #print(api)
    #apy_key = "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"
    model = "gpt-3.5-turbo"

    def __init__(self):
        
        openai.api_key = self.api_key
        self.messaggi : list
        try:
            while True:
                user_input = input('\nUtente: ')
                #test = [{'role': 'system', 'content': 'Ciao'}]
                #test.append({'role':'user','content': content_input})
                self.messaggi = [{'role': 'system', 'content': 'Ciao'}]
                self.messaggi.append({'role':'user','content': user_input})
                conversazioni = self.get_risposta(self.messaggi)

                #q = risposta.choices[0].message.content
                print('Chat: '+ conversazioni)
        except KeyboardInterrupt and RuntimeError as m:
            print('Scusa' + m)

    def get_risposta(self,lista_conversazioni:list):
        risposta = openai.ChatCompletion.create(
            model=self.model,
            temperature=2.0,
            messages=lista_conversazioni
        )
        return risposta.choices[0].message.content
