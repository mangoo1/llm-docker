# Running Gemma 7b with GPU

## I'd uploaded my gemma images to docker hug, so you can skip the first two steps to getting permission from hf
### Build the GPU base image:
sudo docker build -t mangoo1/gemma:gpubase . -f docker/Dockerfile.gpubase

### Build the image base on the GPU image
sudo docker build -t mangoo1/gemma:7b . -f docker/Dockerfile.7b

### Get the permission grant and clone the Gemma to the current folder
https://huggingface.co/google/gemma-7b-it

### Run the model with GPU (CUDA)
sudo docker run --gpus all --ipc=host --ulimit memlock=-1 --ulimit stack=67108864 --rm -it -v `pwd`/gemma-7b-it:/app/google/gemma-7b-it  mangoo1/gemma:7b




# Running Gemma 2b with CPU

### Get the permission grant and clone the Gemma to the current folder
https://huggingface.co/google/gemma-2b-it

### Build the CPU image
sudo docker build -t mangoo1/gemma:cpu2b . -f docker/Dockerfile.cpu2b

### Run the model with CPU (Make sure you have 11G memory and be a bit patient)
sudo docker run --rm -it -v `pwd`/gemma-2b-it:/app/google/gemma-2b-it mangoo1/gemma:cpu2b
