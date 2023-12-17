# MUSE - Famous Painting Image Reconstuctor with Genetic Algorithm (DEAP)  and Painter Identifier with Deep Learning Model (Keras) Program 🧠💻🖌️
MUSE is a program designed with 2 main features, an image reconstructor and a painter identifier. It is designed to assist art enthusiasts and general users in decomposing pictures and reconstruct it step by step and assisting people in identifying the painter behind a famous painting. From identifying the painter behind a painting, users can explore the artist's works for their artstyles, fulfill their curiosity, or just to appreciate them. Moreover, the image reconstructor allows users to see the decomposition to full reconstruction process, done by a genetic algorithm through a natural selection of the fittest generation, which can aid in their art journey. The image reconstructor utilizes the DEAP framework for genetic algorithm while the painter identifier uses a Tensorflow Keras (CNN) based model for the predictions.

## Group Details 🙋🏻‍♀️🙋🏻‍♂️
* Class: L5AC 
* Course: Artificial Intelligence (COMP6065001)
* Members: 
    1. Andrean Hasan - 2501982550
    2. Maria Clarin -2501990331
    3. Raissa Azaria - 2502005805
    4. William Jonathan Mulyadi - 2502045683

## External Links ℹ️
1. [Dataset Source](https://www.kaggle.com/code/paultimothymooney/collections-of-paintings-from-50-artists)
2. [Final Project Report](https://docs.google.com/document/d/1HuUScfZPY4FwAHaa4_YAmZmV_ESywZdEj0sNPvb5beY/edit?usp=sharing)
3. [Video Demo](https://drive.google.com/file/d/1ODouZHuYMgsG8821yfGF8lbg3xq737Zw/view?usp=sharing)

## Repo Directory 🧭
1. GUI.py : main file to run the program
2. requirements.txt : txt file of all dependencies to install
3. backgrounds folder : folder of UI elements
4. identifier folder : folder for identifier file paths and functionalities
    * DownloadModel.py : file to download the model from Google Drive
5. model folder : folder with model training ipynb file
6. reconstructor folder : folder for reconstructor file paths and functionalities



## Installation 👨🏻‍💻
1. Git clone the repository
```
git clone https://github.com/willamjonathan/FamousPainter
```
2. Install dependencies
```
pip install -r requirements.txt
```
3. Run the DownloadModel.py file in the identifier folder
4. Run the GUI.py file to start the program



## Program Manual 🔧
1. Run GUI.py
2. Landing Page
    * Click the Start button to enter the Menu Page
3. Menu Page
    * Click the Reconstruct button to enter the Reconstruct Page
    * Click the Identify Painter button to enter the Identifier Page
4. Reconstruct Page
    *  File Upload:
        1. Click the Upload Painting Image button
        2. Upload an image to reconstruct
        3. Click Start Reconstruction
    * Reconstructor Run:
        1. After every 10 generations (visible from the terminal), click the Refresh Most Recent Generation button.
        2. Click the Stop Reconstruction button to end the process and a Return button will appear to return to the File Upload.
5. Identify Page
    * File Upload:
        1. Click the Upload Painting Image button
        2. Upload an image to identify
        3. Click Start Prediction
    * Identifier Run:
        1. The image uploaded, predicted artist, and prediction score will be displayed.
        2. Click the Finish and Return button to return to the File Upload.


##  User Interface
❗The UI is designed on MacOS and the following screenshots are of Tkinter display on Mac. The display may differ on other OS due to Tkinter's configuration for each. 
</br>
❗Highly recommended to use MacOS is available for the intended UI display and design.


### 1. Landing Page
![landing](https://cdn.discordapp.com/attachments/1178977042331615322/1185688349843931136/image.png?ex=65908553&is=657e1053&hm=16b3ce6e9767b0159202531bfd9ede8fa4ec6a4a1a4e1e6eaab192f12fabe6d4&)
</br>
</br>

### 2. Menu Page
![menu](https://cdn.discordapp.com/attachments/1178977042331615322/1185688389601722499/image.png?ex=6590855d&is=657e105d&hm=e987385a7191b0e2b5e637d5b8e369977c41bb22d4a51aadc844cd707a12a1d0&)
</br>
</br>

### 3. Reconstruct Pages
![recons1](https://cdn.discordapp.com/attachments/1178977042331615322/1185688443326582864/image.png?ex=65908569&is=657e1069&hm=520bb9d568ea885b706f652c2aed5bf78cc30d61a050593652b0350a69039c5f&)
![recons2](https://cdn.discordapp.com/attachments/1178977042331615322/1185688500528496741/image.png?ex=65908577&is=657e1077&hm=23e53414500cf05b561aa7a8a538c31453afa5bf60d49c69b26e48230249b400&)
![recons3](https://cdn.discordapp.com/attachments/1178977042331615322/1185688624721838091/image.png?ex=65908595&is=657e1095&hm=628a11abe8acf6454f396186c323f6bc271658e28f421981bf18053f44d5dcd2&)
</br>
</br>

### 4. Identify Pages
![iden1](https://cdn.discordapp.com/attachments/1178977042331615322/1185688868889043105/image.png?ex=659085cf&is=657e10cf&hm=0e3d6f013474df9eda94a8c6b338fbc9aa52cbd55c40c270e064b74008434fc7&)
![iden2](https://cdn.discordapp.com/attachments/1178977042331615322/1185688972597407764/image.png?ex=659085e8&is=657e10e8&hm=ede7423216364919bac176e09d80d442ec93711672b94cad3cfbc68c37cd0301&)
![iden3](https://cdn.discordapp.com/attachments/1178977042331615322/1185689094320300042/image.png?ex=65908605&is=657e1105&hm=5f84e8dd48548eb8fc482c9dae9cf2f00f9d1df0fe4ebbb00d4784fdab50a9d7&)
</br>
</br>
