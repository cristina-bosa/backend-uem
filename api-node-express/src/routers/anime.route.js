import { Router } from "express";
import {
  createMasive,
  getAll,
  getById,
  getAllFavorites,
  removeById,
  addFavorite,
  removeFavorite
} from "../controllers/anime.controller.js";

const routerAnime = Router();

routerAnime.post("/load", createMasive);
routerAnime.get("/", getAll);
routerAnime.get("/favorites", getAllFavorites)
routerAnime.get("/:mal_id", getById);
routerAnime.put("/add-favorite/:mal_id", addFavorite)
routerAnime.put("/delete-favorite/:mal_id", removeFavorite)
routerAnime.delete("/:mal_id", removeById)

export default routerAnime;
