from astropy.io import fits
import glob
import os
import shutil


def define_output_dir(input_file_path, data_dir):
	"""Looks at IPPPSSOOT of file name and constructs a file path based on the root
	   directory 'data_dir', the program ID, the visit ID and the filter. Returns a string
	   of the path to the directory it should be sorted into."""

	filts = dict(fits.getval(input_file_path, 'filt*'))
	filt = [filts[key] for key in filts if 'CLEAR' not in filts[key]][0]

	rootname = os.path.basename(input_file_path)[0:9]
	print(rootname)
	progid_obsnum = rootname[1:4] + '_' + rootname[4:6]

	dest_dir = data_dir + '{}/{}/'.format(progid_obsnum, filt)
	print(dest_dir)

	return dest_dir

def make_dirs(dest_dir):
	"""Given a path, makes that directory tree if it doesn't yet exist."""

	if not os.path.isdir(dest_dir):
		print('making directory {}.'.format(dest_dir))
		os.makedirs(dest_dir)

def move_files(input_file_path, dest_dir):
	"""Moves `input_file_path` to `dest_dir'."""

	print('moving {} to {}'.format(input_file_path, dest_dir))
	shutil.move(input_file_path, dest_dir + os.path.basename(input_file_path))

def main_sort_data(input_file_path, data_dir):
	"""Main function to determine destination for `input_file_path` and move to file to the appropriate directory."""

	dest_dir = define_output_dir(input_file_path, data_dir)
	make_dirs(dest_dir)
	move_files(input_file_path, dest_dir)

if __name__ == '__main__':
	# Set global paths here first
	input_dir = '/Users/cshanahan/Desktop/WD_acs/scripts/test_data_dir/' # where input data is. must have trailing slash
	data_dir = '/Users/cshanahan/Desktop/WD_acs/scripts/test_data_dir/' # directory data will be sorted into


	for f in glob.glob(input_dir + '*drc.fits'):
		main_sort_data(f, data_dir)
