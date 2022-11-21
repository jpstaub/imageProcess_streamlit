### [Click here for online imageProcess_streamlit webapp](https://jpstaub-imageprocess-streamlit-imageprocess-streamlit-m0xso8.streamlit.app/)

#### Description: This python app processes Velux Daylight Visualizer report images in png or jpg format.

#### Input: Uploaded Velux Daylight Visualizer daylight factor report images.

#### Output: Cropped Velux Daylight Visualizer report images with transparent background for use as underlays.

### [To run imageProcess_streamlit webapp locally](https://docs.streamlit.io/knowledge-base/using-streamlit/how-do-i-run-my-streamlit-script)
    1. Clone repo
	2. Enter correct virtual environment
	3. Open terminal in virtual environment
	4. Navigate to folder containing your_script.py
	5. Run: 'streamlit run your_script.py'
	6. App opens in a new tab on default browser

### Notes:
1. Depends on [streamlit](https://pypi.org/project/xgbxml/)
2. Depends on [opencv](https://test.pypi.org/project/topologicpy/)
3. Depends on [numpy](https://pypi.org/project/numpy/)
4. Depends on [Velux Daylight Visualizer](https://www.velux.com/what-we-do/digital-tools/daylight-visualizer) report images 
5. Processed images can be [used as underlays in design software like Revit](https://www.youtube.com/watch?v=J5ilicWeNCs)

### Functional Development & Test:
    Windows 10 /
    Anaconda / Spyder IDE / Python 3.10 /
    streamlight 1.15.0 /
    opencv-contrib-python-headless 4.6.0.66
