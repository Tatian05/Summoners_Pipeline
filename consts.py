import os

SUMM_NAME = input("Insert your summoner name...")
TAG_LINE = input("Insert your tag line...")

api_key = os.environ.get("Summoner's_Pipeline")

PARAMS = {
    "api_key" : api_key
}

SERVERS = {
    'AMERICAS': 'americas.api.riotgames.com',
    'ASIA': 'asia.api.riotgames.com',
    'EUROPE': 'europe.api.riotgames.com',   
    'SEA': 'sea.api.riotgames.com'
}

AWS_REGION_NAME = "us-east-1"

JDBC_PATH = "C:\spark\jars\redshift-jdbc42-2.1.0.32"