# MiBandDataVisualization
This project is about the real extraction of Data from MI Fitness Band using selenium and applying some automization and visualization on real data such as your health monitoring.<br>
`Note: Make sure that while using our web app, you put your business or educational email id which is attached to your MI Fit App on your smartphone.`

# How to run this analysis in your local machine
1. Check your chrome version : `Open chrome > At the top right, look at More > Click Help > About Chrome.`
2. Go to `https://chromedriver.chromium.org/downloads` and download suitable chrome driver according to your chrome version.
3. Move the downloaded driver to `C:\Program Files (x86)`
4. Clone This Project: `git clone https://github.com/yashagg2001/MiBandDataVisualization.git`
5. Go to Project Directory: `cd MIBandDataVisualization`
6. Create a Virtual Environment: `python -m venv miui` (for windows)
7. Activate Virtual Environment: `miui\Scripts\activate.bat` (for windows)
8. Install Requirements Package: `pip install -r requirements.txt`
9. Run: `streamlit run user_interface.py`

To deactivate virtual environment: `deactivate` or `miui\Scripts\deactivate`<br>
To delete virtual environment (simply delete folder `miui`): `rmdir miui /s`
