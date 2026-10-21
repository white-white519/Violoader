import sys
path = 'violoader.py'
with open(path, encoding='utf-8-sig') as f:
    content = f.read()

marker = "\n            def main():"
idx = content.rfind(marker)
if idx == -1:
    print('Не нашёл кривой def main()'); sys.exit(1)

line_start = content.rfind('\n', 0, idx) + 1
new_content = content[:line_start].rstrip() + '''


def main():
    api = Api()
    window = webview.create_window(
        f"violoader v{APP_VERSION}",
        html=HTML,
        js_api=api,
        width=1200, height=800,
        min_size=(900, 600),
        resizable=True,
    )
    api._window = window
    webview.start(debug=False)
    api._shutdown_app()


if __name__ == "__main__":
    main()
'''

with open(path, 'w', encoding='utf-8', newline='\n') as f:
    f.write(new_content)
print('OK')