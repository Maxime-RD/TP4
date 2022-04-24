from message import CustomCommands
from log import Logs
from discord.ext.commands import Bot
from discord.ext.commands.context import Context
import argparse
import json


# Classe pour créer le Bot Discord
class My_Bot(Bot):

	def __init__(self, config):
		super().__init__(str(config['prefix']))
		self.remove_command("help")
		self.add_cog(CustomCommands(self))
		self.add_cog(Logs(self, config))

	async def on_ready(self):
		print(f'{self.user} vient de rejoindre le salon.')

def get_args():
	parser = argparse.ArgumentParser()
	parser.add_argument("-c", "--config", help="Config file", required=True, dest="config")
	return parser.parse_args()


def main():
	args = get_args()
	config = json.load(open(args.config))#Cf fichier en .json
	bot = My_Bot(config)
	bot.run(str(config['token']))


if __name__ == "__main__":
	main()