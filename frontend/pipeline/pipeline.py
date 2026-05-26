from time import sleep
from loguru import logger

logger.add("execution_logs.log", format="{time:YYYY-MM-DD HH:mm:ss.SSS} | {level: <8} | {name}:{function}:{line} - {message}", level="INFO")

def primeira_atividade():
        logger.info("minha primeira atividade")
        sleep(2)

def segunda_atividade():
        logger.info("minha segunda atividade")
        sleep(2)

def terceira_atividade():
        logger.info("minha terceira atividade")
        sleep(2)

def pipeline():
    primeira_atividade()
    segunda_atividade()
    terceira_atividade()
    logger.info("pipeline finalizou")

pipeline()