-- Załadowanie biblioteki LÖVE
love = require("love")

-- Funkcja wywoływana przy starcie programu
function love.load()
    -- Ustawienie tytułu okna
    love.window.setTitle("Gra")

    -- Załadowanie grafik
    player_img = love.graphics.newImage("player.png")
    enemy_img = love.graphics.newImage("enemy.png")

    -- Inicjalizacja zmiennych
    player_x = 100
    player_y = 100
    enemy_x = 500
    enemy_y = 300
end

-- Funkcja wywoływana co klatkę gry
function love.update(dt)
    -- Poruszanie postacią gracza za pomocą strzałek
    if love.keyboard.isDown("up") then
        player_y = player_y - 200 * dt
    elseif love.keyboard.isDown("down") then
        player_y = player_y + 200 * dt
    end
    if love.keyboard.isDown("left") then
        player_x = player_x - 200 * dt
    elseif love.keyboard.isDown("right") then
        player_x = player_x + 200 * dt
    end

    -- Sprawdzenie kolizji gracza z wrogiem
    if math.abs(player_x - enemy_x) < 50 and math.abs(player_y - enemy_y) < 50 then
        love.event.quit() -- Zakończenie gry w przypadku kolizji
    end
end

-- Funkcja wywoływana przy rysowaniu klatek gry
function love.draw()
    -- Narysowanie postaci gracza i wroga
    love.graphics.draw(player_img, player_x, player_y)
    love.graphics.draw(enemy_img, enemy_x, enemy_y)
end
