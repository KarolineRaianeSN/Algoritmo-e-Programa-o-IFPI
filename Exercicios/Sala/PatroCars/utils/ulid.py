import random
import time

BASE32_ALPHABET = '0123456789ABCDEFGHJKMNPQRSTVWXYZ'


def converter_timestamp(timestamp_ms):
    """Função para converter um timestamp para ULID (primeira parte)"""
    encoded = ''
    for _ in range(10):  # Precisamos de 10 caracteres para o timestamp em Base32
        encoded = BASE32_ALPHABET[timestamp_ms % 32] + encoded
        timestamp_ms //= 32
    return encoded


def gerar_entropia():
    """Função para gerar a entropia aleatória (segunda parte do ULID)"""
    entropia = ''.join(random.choices(BASE32_ALPHABET, k=16))  # 16 caracteres aleatórios
    return entropia


def gerar_ulid():
    """Função para gerar o ULID completo (com a primeira e segunda parte)"""
    # Pegamos o timestamp atual em milissegundos
    timestamp_ms = int(time.time() * 1000)
    
    # Codificamos o timestamp em Base32 (primeira parte)
    timestamp_part = converter_timestamp(timestamp_ms)
    
    # Geramos a parte de entropia aleatória (segunda parte)
    entropy_part = gerar_entropia()
    
    # Concatenamos as duas partes para formar o ULID completo
    return timestamp_part + entropy_part