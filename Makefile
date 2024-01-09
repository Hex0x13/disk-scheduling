
build:
	pyinstaller --noconfirm --onefile --windowed --icon "icon.ico" --add-data ".\icon.ico;." main.py

clean:
	rm -r build dist main.spec