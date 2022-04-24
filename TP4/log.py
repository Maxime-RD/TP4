from discord.ext import commands
import logging 

# Logs gérés depuis cette classe
class Logs(commands.Cog):
	#Initialisation
	def __init__(self, bot, config) -> None:
		super().__init__()
		self.bot = bot
		self.setupLog(config)

	# Config
	def setupLog(self, config):
		log_format = str(config['log_format'])
		log_date = str(config['log_date'])
		log_file = str(config['log_file'])
		logging.basicConfig(filename=log_file, encoding='utf-8', format=log_format, level=logging.INFO, datefmt=log_date)


    #Les fonctions suivantes régissent l'affichage dans les logs de toute requêtes (comme des erreurs, les warnings, etc.)
	def debugLog(message):
		logging.debug(message)

	def errorLog(message):
		logging.error(message)

	def infoLog(message):
		logging.info(message)

	def warningLog(message):
		logging.warning(message)

	def criticalLog(message):
		logging.critical(message)