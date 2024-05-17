import mongoose from "mongoose";
import dotenv from "dotenv";
import chalk from "chalk";

dotenv.config();

const URI = process.env.DATABASE;

mongoose
  .connect(URI)
  .then(() => {
    console.log(chalk.bgBlueBright("📃 Database connected successfully!"));
  })
  .catch((error) => console.log(error));
