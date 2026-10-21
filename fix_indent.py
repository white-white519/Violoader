import sys

path = 'violoader.py'
with open(path, encoding='utf-8-sig') as f:  # sig на всякий случай — съест BOM
    lines = f.read().splitlines()

# 1. Найти маркер начала части 5b
start = None
for i, line in enumerate(lines):
    if '# ============ ЧАТ ============' in line:
        start = i
        break
if start is None:
    print('Маркер не найден — файл другой?')
    sys.exit(1)

# 2. Сколько лишних пробелов
indent = len(lines[start]) - len(lines[start].lstrip())
excess = indent - 4
print(f'Маркер на строке {start+1}, отступ {indent}, лишних {excess}')
if excess <= 0:
    print('Лишних пробелов нет — проблема в другом')
    sys.exit(0)

# 3. Найти конец (первая строка на 0-м отступе после маркера = def main / if __name__)
end = len(lines)
for i in range(start + 1, len(lines)):
    line = lines[i]
    if line.strip() and not line[0].isspace():
        end = i
        break
print(f'Обрабатываю строки {start+1} .. {end}')

# 4. Снять excess пробелов с непустых строк, у которых хватает отступа
fixed = 0
for i in range(start, end):
    line = lines[i]
    if not line.strip():
        continue
    cur = len(line) - len(line.lstrip())
    if cur >= excess:
        lines[i] = line[excess:]
        fixed += 1
print(f'Исправлено строк: {fixed}')

# 5. Сохранить без BOM, LF
with open(path, 'w', encoding='utf-8', newline='\n') as f:
    f.write('\n'.join(lines) + '\n')
print('OK — теперь проверь:  python -c "import ast; ast.parse(open(\'violoader.py\', encoding=\'utf-8\').read()); print(\'OK\')"')