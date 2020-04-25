file = "pick_up_lines2.txt"
with open(file, encoding="utf-8") as fp:
    lines = fp.read().splitlines()
with open("lines.txt", "w", encoding="utf-8",errors='ignore') as fp:
    for line in lines:
        fp.write(line + "<|endoftext|>\n")
