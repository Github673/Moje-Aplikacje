require 'shoes'

Shoes.app(title: "Moja aplikacja", width: 400, height: 200) do
  background "#F5F5F5"
  
  stack margin: 10 do
    para "Witaj w mojej aplikacji!"
    button "Kliknij mnie!" do
      alert "Cześć, świat!"
    end
  end
end
