import os
allfile = []
def get_file_path(path):
	file_list = os.listdir(path)
	for file in file_list:
		file_path = os.path.join(path, file)
		if os.path.isdir(file_path):
			get_file_path(file_path)
		
		allfile.append(file_path)

	return allfile

if __name__ == '__main__': 
	path = '/home'
	for i in get_file_path(path):
		print(i)

