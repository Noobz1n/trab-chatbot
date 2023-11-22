import requests 
import json

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def main():
	data = request.get_json(silent=True)
	
	
	intentName = data['queryResult']['intent']['displayName']
def msgNumero():
	data['fulfillmentText'] = f"Não conseguiu solucionar suas dúvidas? fale pessoalmente com a gente +5582999141488"


#intents 
	if intentName == "SistemaTelas": 	
		data['fulfillmentText'] = f"Sim, o sistema é responsivo e roda em qualquer aparelho, seja em desktops, notebooks, tablets, smartphones e iPhones."
		msgNumero()

	elif intentName == "OcupaEspaco":
		data['fulfillmentText'] = f"Não, para acessar o nosso sistema, basta possuir um login e senha e ter um aparelho que se conecte à internet."
		msgNumero()

	elif intentName == "Informacoes":
		data['fulfillmentText'] = f"Não, cada usuário possui seu próprio login e senha. Ninguém consegue alterar o que o professor registra, a não ser o próprio professor, através de seu login e senha."
		msgNumero()

	elif intentName == "Seguranca":
		data['fulfillmentText'] = f"Recomendamos que as senhas sejam alteradas com frequência, por meio do campo apropriado no Sistema, para garantir ainda mais que ninguém terá acesso à sua senha."
		msgNumero()

	elif intentName == "FaltarEnergia":
		data['fulfillmentText'] = f"Trabalhamos com um sistema de armazenamento em nuvem, o que proporciona total segurança no armazenamento de todas as informações."
		msgNumero()

	elif intentName == "EsquecerSenha":
		data['fulfillmentText'] = f"No sistema, existe um campo próprio para recuperar a senha, que oferece total segurança ao identificar o usuário com base nas informações previamente cadastradas no sistema."
		msgNumero()

	elif intentName == "Capacitacao":
		data['fulfillmentText'] = f"""As capacitações ocorrem presencialmente ou virtualmente, quantas vezes forem necessárias para que todos os usuários se sintam seguros ao usar o sistema. Além disso, oferecemos suporte diário de segunda a sexta-feira, durante o horário comercial."""
		msgNumero()

		
	return jsonify(data)

# run flask app
if __name__ == "__main__":
	app.debug = False
	app.run()