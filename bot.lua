local internet = require("internet")
local h = internet.open("127.0.0.1", 42069)


while true do
    local data = h:read()
    if data ~= nil then
        print(data)
    end
end