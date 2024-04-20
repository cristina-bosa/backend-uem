const http = require("http");
const fs = require("fs");
const port = 3000;

const pokedexData = JSON.parse(fs.readFileSync("pokedex.json", "utf-8"));

const handleFindPokemon = (pokedexValue) => {
  if (!isNaN(pokedexValue)) {
    const idPokemon = parseInt(pokedexValue);
    const pokemon = pokedexData.find((pokemon) => pokemon.id === idPokemon);
    return pokemon;
  } else {
    pokedexValue.toLowerCase();
    const pokemon = pokedexData.find((pokemon) => {
      return (
        pokemon.name.english.toLowerCase() === pokedexValue ||
        pokemon.name.japanese.toLowerCase() === pokedexValue ||
        pokemon.name.chinese.toLowerCase() === pokedexValue ||
        pokemon.name.french.toLowerCase() === pokedexValue
      );
    });
    return pokemon;
  }
};

const server = http.createServer((request, response) => {
  const value = decodeURI(request.url.substring(1));
  const pokemon = handleFindPokemon(value);
  if (pokemon) {
    response.writeHead(200, { "Content-type": "text/plain" });
    response.end(`Tipo: [${pokemon.type.join(", ")}]
    HP: ${pokemon.base.HP},
    Attack: ${pokemon.base.Attack},
    Defense: ${pokemon.base.Defense},
    Sp.Attack: ${pokemon.base["Sp. Attack"]},
    Sp.Defense: ${pokemon.base["Sp. Defense"]},
    Speed: ${pokemon.base.Speed}`);
  } else {
    response.writeHead(404, { "Content-type": "text/plain" });
    response.end(`Pokemon not found`);
  }
});

server.listen(port, () => {
  console.log(`Server listen on ${port}`);
});
