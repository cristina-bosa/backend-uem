import app from "./config/server.config.js";
import "./config/db.config.js";
import chalk from "chalk";
import dotenv from "dotenv";

dotenv.config();

const PORT = process.env.PORT;

app.listen(PORT, () => {
  console.log(chalk.bgCyanBright(`🚀 Server listen on port: ${PORT}`));
});
