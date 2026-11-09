# Headless screenshot tool. Playwright exists only in this image, not in pyproject.toml.
# Pinned by digest for reproducible builds; the tag it was taken from is v1.55.0-noble.
FROM mcr.microsoft.com/playwright/python:v1.55.0-noble@sha256:640d578aae63cfb632461d1b0aecb01414e4e020864ac3dd45a868dc0eff3078

# The project needs Python 3.13, the base image ships an older one: use a uv managed venv.
# The interpreter is installed under /opt/python so the unprivileged user can read it.
ENV UV_PYTHON_INSTALL_DIR=/opt/python
RUN pip install --no-cache-dir uv \
    && uv venv --python 3.13 /opt/venv \
    && chmod -R a+rX /opt/python
ENV PATH="/opt/venv/bin:${PATH}" VIRTUAL_ENV=/opt/venv

WORKDIR /app
COPY pyproject.toml README.md LICENSE ./
COPY src ./src
RUN uv pip install --no-cache . "playwright==1.55.0"

COPY tools/screenshots/take_screenshots.py /app/take_screenshots.py
ENV SCREENSHOT_OUT_DIR=/home/pwuser/out

# Run as the unprivileged user the Playwright image provides, not as root.
RUN mkdir -p /home/pwuser/out && chown pwuser:pwuser /home/pwuser/out
USER pwuser
CMD ["python", "/app/take_screenshots.py"]
