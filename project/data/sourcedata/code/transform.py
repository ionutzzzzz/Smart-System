import os
import scipy.io as sio
import numpy as np
from os.path import join

# Path to save the preprocessed data
path = r'F:\WBCIC_SHU Motor Imagery dataset\derivatives\2C dataset_processeddata'
output_dir = r'F:\WBCIC_SHU Motor Imagery dataset\code\shu_data'  # Directory to save the processed data

# Ensure output directory exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Initialize data index
data_index = 1

# Number of participants and sessions
num_participants = 51
num_sessions = 3

# Traverse each participant and their sessions
for sub_id in range(1, num_participants + 1):  # Iterate through 52 participants
    for session_id in range(1, num_sessions + 1):  # Iterate through 3 sessions

        # Create participant and session path
        sub_path = join(path, f"sub-{str(sub_id).zfill(3)}", f"ses-{str(session_id).zfill(2)}", "eeg")

        # Check if the participant session directory exists
        if not os.path.exists(sub_path):
            print(f"Warning: Directory {sub_path} not found, skipping.")
            continue

        file_num_list = os.listdir(sub_path)

        for files in file_num_list:
            file_path = join(sub_path, files)

            # Check if the file is a .mat file
            if files.endswith('.mat'):
                try:
                    # Load data from the .mat file
                    dat = sio.loadmat(file_path)
                    data = dat['data'].transpose(2, 0, 1)  # Transpose as required
                    labels = np.ravel(dat['labels']).astype(int)

                    # Optionally shuffle data and labels (uncomment to enable)
                    # datarand = np.arange(len(labels))
                    # np.random.shuffle(datarand)
                    # data = data[datarand]
                    # labels = labels[datarand]

                    # Save preprocessed data to the output directory
                    output_file = join(output_dir, f'S{str(data_index).zfill(3)}.mat')
                    sio.savemat(output_file, {'data': data, 'labels': labels})

                    print(f"Processed and saved {output_file}")

                    data_index += 1

                except Exception as e:
                    print(f"Error processing file {file_path}: {e}")
            else:
                print(f"Skipping non-MAT file: {file_path}")
