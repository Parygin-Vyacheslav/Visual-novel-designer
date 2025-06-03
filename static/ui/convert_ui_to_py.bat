for %%F in (.\*.ui) do (
	pyuic6.exe .\%%F -o ..\..\view\%%~nF.py
)