import express from "express";
import animeRouter from "../routers/anime.route.js";
import bodyParser from "body-parser";
import cors from "cors";

const app = express();

app.use(cors());
app.use(express.json());

app.use(bodyParser.urlencoded({ extended: true }));
app.use("/api/anime", animeRouter);

export default app;
