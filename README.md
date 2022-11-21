### [imageProcess_streamlit online](https://jpstaub-imageprocess-streamlit-imageprocess-streamlit-m0xso8.streamlit.app/)
Process Velux Dayligth Visualizer images.

Purpose: This python script is meant to process Velux Daylight Visualizer report images in png format.


Inputs:
1. Velux Daylight Visualizer report images. File locations are chosen via a typical directory GUI.


Outputs:
1. Cropped Velux Daylight Visualizer report images with transparent background.

### [Run streamlit app](https://docs.streamlit.io/knowledge-base/using-streamlit/how-do-i-run-my-streamlit-script)
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
