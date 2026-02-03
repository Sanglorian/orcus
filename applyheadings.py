from pathlib import Path

INPUT_FILE = Path("Orcus Classes and Powers - current.md")

CLASS_MAP = {
    "At-Will": "Heading-4---At-Will",
    "Encounter": "Heading-4---Encounter",
    "Daily": "Heading-4---Daily",
}

def detect_power_class(next_line: str) -> str | None:
    s = next_line.lstrip()
    if not s.startswith(">"):
        return None

    rest = s[1:].lstrip()

    for key, css_class in CLASS_MAP.items():
        if rest.startswith(f"**{key}**"):
            return css_class

    return None


def extract_heading_text(line: str) -> str:
    text = line.replace("> ####", "", 1).strip()
    return text.rstrip()


def process_markdown(text: str) -> str:
    lines = text.splitlines()
    out = []
    i = 0

    while i < len(lines):
        line = lines[i]

        if line.startswith("> ####"):
            heading_text = extract_heading_text(line)

            if i + 1 < len(lines):
                css_class = detect_power_class(lines[i + 1])
                if css_class:
                    out.append(f'<h4 class="{css_class}">{heading_text}</h4>')
                    i += 1
                    continue

        out.append(line)
        i += 1

    return "\n".join(out)


if __name__ == "__main__":
    original = INPUT_FILE.read_text(encoding="utf-8")
    updated = process_markdown(original)
    INPUT_FILE.write_text(updated, encoding="utf-8")
    print(f"Updated: {INPUT_FILE}")
