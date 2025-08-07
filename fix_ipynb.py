def clean_ipynb_conflicts(file_path, output_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    cleaned_lines = []
    skip = False
    for line in lines:
        if line.startswith('<<<<<<<'):
            skip = True
            continue
        elif line.startswith('======='):
            skip = False
            continue
        elif line.startswith('>>>>>>>'):
            continue
        if not skip:
            cleaned_lines.append(line)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.writelines(cleaned_lines)

    print(f"Cleaned file saved to: {output_path}")
clean_ipynb_conflicts('4_multi_linear_reg.ipynb', '4_multiLinearReg.ipynb')