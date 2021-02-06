import random
import re
from pathlib import Path

if __name__ == '__main__':

    compose = Path('docker-compose.yml').read_text()

    postgres_port = random.randint(5433, 6433)
    compose = compose.replace('5525', str(postgres_port))
    compose = compose.replace('5526', str(postgres_port + 1))

    redis_port = random.randint(6380, 7380)
    compose = compose.replace('6913', str(redis_port))
    compose = compose.replace('6914', str(redis_port + 1))

    es_port = random.randint(9301, 10301)
    compose = compose.replace('9483', str(es_port))
    compose = compose.replace('9484', str(es_port + 1))
    print(compose)
    # Path('docker-compose.yml').write_text(compose)

    env = Path('.env.example').read_text()
    env = env.replace('5525', str(postgres_port))
    env = env.replace('6913', str(redis_port))
    print(env)
    # Path('.env.example').write_text(env)

    # if not Path('.env').exists():
    #     Path('.env').write_text(Path('.env.example').read_text())
