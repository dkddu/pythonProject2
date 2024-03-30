def count_key_lines(file_path):
    key_lines = set()  # 用集合记录关键行，保证不重复

    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        line = line.strip()
        if line:  # 非空行
            key_lines.add(line)

    key_lines_count = len(key_lines)
    return key_lines_count

file_path = "your_file.txt"  # 替换成你的文件路径
result = count_key_lines(file_path)
print("关键行数:", result)
