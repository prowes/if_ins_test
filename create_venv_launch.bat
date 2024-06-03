py -m venv venv
powershell.exe -File  "venv\Scripts\Activate.ps1"
pip3 install -r requirements.txt
pytest --screenshot=on tests/