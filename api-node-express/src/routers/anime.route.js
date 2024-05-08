import { Router } from "express";
import {
  createMasive,
  getAll,
  getById,
} from "../controllers/anime.controller.js";

const routerAnime = Router();

routerAnime.get("/load", createMasive);
routerAnime.get("/", getAll);
routerAnime.get("/:mal_id", getById);
// routerAnime.post("/", createAll)
// routerAnime.put("/:id", update)
// routerAnime.delete("/:id", remove)

export default routerAnime;
