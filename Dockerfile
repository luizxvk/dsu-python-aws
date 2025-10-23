FROM python:3.12-slim

WORKDIR /app

# Instala dependências nativas do WeasyPrint
RUN apt-get update && apt-get install -y \
    libcairo2 libcairo2-dev \
    libpango-1.0-0 libpango1.0-dev \
    libgdk-pixbuf-2.0-0 libgdk-pixbuf-2.0-dev \
    libfreetype6 libfreetype6-dev \
    libjpeg-dev \
    libpng-dev \
    libffi-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Copia requirements e instala dependências Python
COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copia o código
COPY . .

CMD ["main.lambda_handler"]
