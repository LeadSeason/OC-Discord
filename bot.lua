local internet = require("internet")
local h = internet.open("localhost", 42069)


while true do
    local data = h:read()
    if data ~= nil then
        print(data)
    end
end