# Use a base image with Python and pip installed
FROM python:3.8-slim

# Install LaTeX
RUN apt-get update && \
    apt-get install -y --no-install-recommends texlive-latex-base texlive-fonts-recommended texlive-fonts-extra texlive-latex-extra && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Adjusted COPY paths based on your project structure
COPY hw_2/create_figure.py /app/create_figure.py
COPY hw_2/artifacts/image.png /app/image.png

# Ensure the artifacts directory exists
RUN mkdir -p /app/hw_2/artifacts

# Install your Python package
RUN pip install -i https://test.pypi.org/simple/ texgen-simple

# Generate the .tex file
RUN python create_figure.py

# Then, attempt to compile the .tex file to PDF
RUN pdflatex -output-directory=/app/hw_2/artifacts /app/hw_2/artifacts/example_figure.tex

# Example command, adjust as needed
CMD ["echo", "PDF generation complete. Please copy out the PDF from the container."]