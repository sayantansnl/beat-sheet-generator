from outline import slow_print, choose_structure, fill_in_the_beats

def export_beats_to_text(story_data):
    title = story_data.get("title", "Untitled")
    structure_name = story_data.get("structure_name", "Unknown Structure")
    beats = story_data.get("beats", {})

    lines = []
    lines.append("=" * 50)
    lines.append(f"STORY BLUEPRINT: {title}")
    lines.append(f"Structure: {structure_name}")
    lines.append("=" * 50)
    lines.append("")

    for i, (beat_name, beat_desc) in enumerate(beats.items(), start=1):
        lines.append(f"Beat {i}: {beat_name}")
        lines.append(f"    {beat_desc}")
        lines.append("-" * 50)

    return "\n".join(lines)

def main():
    structure = choose_structure()
    slow_print(f"\nBased on \"{structure["name"]}\", fill in the following beats: \n")
    blueprint = fill_in_the_beats(structure)
    blueprint_text = export_beats_to_text(blueprint)
    slow_print(blueprint_text)

    with open("story_blueprint.txt", "w") as f:
        f.write(blueprint_text)
    

main()

