![cover](readme/cyberchat.png)

<p align="center">
	<img alt="GitHub" src="https://img.shields.io/github/license/cjyaddone/ChatWaifu?color=red">
	<img src="https://img.shields.io/badge/Python-3.7|8|9|10-green" alt="PYTHON" >
  	<a href="https://app.fossa.com/projects/git%2Bgithub.com%2Fcjyaddone%2FChatWaifu?ref=badge_small" alt="FOSSA Status"><img src="https://app.fossa.com/api/projects/git%2Bgithub.com%2Fcjyaddone%2FChatWaifu.svg?type=small"/></a>
</p>

[original readme](README-original.md)

## 좋은말 봇
배경 설정을 지정해주면 15초 단위로 좋은말을 해줍니다.

## How to run
### Create virtual environment (optional)
```
python -m venv venv
venv\Scripts\activate
```
### Install pytorch
```
pip3 install torch==1.13.1 torchvision==0.14.1 torchaudio==0.13.1 --index-url https://download.pytorch.org/whl/cu117
```
### Install requirements
```
pip3 install -r requirements.txt
```
if error occurs, install visual studio and build tools and try again.

### Install Ren'py
- Download [Ren'py sdk](https://www.renpy.org/latest.html) and add path to environment variable
- Install Live2D library
```
Setting - Install library - Install Live2D Cubism
```

### Place your vits model ./userfile/tts/
such this structure:
```
──┬─userfile/tts/
  ├── config.json
  └── G_128000.pth
```

### Run server
```
python server.py
```

### Run game
```
renpy ./ChatWithGPT/
```
You can get api key [here](https://platform.openai.com/account/api-keys)

## VITS credit
- [MoeGoe_GUI]https://github.com/CjangCjengh/MoeGoe_GUI
- [Pretrained models]https://github.com/CjangCjengh/TTSModels
