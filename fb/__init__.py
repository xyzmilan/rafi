from .__paysort import *
from .__myhead import *
from .__friend import *
from .__userAgent import *
from .__cook import *

import requests
import random
import sys
import re
from concurrent.futures import ThreadPoolExecutor as executor
from bs4 import BeautifulSoup as parser
import colorama
from colorama import Fore,Style

colorama.init(True)

logo = f"""

                                                 
    
┏━┓┏━┳━━┳┓╋╋┏━━━┳━┓╋┏┓
┃┃┗┛┃┣┫┣┫┃╋╋┃┏━┓┃┃┗┓┃┃ Facebook: {Fore.GREEN}https://facebook.com/isthislovedaddy {Fore.RESET}
┃┏┓┏┓┃┃┃┃┃╋╋┃┃╋┃┃┏┓┗┛┃ GitHub      : {Fore.GREEN}https://github.com/milan-says{Fore.RESET
┃┃┃┃┃┃┃┃┃┃╋┏┫┗━┛┃┃┗┓┃┃
┃┃┃┃┃┣┫┣┫┗━┛┃┏━┓┃┃╋┃┃┃
┗┛┗┛┗┻━━┻━━━┻┛╋┗┻┛╋┗━┛
                                                 
"""
