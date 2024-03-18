from texgen_simple.latex_gen import generate_latex_table

# Data example
data = [
    ["Header1", "Header2", "Header3"],
    ["Row1Col1", "Row1Col2", "Row1Col3"],
    ["Row2Col1", "Row2Col2", "Row2Col3"],
    ["Row3Col1", "Row3Col2", "Row3Col3"]
]

latex_code = generate_latex_table(data)

with open("hw_2/artifacts/example_table.tex", "w") as file:
    file.write(latex_code)
