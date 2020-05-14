import os,shutil

def demo_main():
	folderPath = './pics'
	croppedFol = './StudentFaces'
	for image in os.listdir(folderPath):
		if os.path.exists(croppedFol):
			shutil.rmtree(croppedFol)
		os.makedirs(croppedFol)
		os.system("python detect.py " + os.path.join(folderPath, image))
		os.system("python spreadsheet.py")
		os.system("python identify.py")
