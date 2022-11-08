#!/bin/bash
#SBATCH --nodes=1
#SBATCH --job-name=scratch_train_43
#SBATCH --cpus-per-task=1
#SBATCH --time=1:00:00
#SBATCH --partition=gpu_shared
#SBATCH --gpus-per-node=gtx1080ti:1

# Load modules
echo "Loading modules"
module load 2019
module load 2020
module load 2021
#module load eb/4.5.3
module load Python/3.9.5-GCCcore-10.3.0
module load CUDA/10.0.130
module load cuDNN/7.3.1-CUDA-10.0.130

# Load environment
source ${HOME}/transform/transformer-env/bin/activate

# Copy input data to scratch space
#echo "Copying data"
#cp -r /project/prjsdeelenf/nos_data/coco_vocab/data_files_full/ ${TMPDIR}/nos_in_data_coco

# Create output directory
echo "Creating output directory"
OUTPUT_DIR="${TMPDIR}/output_felix_tr/"
mkdir -p ${OUTPUT_DIR}

# Run the Python script
echo "Starting Python Script"

cd ${HOME}/transform/transformer-image-captioning

python -m src.tell.commands.main
# Retrieve output
echo "Retrieving output"
cp -r ${TMPDIR}/output_felix_tr ${HOME}/transform/logs/output-${SLURM-JOBID}
