FROM python:3.12-slim

# Install TA-Lib dependencies
RUN apt-get update && apt-get install -y \
    wget \
    gcc \
    g++ \
    make \
    && rm -rf /var/lib/apt/lists/*

# Install TA-Lib
RUN wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz && \
    tar -xzf ta-lib-0.4.0-src.tar.gz && \
    cd ta-lib && \
    ./configure --prefix=/usr && \
    make && \
    make install && \
    cd .. && \
    rm -rf ta-lib ta-lib-0.4.0-src.tar.gz

WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Set environment variables
ENV MSD_HOST=82.156.17.205
ENV STOCK_TO_SECTOR_DATA=confs/stock_sector.json

# Expose port
EXPOSE 8000

# Start the server
CMD ["python", "main.py", "--transport=sse", "--port=8000"]