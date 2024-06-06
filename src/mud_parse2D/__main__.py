import textwrap
from parse_2d import Diagram
from parse_2d.tokens import BoxTokenizer, Directions

def main():
    box = textwrap.dedent("""\
        ┌──┐
        │ab│
        │cd│
        └──┘
    """)
    print('Text to parse:')
    print(box)
    diagram = Diagram.from_string(box)
    box_tokenizer = BoxTokenizer(
        {
            Directions.UP: frozenset({"─"}),
            Directions.UP_RIGHT: frozenset({"┐"}),
            Directions.RIGHT: frozenset({"│"}),
            Directions.DOWN_RIGHT: frozenset({"┘"}),
            Directions.DOWN: frozenset({"─"}),
            Directions.DOWN_LEFT: frozenset({"└"}),
            Directions.LEFT: frozenset({"│"}),
            Directions.UP_LEFT: frozenset({"┌"}),
        },
        lambda diagram: "\n".join(
            "".join(line[1:-1]) for line in diagram.contents[1:-1]
        )
    )
    token = box_tokenizer.extract_token(diagram, (0, 0))
    print(f"Extracted token: {token}")
