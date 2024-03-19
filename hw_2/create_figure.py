from texgen_simple.latex_gen import generate_latex_figure

# Path to your image and the caption for the image
image_path = "image.png"
caption = "An illustrative example image."

# Generate the LaTeX code for the figure
latex_code = generate_latex_figure(image_path, caption)

# Define the path for saving your LaTeX file
file_path = r"hw_2/artifacts/example_figure.tex"

# Wrapping the generated figure LaTeX code in a document structure
full_latex_document = f"""
\\documentclass{{article}}
\\usepackage{{graphicx}}
\\begin{{document}}
{latex_code}
\\end{{document}}
"""

# Save the LaTeX code to a file
with open(file_path, "w") as file:
    file.write(full_latex_document)
