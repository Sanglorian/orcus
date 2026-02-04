from pathlib import Path

INPUT_FILE = Path("Orcus Classes and Powers - current.md")

CLASS_MAP = {
    "At-Will": "Heading-4---At-Will",
    "Encounter": "Heading-4---Encounter",
    "Daily": "Heading-4---Daily",
}

def detect_power_class(line: str) -> str | None:
    s = line.lstrip()
    if not s.startswith(">"):
        return None

    rest = s[1:].lstrip()

    # Only consider lines that start with bold, per your requirement
    if not rest.startswith("**"):
        return None

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

        # Do not overwrite existing HTML headings
        if line.lstrip().lower().startswith("<h4"):
            out.append(line)
            i += 1
            continue

        if line.startswith("> ####"):
            heading_text = extract_heading_text(line)

            # Scan forward to find the first blockquote line that starts with '**'
            j = i + 1
            css_class = None

            while j < len(lines):
                nxt = lines[j]

                # Stop scanning if we hit another heading (any level) in blockquote form
                if nxt.startswith("> #"):
                    break

                # Only decide on the first "> **..." line we encounter
                css_class = detect_power_class(nxt)
                if css_class:
                    out.append(f'<h4 class="{css_class}">{heading_text}</h4>')
                    i += 1  # consume only the heading line; keep the following lines as-is
                    break

                j += 1
            else:
                # fell off end without break
                pass

            # If we converted, we've already appended and advanced i
            if css_class:
                continue

        out.append(line)
        i += 1

    return "\n".join(out)



if __name__ == "__main__":
    original = INPUT_FILE.read_text(encoding="utf-8")
    updated = process_markdown(original)
    INPUT_FILE.write_text(updated, encoding="utf-8")
    print(f"Updated: {INPUT_FILE}")
