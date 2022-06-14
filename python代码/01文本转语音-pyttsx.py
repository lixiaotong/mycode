# 语音播报模块
import pyttsx3

# 模块初始化
engine = pyttsx3.init()
print('准备开始语音播报...')

# 设置发音速率，默认值为200
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 50)
# 设置发音大小，范围为0.0-1.0
volume = engine.getProperty('volume')
engine.setProperty('volume', 0.6)
# 设置默认的声音：voices[0].id代表男生，voices[1].id代表女生
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id)
# 普通话发音
# voices = engine.setProperty('voice', "com.apple.speech.synthesis.voice.ting-ting.premium")
# 标准的粤语发音
# voices = engine.setProperty('voice', "com.apple.speech.synthesis.voice.sin-ji")
# 台湾甜美女生普通话发音
voices = engine.setProperty('voice', "com.apple.speech.synthesis.voice.mei-jia")
# 添加朗读文本
engine.say('测试测试')

# 等待语音播报完毕
engine.runAndWait()



# 还可以尝试PocketSphinx
# 还可以尝试讯飞

