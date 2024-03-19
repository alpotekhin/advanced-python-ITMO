def generate_latex_table(data):
    """
    Generates a LaTeX table from a 2D list (matrix).

    Parameters:
    data (List[List[str]]): A 2D list representing the table data.

    Returns:
    A string containing the LaTeX code for the table.
    """
    header, body = data[0], data[1:]  # Assume the first row is the header and the rest is body

    # Start the table, define alignment for each column
    latex = "\\begin{table}[h!]\n\\centering\n\\begin{tabular}{|" + "l|" * len(header) + "}\n\\hline\n"
    latex += " & ".join(["\\textbf{" + item + "}" for item in data[0]]) + " \\\\\n\\hline\n" # bold header
    
    for row in body:
        latex += " & ".join(row) + " \\\\\n\\hline\n"

    latex += "\\end{tabular}\n\\caption{Your caption here.}\n\\label{table:your_label_here}\n\\end{table}"

    return latex

def generate_latex_figure(image_path, caption="Figure"):
    """
    Generates LaTeX code to include an image.

    Parameters:
    image_path (str): The path to the image file.
    caption (str): The caption for the figure.

    Returns:
    str: A string containing the LaTeX code to include the image.
    """
    latex = f"""\\begin{{figure}}[ht]
\\centering
\\includegraphics[width=0.8\\textwidth]{{{image_path}}}
\\caption{{{caption}}}
\\end{{figure}}
"""
    return latex
