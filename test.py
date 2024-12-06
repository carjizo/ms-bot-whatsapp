from rivescript.rivescript import RiveScript

mensaje = "Menu"
bot = RiveScript(utf8=True, debug=False)
bot.load_file(r"database/database.rive")
bot.sort_replies()

response = bot.reply("localuser", mensaje)
response = response.replace("\\n", "\\\n")
response = response.replace("\\", "")

print("Output:\n",response)