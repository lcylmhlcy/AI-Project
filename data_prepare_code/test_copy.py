import os

path_dir = 'C:\\Users\\ssss\\Documents\\2019-6-11\\04\\copy'
# save_dir = 'C:\\Users\\ssss\\Documents\\data_use\\01\\mhqbabnormal1'

for filename in os.listdir(path_dir):
	basename, ext = filename.split('.')
	new_name = basename + '_copy.' + ext
	os.rename(os.path.join(path_dir, filename), os.path.join(path_dir, new_name)) 
