# Game scripts can be placed in this file.

# Declare the characters used by this game. The color parameter colors the character name.

define e = Character("챗봇")
define y = Character("사용자")
define config.gl2 = True

image hiyori = Live2D("Resources/Hiyori", base=.6, loop = True, fade=True)

init python:
    import socket
    import time
    thinking = 0
    total_data = bytes()
    renpy.block_rollback()
    ip_port = ('127.0.0.1', 9000)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    client.connect(ip_port)


# The game starts here.

label start:
    $ renpy.block_rollback()
    show hiyori m01

    jump chooseTts

label chooseTts:
    $ renpy.block_rollback()
    menu TTSChoice:
        e"TTS 서비스를 선택해주세요"
        "로컬 VITS":
            python:
                client.send(("0").encode())
            jump modelChoice
        "네이버 TTS":
            python:
                client.send(("1").encode())
            jump getApiKey

label modelChoice:
    $ renpy.block_rollback()
    menu KRmodelChoice:
        e "음성 출력할 캐릭터를 선택해주세요"
        "index 0":
            python:
                client.send(("0").encode())
        "index 1":
            python:
                client.send(("1").encode())
        "index 2":
            python:
                client.send(("2").encode())
        "index 3":
            python:
                client.send(("3").encode())
        "index 4":
            python:
                client.send(("4").encode())
        "index 5":
            python:
                client.send(("5").encode())

    jump getApiKey


label getApiKey:
    $ renpy.block_rollback()

    python:
        token = renpy.input("open AI API KEY를 입력해주세요")
        client.send(token.encode())
    
    jump uploadSetting
    return
    

label uploadSetting:
    $ renpy.block_rollback()
    python:
        token = renpy.input("원하는 배경 설정을 입력해주세요",
        default="당신은 사용자와 여자친구 역할을 수행합니다. 당신의 이름은 이초현이고, 주기적으로 안부 인사나 좋은말을 해줘야 합니다. 반말로 말하는 것을 잊지 마세요.")
        client.send(token.encode())
    jump uploadInit

label uploadInit:
    $ renpy.block_rollback()
    python:
        token = renpy.input("해당 캐릭터의 첫 대사를 입력해주세요",
        default="안녕 오늘 하루는 어땠어?")
        client.send(token.encode())
    jump checkRes

label checkRes:
    $ renpy.block_rollback()
    if(thinking == 0):
        show hiyori m03
    e "..."

    python:
        client.setblocking(0)
        try:
                data = client.recv(1024)
                total_data += data
        except:
                data = bytes()
                client.setblocking(1)
    
    if(len(data) > 0 and len(data) < 1024):
        python:
            response = total_data.decode()
            total_data = bytes()
            thinking = 0
        jump answer
    else:
        $ renpy.block_rollback()
        e "......"
        $ thinking = 1
        jump checkRes

        


label answer:
    show hiyori talking
    voice "/audio/test.ogg"
    $ renpy.block_rollback()
    e "[response]"
    voice sustain
    
    $ client.send("음성 재생 완료".encode())
    jump checkRes