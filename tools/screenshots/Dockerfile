# Headless screenshot tool. Playwright exists only in this image, not in pyproject.toml.
FROM mcr.microsoft.com/playwright/python:v1.55.0-noble

# The project needs Python 3.13, the base image ships an older one: use a uv managed venv.
RUN pip install --no-cache-dir uv \
    && uv venv --python 3.13 /opt/venv
ENV PATH="/opt/venv/bin:${PATH}" VIRTUAL_ENV=/opt/venv

WORKDIR /app
COPY pyproject.toml README.md LICENSE ./
COPY src ./src
RUN uv pip install --no-cache . "playwright==1.55.0"

COPY tools/screenshots/take_screenshots.py /app/take_screenshots.py
ENV SCREENSHOT_OUT_DIR=/out
CMD ["python", "/app/take_screenshots.py"]
