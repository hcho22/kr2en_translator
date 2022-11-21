# Korean 2 English Translator

![](https://i.imgur.com/ChiSDjr.jpg)

This repository is a Korean to English translator using [Transformer](https://https://proceedings.neurips.cc/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf). 

## Dataset
The Korean 2 English data can be downloaded in the following links:
- [AI Hub](https://www.aihub.or.kr/)

## Model 
The model was created using transfer learning from a model from huggingface. Please refer to acknowledgements for additional reading.  
![](https://i.imgur.com/lqwnbdD.png)


## Architecture 
The following tools were used to setup the MLOPs deployment pipeline:
- Fastapi: Main RestAPI Framework
- Docker: Images and Containers
- Streamlit: Frontend UI

## Test Results
The results from the training model. 

| Model       | Loss       | Val Loss   | Bleu Score |
| --------    | --------   | --------   |------------|
| Transformer | 2.5571     | 2.0146     |2.3711      |



## Acknowledgements
- [Hugging Face Model](https://huggingface.co/Helsinki-NLP/opus-mt-ko-en)

# Kr2En web app installation procedure

### Create new conda environment
Create a new conda environment by running the following command. 

conda create --name myenv python=3.9

(python version 3.9 was used to create the app)

### Clone kr2en repository
Clone the Koren 2 English repository by running the following command.

git clone git@github.com:(your profile)/kr2en_translator.git

![](https://i.imgur.com/5TBEE9d.png)


### To build and run docker containers

docker-compose build

if successful, the following outputs will appear.
![](https://i.imgur.com/mXwbIxU.png)

docker-compose up

if successful, the following output will appear.
![](https://i.imgur.com/S0FpUiF.png)




### Testing via fastapi

User can test the model via fastapi using swaggerUI by visiting http://localhost:8000/docs

![](https://i.imgur.com/xlKtZGf.png)

![](https://i.imgur.com/Hz35np3.png)



### Testing via Streamlit
User can also use the app using Streamlit by visiting http://localhost:8501/

![](https://i.imgur.com/AFghVqj.png)


### Run the app on AWS EC2

After launching the EC2 and git cloning the repo, run the app by typing the following commands from the terminal.

docker-compose build

docker-compose up

Network URL: http://(**your ip address**):8501
External URL: http://(**your ip address**):8501

App will launch on the External URL


### Limitations

Model 
- Currently the model performs slower than expected. Improvements will be performed to enhance the speed of the translation. 
