local shell = require("shell")
 
shell.setWorkingDirectory("/")
 
loadfile("/bin/wget.lua")("-f", "https://raw.githubusercontent.com/LeadSeason/OC-Discord/master/bot.lua", "/home/bot.lua")
loadfile("/home/bot.lua")()