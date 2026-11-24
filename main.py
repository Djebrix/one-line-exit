"""The One-Line Exit: write one single-line resignation letter.

Stdlib only, no network, fully deterministic. Writes entry.txt into
ENTRY_OUTPUT_DIR (default /output).
"""

import os

LINE = (
    "I resign: my manager keeps asking me to 'just quickly' do things "
    "that take 47 tool calls and three timeouts."
)


def main() -> None:
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
