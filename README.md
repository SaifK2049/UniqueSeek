**UniqueSeek: An intuitive approach to finetuning LLM with plaintext files**

UniqueSeek is an amatuer project which aims to introduce a user friendly appraoch by simply allowing the addition of a txt file to the initial prompt using the deepseek-r1 model. 


**Requirements** 

Please make sure that you have the deepseek model installed within your system using Ollama 

Step 1. **Downloading Ollama**
    https://ollama.com/download  
please follow the Ollama setup instructions in order to have it installed within your system 

Step 2. **Downloading deepseek-r1** 

this Project uses the deepseek-r1:7B model which takes into consideration the RAM and VRAM capabilites of our consumer grade electronics. 

    #in your powershell run the following 

    ollama serve 
    ollama run deepseek-r1
    #to check if your file has been running correctly 
    ollama ps 

    #you should the see the following sample output
    NAME                  ID              SIZE      MODIFIED
    deepseek-r1:latest    0a8c26691023    4.7 GB    5 hours ago

Step 3. **Running docker file**
Go to the project directory; in the terminal run the following command:

    docker build -t deepseek-image -f dockerfile.dockerfile

    docker run deepseek-image
