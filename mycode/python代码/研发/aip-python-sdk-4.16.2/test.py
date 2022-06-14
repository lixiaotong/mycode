#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from aip import AipSpeech
import subprocess,time,tempfile

import sys
import wave
import pyaudio

class BaiduTTS():

    def __init__(self):

        """ 你的 APPID AK SK """
        self.APP_ID = '26120277'
        self.API_KEY = 'yepoqyYwXvbXNNKzrsF0gb1B'
        self.SECRET_KEY = 'N24iVNfKnZbSzOODswEuZuZcPn8zMfZk'

        self.client = AipSpeech(self.APP_ID, self.API_KEY, self.SECRET_KEY)

    def send_request(self,words):

        result  = self.client.synthesis(words, 'zh', 1, {'vol' : 5, 'per' : 4} )
        
        if not isinstance(result, dict):
            with tempfile.NamedTemporaryFile(suffix='.mp3',delete=False) as f:
                f.write(result)
                self.play_audio(f)
                tmpfile = f.name
                return tmpfile
    
        


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

    
    def say(self,words):

        tmpfile = self.send_request(words)
        #time.sleep(0.5)
        # subprocess.call("play -q %s"%tmpfile,shell=True)
        # self.play_audio(tmpfile)


if __name__=='__main__':

    b = BaiduTTS()
    b.say('我们去打羽毛球吧！')


