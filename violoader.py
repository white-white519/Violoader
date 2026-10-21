path = 'violoader.py'
with open(path, encoding='utf-8') as f:
    content = f.read()

broken = """        except Exception:


def main():"""

fixed = """        except Exception:
            pass


def main():"""

if broken in content:
    content = content.replace(broken, fixed)
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(content)
    print("Fixed OK")
else:
    print("Не нашёл шаблон — правь вручную (см. ниже)")