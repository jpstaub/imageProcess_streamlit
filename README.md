### [Click here for online imageProcess_streamlit webapp](https://jpstaub-imageprocess-streamlit-imageprocess-streamlit-m0xso8.streamlit.app/)

    Description: This python script is meant to process Velux Daylight Visualizer report images in png format.


    Input: Velux Daylight Visualizer daylight factor report images. File locations are chosen via a typical directory GUI.


    Output: Cropped Velux Daylight Visualizer report images with transparent background for use as underlays.

### [To run imageProcess_streamlit webapp locally](https://docs.streamlit.io/knowledge-base/using-streamlit/how-do-i-run-my-streamlit-script)
	1. Enter correct virtual environment
	2. Open terminal in virtual environment
	3. Navigate to folder containing your_script.py
	4. Run: 'streamlit run your_script.py'
	5. App opens in a new tab on default browser


Notes:
    1. Depends on [streamlit](https://pypi.org/project/xgbxml/)
    2. Depends on [opencv](https://test.pypi.org/project/topologicpy/)
    3. Depends on [numpy](https://pypi.org/project/numpy/)
    3. Depends on [Velux Daylight Visualizer](https://www.velux.com/what-we-do/digital-tools/daylight-visualizer) report images 
    4. Processed images can be [used as underlays in design software like Revit](https://www.youtube.com/watch?v=J5ilicWeNCs)


Functional Development & Test:
    Windows 10 /
    Anaconda / Spyder IDE / Python 3.10 /
    streamligt 1.15.0 /
    opencv-contrib-python-headless 4.6.0.66
