import os

SUMM_NAME = "TATIAN"
TAG_LINE = "LAS"

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

JDBC_PATH = "C:\spark-3.5.3-bin-hadoop3\jars\redshift-jdbc42-2.1.0.31"