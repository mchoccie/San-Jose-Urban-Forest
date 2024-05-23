from preprocessing import dataset_split_feature_cluster


import os
import argparse

parser = argparse.ArgumentParser(prog='Tile Selector')
parser.add_argument('-s', '--source',type=str, required=True, help='source, input tiles folder')
parser.add_argument('-d', '--destination', type=str, required=True, help='Destination, output resampled tiles folder')

args = parser.parse_args()

this_dir =  os.getcwd()
input_folder = args.source
output_folder = args.destination


#
# dataset splitting
#
# train an image which has lower no-data ratio than the give threshold
# (use '0' to train images without any nodata. use '1' to train all possible images)

output_folder_for_selected_data = this_dir + '/' +output_folder + '/output'
output_folder_for_meta = this_dir + '/' + output_folder +'/meta' 
dataset_split_max_nodata_threshold = 0.3
dataset_split_nr_clusters = 2
dataset_split_nr_pca_comp = 3
#the percentage put aside for labeling 0.0 to 1.0
dataset_split_train_proportion = 0.02
dataset_img_meta_path = this_dir + '/' + input_folder +'/meta'  
dataset_img_path_list = this_dir + '/' + input_folder



dataset_split_feature_cluster(output_folder_for_selected_data,
                                  output_folder_for_meta,
                                  dataset_split_nr_clusters,
                                  dataset_split_nr_pca_comp,
                                  dataset_split_train_proportion,
                                  dataset_img_meta_path,
                                  dataset_img_path_list,
                                  dataset_split_max_nodata_threshold)
