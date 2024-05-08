import app from "./config/server.config.js";
import "./config/db.config.js";
import chalk from "chalk";

const port = 3000;

app.listen(port, () => {
  console.log(chalk.bgCyanBright(`🚀 Server listen on port: ${port}`));
});
