import numpy as np
from handwriting_synthesis import Hand

all_star = """Somebody once told me the world is gonna roll me
I ain't the sharpest tool in the shed
She was looking kind of dumb with her finger and her thumb
In the shape of an "L" on her forehead"""

downtown = """Making my way downtown
Walking fast
Faces pass
And I'm home-bound"""

give_up = """Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you"""

lines = [
    "Father time, I'm running late",
    "I'm winding down, I'm growing tired",
    "Seconds drift into the night",
    "The clock just ticks till my time expires",
]

def test():
    hand = Hand()

    # usage demo
    biases = [.75 for i in lines]
    styles = [9 for i in lines]
    stroke_colors = ['red', 'green', 'black', 'blue']
    stroke_widths = [1, 2, 1, 2]

    hand.write(
        filename='img/usage_demo.svg',
        lines=lines,
        biases=biases,
        styles=styles,
        stroke_colors=stroke_colors,
        stroke_widths=stroke_widths
    )

    # demo number 1 - fixed bias, fixed style
    lines = all_star.split("\n")
    biases = [.75 for i in lines]
    styles = [12 for i in lines]

    hand.write(
        filename='img/all_star.svg',
        lines=lines,
        biases=biases,
        styles=styles,
    )

    # demo number 2 - fixed bias, varying style
    lines = downtown.split("\n")
    biases = [.75 for i in lines]
    styles = np.cumsum(np.array([len(i) for i in lines]) == 0).astype(int)

    hand.write(
        filename='img/downtown.svg',
        lines=lines,
        biases=biases,
        styles=styles,
    )

    # demo number 3 - varying bias, fixed style
    lines = give_up.split("\n")
    biases = .2 * np.flip(np.cumsum([len(i) == 0 for i in lines]), 0)
    styles = [7 for i in lines]

    hand.write(
        filename='img/give_up.svg',
        lines=lines,
        biases=biases,
        styles=styles,
    )

steps = """Define Objectives and Constraints
1. Define the Broad (qualitative) Objectives and Constraints
2. Define the Principal Players
3. Define the Program Timescale
4. Estimate the quantitative Needs, Requirements, and Constraints
"""

to_olivia = """To Olivia, who is the best
handwriting expert in the world"""

olivia_sonnet = """Olivia, a queen of the pipes and the flow,
She treats all the water, both fast and slow.
With valves that turn and tanks that rumble,
She keeps it clean while the world might stumble.
Her gloves are her armor, her boots like steel,
She battles the sludge with a confident feel.
In tanks full of foam, she dances with grace,
A watery waltz, she owns the space.
With meters that beep and pumps that hum,
She makes sure no waste gets left undone.
No muck is too thick, no gunk too vile,
Olivia makes it clean with style.
So here's to the queen of the liquid world,
Whose waste-water wisdom keeps all swirled!"""

# defining my own style parameters, they are stable, but have some variation to look more natural
style_dict = {
    "bias": 20,
    "style": 11,
    "stroke_width": 1.5,
}

def write_text(text, style_dict=style_dict, filename='output.svg', alignment='left'):
    hand = Hand()
    lines = text.split("\n")
    biases = [style_dict["bias"] for _ in lines]
    styles = [style_dict["style"] for _ in lines]
    stroke_widths = [style_dict["stroke_width"] for _ in lines]
    alignments = [alignment for _ in lines]  # Set alignment for each line
    
    hand.write(
        filename=filename,
        lines=lines,
        biases=biases,
        styles=styles,
        stroke_widths=stroke_widths,
        alignments=alignments  # Pass alignments to the write method
    )




# generate olivias sonnet
if __name__ == "__main__":
    write_text(steps, filename='img/steps.svg')
    #write_text(to_olivia, filename='img/to_olivia.svg')
    #write_text(olivia_sonnet, filename='img/olivia_sonnet.svg')

    # generate olivias sonnet in 13 different styles (0-12)
    #for i in range(13):
    #    style_dict["style"] = i
    #    write_text(olivia_sonnet, style_dict, filename=f'img/olivia_sonnet_{i}.svg')

