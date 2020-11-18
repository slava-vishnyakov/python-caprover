FROM python:3.8

WORKDIR /app

RUN pip install --upgrade pip
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && apt-get install -y --no-install-recommends --no-install-suggests supervisor

COPY . .

COPY supervisor.conf /etc/supervisor/conf.d/supervisor.conf

RUN groupadd --gid 32767 appuser
RUN useradd --create-home --uid 32767 --gid 32767 --shell /bin/bash appuser
RUN chown -R appuser:appuser /app/

CMD bash -c "test -d /app/storage && chown appuser:appuser /app/storage; /usr/bin/supervisord -c /etc/supervisor/conf.d/supervisor.conf"
