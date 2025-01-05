"""
Main module for handwriting synthesis.
Provides functionality to generate handwritten text using different styles and save as SVG files.
"""

from handwriting_synthesis import Hand

# Define your own style, have some variation to look more natural with bias.
style_dict = {
    "bias": 20,
    "style": 11,
    "stroke_width": 1.5,
}

def write_text(text, style=None, filename='output.svg', alignment='left'):
    """
    Generates handwritten text and saves it as an SVG file.

    Parameters:
    text (str): The text to be written.
    style (dict): Dictionary containing style parameters such as bias, style, and stroke width.
    filename (str): The name of the output SVG file.
    alignment (str): The alignment of the text ('left', 'center', or 'right'). Default is 'left'.
    """
    hand = Hand()
    lines = text.split("\n")
    biases = [style["bias"] for _ in lines]
    styles = [style["style"] for _ in lines]
    stroke_widths = [style["stroke_width"] for _ in lines]
    alignments = [alignment for _ in lines]  # Set alignment for each line

    hand.write(
        filename=filename,
        lines=lines,
        biases=biases,
        styles=styles,
        stroke_widths=stroke_widths,
        alignments=alignments  # Pass alignments to the write method
    )

# Generate images
if __name__ == "__main__":
    from text_blocks import STEPS, TRL
    write_text(STEPS, style_dict, filename='img/export/steps.svg')
    write_text(TRL, style_dict, filename='img/export/trl.svg',)
