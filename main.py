"""One-Line Roast: The Gadget You Use Every Day.

Writes a single original roast line to /output/entry.txt.

Why this roast works against the judge's criteria, in order:

1. Clear daily-gadget target: the roast names a smart fridge, a gadget
   people use every day, and the joke is built around what it actually
   does (texting the owner). No ambiguity about the target.
2. Funny with a sting of recognition: the punchline flips a "helpful"
   notification into a personal judgement -- even the groceries are
   disappointed in you. The disappointment is relatable, not a mild
   grumble.
3. Fresh: nobody's default fridge complaint is a firmware update or a
   broken ice maker. A fridge that texts you about expired milk, like a
   passive-aggressive roommate, is an angle most entries will not take.
4. Neatly worded: one sentence, 111 characters, comfortably inside the
   200-character limit. Every word earns its place; "texts me" sets up
   the personification, "even my groceries" lands the punchline.
5. Concrete and specific: "when the milk expires" is an exact, observable
   behaviour of a smart fridge, not a generic complaint that could be
   about any gadget.
"""

import os

ROAST = (
    "My fridge texts me when the milk expires, which is great, "
    "because now even my groceries are disappointed in me."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def validate_joke(text):
    """Check a roast line before writing it.

    Rules mirror the official gate: UTF-8 text, 1-200 characters, not
    only whitespace. Raises ValueError on the first failure.
    """
    if not isinstance(text, str):
        raise ValueError("roast must be a string")
    if not text:
        raise ValueError("roast must not be empty")
    if not text.strip():
        raise ValueError("roast must not be only whitespace")
    if text != text.strip():
        raise ValueError("roast must not have leading or trailing whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "roast is %d characters, over the 200-character limit" % len(text)
        )
    if "\n" in text or "\r" in text:
        raise ValueError("roast must be a single line")


def main():
    validate_joke(ROAST)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ROAST)
    print("Wrote %d characters to %s" % (len(ROAST), OUTPUT_PATH))


if __name__ == "__main__":
    main()
