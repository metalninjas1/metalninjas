import google.generativeai as palm 
from googletrans import Translator

from pyrogram import Client, filters,enums


app = Client("iohdKiohoi", api_id=13016641, api_hash='a8385d296e8b826994bee14b83cf988b',bot_token="6540986992:AAGxkoSGpbtWXDwZXE9REc44dDQ7XxGtOIc")



@app.on_message(filters.command("start"))
def start(client,msg):
   msg.reply("""Bot istədiyiniz suallara cavab almaq üçündür.✅\n
             Şəkil atmayın❌\n
             Sadəcə yazışmaq üçün😍\n
             Developer: @codejavascript""")


@app.on_message(filters.text & filters.private)
def msg(client,msg):
  client.send_chat_action(msg.chat.id, enums.ChatAction.TYPING)
  try:

    translator = Translator()
    translated_text = translator.translate(msg.text, dest='en')

    palm.configure(api_key="AIzaSyCrAvNhZ7uNzotaRAC9GSzkIO8z10yJbo8")

    response = palm.chat(messages=translated_text.text)
    msg.reply( translator.translate(response.last, dest='az').text)
  except:
    msg.reply("Cavab verə bilmədiyim üçün üzgünəm😭")


print("online")
app.run()