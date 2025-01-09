"""
Main module for handwriting synthesis.
Provides functionality to generate handwritten text using different styles and save as SVG files.
"""

from handwriting_synthesis import Hand

# Define your own style, have some variation to look more natural with bias.
style_dict = {
    "bias": 2,
    "style": 5,
    "stroke_width": 1.5,
}

VALID_CHARS = {
    'h','C','T','5',"'",',','n','A','7',' ','G','d','K','H','j','?','0',
    'E','V','q',':','M','1','z','4','e','9','P','u','y','!',';','v','"',
    '8',')','3','J','s','(','O','a','c','2','w','I','R','g','S','.',
    '6','p','m','k','t','l','o','\x00','B','D','L','f','i','r','U','Y',
    'x','b','-','#','W','N','F'
}

def sanitize_line(line):
    """
    Sanitizes the input line by removing unsupported characters.

    Parameters:
    line (str): The input line to be sanitized.

    Returns:
    str: The sanitized line.
    """
    line = (
        line.replace('Q', 'q')
            .replace('Z', 'z')
            .replace('X', 'x')
            .replace("'", "")
            .replace("’", "")
            .replace("“", "")
            .replace("”", "")
            .replace("/", ";")
    )
    for char in line:
        if char not in VALID_CHARS:
            raise ValueError(
                f"Character '{char}' is not supported in handwriting synthesis"
            )
    return line

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
    lines = [sanitize_line(line) for line in lines]
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
    from text_blocks import TEST, STEPS, TRL, MISSION_ARCHITECTURE, COMMON_ALTERNATIVES_MISSION_ELEMENTS, FIRESAT_MISSION_CONCEPT_ELEMENTS, DEFINE_MISSION_CONCEPT, SPACE_ENVIRONMENT
    #write_text(STEPS, style_dict, filename='img/export/steps.svg')
    #write_text(TRL, style_dict, filename='img/export/trl.svg')
    #write_text(MISSION_ARCHITECTURE, style_dict, filename='img/export/mission_architecture.svg')
    #write_text(COMMON_ALTERNATIVES_MISSION_ELEMENTS, style_dict, filename='img/export/common_alternatives_mission_elements.svg')
    #write_text(FIRESAT_MISSION_CONCEPT_ELEMENTS, style_dict, filename='img/export/firesat_mission_concept_elements.svg')
    #write_text(DEFINE_MISSION_CONCEPT, style_dict, filename='img/export/define_mission_concept.svg')
    #write_text(SPACE_ENVIRONMENT, style_dict, filename='img/export/space_environment.svg')
    write_text(TEST, style_dict, filename='img/export/test.svg')