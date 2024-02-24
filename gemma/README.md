Running Gemma 7b with GPU


Build the GPU base image:
sudo docker build -t mangoo1/gemma:gpubase . -f docker/Dockerfile.gpubase

Build the image base on the GPU image
sudo docker build -t mangoo1/gemma:7b . -f docker/Dockerfile.7b

Get the permission grant and clone the Gemma to the current folder
https://huggingface.co/google/gemma-7b-it

sudo docker run --gpus all --ipc=host --ulimit memlock=-1 --ulimit stack=67108864 --rm -it -v `pwd`/gemma-7b-it:/app/google/gemma-7b-it  mangoo1/gemma:7b
