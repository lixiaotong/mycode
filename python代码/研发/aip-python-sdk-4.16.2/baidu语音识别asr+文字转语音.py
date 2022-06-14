# -*- coding: utf-8 -*
from asyncore import file_dispatcher
import subprocess
import sys
import wave
import pyaudio
from aip import AipSpeech # 导入百度aip库

from sphfile import SPHFile
import os

# 需要上传完整语音文件进行识别，时长不超过60s，支持、自定义词库设置， 没有其他额外功能。
# 原始 PCM 的录音参数必须符合 16k 采样率、16bit 位深、单声道，支持的格式有：pcm（不压缩）、wav（不压缩，pcm编码）、amr（压缩格式）。
# 目前系统支持的语音时长上限为60s，请不要超过这个长度，否则会返回错误。 
# """ 你的 APPID AK SK """
APP_ID = '26120277'
API_KEY = 'yepoqyYwXvbXNNKzrsF0gb1B'
SECRET_KEY = 'N24iVNfKnZbSzOODswEuZuZcPn8zMfZk'

#创建识别对象
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

CHUNK = 1024  # 每个缓冲区的帧数
FORMAT = pyaudio.paInt16 # 采样位数
CHANNELS = 1  # 单声道
RATE = 16000  # 采样频率
TEMPAUDIO = 'temp.wav'
OUTAUDIO = 'out.mp3'


def record_audio(wave_out_path, record_second):
    """ 录音功能 """
    p = pyaudio.PyAudio()  # 实例化对象
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)  # 打开流，传入响应参数
    wf = wave.open(wave_out_path, 'wb')  # 打开 wav 文件。
    wf.setnchannels(CHANNELS)  # 声道设置
    wf.setsampwidth(p.get_sample_size(FORMAT))  # 采样位数设置
    wf.setframerate(RATE)  # 采样频率设置

    for _ in range(0, int(RATE * record_second / CHUNK)):
        data = stream.read(CHUNK)
        wf.writeframes(data)  # 写入数据
    stream.stop_stream()  # 关闭流
    stream.close()
    p.terminate()
    wf.close()



class Logger(object):
    def __init__(self, fileN='Default.log'):
        self.terminal = sys.stdout
        self.log = open(fileN, 'a') # a表示直接在后面添加

    def write(self, message):
        '''print实际相当于sys.stdout.write'''
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass

sys.stdout = Logger('./log.txt')  # 调用print时相当于Logger().write()



def play_audio(wave_input_path):
    p = pyaudio.PyAudio()  # 实例化
    wf = wave.open(wave_input_path, 'rb')  # 读 wav 文件
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    data = wf.readframes(CHUNK)  # 读数据
    while len(data) > 0:
        stream.write(data)
        data = wf.readframes(CHUNK)

    stream.stop_stream()  # 关闭资源
    stream.close()
    p.terminate()
    wf.close()


# 将语音转文字
def audio_to_text(file):
    #传递参数： 文件，文件格式，采样频率，PID1537
    #识别的三种格式：wav，pcm，amr
    Format = file[-3:]

    data = open(file,'rb').read()
    result = client.asr(data, Format, 16000, {'dev_pid':1537})
    print(result['result'][0])
    return result['result'][0]

# 将文字转语音
def text_to_audio(text):
    # 1）百度client配置通过 https://ai.baidu.com/ai-doc/SPEECH/Gk4nlz8tc
    # 2）调用合成方法 synthesis（）
    # 参数：文本，语言zh，声道数2，音量，音调，音速，发声人
    # spd 	String 	语速，取值0-9，默认为5中语速 	
    # pit 	String 	音调，取值0-9，默认为5中语调 	
    # vol 	String 	音量，取值0-15，默认为5中音量 	
    # per 	String 	普通发音人选择：度小美=0(默认)，度小宇=1，，度逍遥（基础）=3，度丫丫=4 	
    # per 	String 	精品发音人选择：度逍遥（精品）=5003，度小鹿=5118，度博文=106，度小童=110，度小萌=111，度米朵=103，度小娇=5
    result = client.synthesis(text,'zh',2,{'vol':5,'spd':6,'per':111, 'pit': 6})
    # 3）将合成得到的编码写入文件中
    # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
    if not isinstance(result, dict):
        with open('outaudio.mp3', 'wb') as f:
            f.write(result)
    return 


# print("录音开始")
# record_audio(TEMPAUDIO,5)
# print("录音结束")
# print("识别开始")
# audio_to_text(TEMPAUDIO)
# print("识别结束")
# print("发音开始")
text_to_audio("今天天气去")
# sphfile_trans_to_wave(OUTAUDIO)
ret = subprocess.run('ffmpeg -y -i outaudio.mp3 outaudio.wav',shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,encoding="utf-8",timeout=1)
if ret.returncode == 0:
    # print("success:",ret)
    play_audio('./outaudio.wav')
# else:
    # print("error:",ret)

print("发音结束")




