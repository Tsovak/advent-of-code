import os


def read_lines() -> list[str]:
    filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data.txt')
    with open(filename, "rb") as f:
        return [line.decode("utf-8").strip() for line in f.readlines()]


lines = read_lines()
line = lines[0]


def disk_fragmenter(line):
    files = []
    current_pos = 0
    for i in range(0, len(line), 2):
        file_len = int(line[i])
        free_len = int(line[i + 1]) if i + 1 < len(line) else 0
        files.append({
            'id': i // 2,
            'length': file_len,
            'start': current_pos,
            'end': current_pos + file_len
        })
        current_pos += file_len + free_len

    total_length = current_pos
    disk = ['.'] * total_length

    for file in files:
        for j in range(file['length']):
            disk[file['start'] + j] = str(file['id'])

    sorted_files = sorted(files, key=lambda x: x['id'], reverse=True)

    for file in sorted_files:
        # first free space large enough
        free_space_start = -1

        for i in range(total_length):
            if all(disk[j] == '.' for j in range(i, i + file['length'])):
                free_space_start = i
                break

        # move file
        if free_space_start != -1 and free_space_start < file['start']:
            # copy file to new location
            for j in range(file['length']):
                disk[free_space_start + j] = str(file['id'])
                disk[file['start'] + j] = '.'

    return sum(i * int(d) for i, d in enumerate(disk) if d != '.')


result = disk_fragmenter(line)
print(result)
