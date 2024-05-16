import axios from "axios";
import chalk from "chalk";
import dotenv from "dotenv";
import Anime from "../models/anime.model.js";

dotenv.config();

const URI = process.env.API_ANIME;

export const createMasive = async (req, res) => {
  try {
    const response = await axios.get(URI);
    const animeData = response.data.data;

    for (const anime of animeData) {
      const newAnime = new Anime({
        mal_id: anime.mal_id,
        url: anime.url,
        title: anime.title,
        title_english: anime.title_english,
        title_japanese: anime.title_japanese,
        url_image: anime.images.jpg.image_url,
        synopsis: anime.synopsis,
        background: anime.background,
        episodes: anime.episodes,
        duration: anime.duration,
        season: anime.season,
        year: anime.year,
        favorite: false,
      });
      await newAnime.save();
    }

    console.log(chalk.green("🌟 Data fetched successfully!"));
    return res.status(200).json({
      message: "Data saved successfully!",
    });
  } catch (error) {
    console.log(chalk.red("❌ Error fetching data!"), error);
    return res.status(500).json({
      message: "Error fetching data!",
    });
  }
};

export const getAll = async (req, res) => {
  try {
    const animes = await Anime.find().exec();
    if (animes.length > 0) {
      return res.status(200).json(animes);
    } else {
      return res.status(204).json({
        message: "Data not found!",
      });
    }
  } catch (error) {
    console.log(chalk.red("❌ Error fetching data!"), error);
    return res.status(500).json({
      message: "Error fetching data!",
    });
  }
};

export const getById = async (req, res) => {
  try {
    const { mal_id } = req.params;

    const anime = await Anime.find({ mal_id: mal_id }).exec();

    if (anime !== null) {
      return res.status(200).json(anime);
    } else {
      return res.status(204).json({
        message: "Data not found!",
      });
    }
  } catch (error) {
    console.log(chalk.red("❌ Error fetching data!"), error);
    res.status(500).json({
      message: "Error fetching data!",
    });
  }
};

export const addFavorite = async (req, res) => {
  try {
    const { mal_id } = req.params;

    const anime = await Anime.findOneAndUpdate(
      { mal_id: mal_id },
      { favorite: true }
    ).exec();
    return res.status(200).json({
      data: anime,
      message: "Data updated successfully",
    });
  } catch (error) {
    console.log(chalk.red("❌ Error updating data"), error);
    return res.status(500).json({
      message: "Error updating data",
    });
  }
};

export const removeFavorite = async (req, res) => {
  try {
    const { mal_id } = req.params;

    const anime = await Anime.findOneAndUpdate(
      { mal_id: mal_id },
      { favorite: false }
    ).exec();

    return res.status(200).json({
      data: anime,
      message: "Data updated successfully",
    });
  } catch (error) {
    console.log(chalk.red("❌ Error updating data"), error);
    return res.status(500).json({
      message: "Error updating data",
    });
  }
};

export const getAllFavorites = async (req, res) => {
  try {
    const animes = await Anime.find({ favorite: true }).exec();
    if (animes.length > 0) {
      return res.status(200).json(animes);
    } else {
      return res.status(204).json({
        message: "Data not found",
      });
    }
  } catch (error) {
    console.log(chalk.red("❌ Error fetching data"), error);
    return res.status(500).json({
      message: "Error fetching data",
    });
  }
};

export const removeById = async (req, res) => {
  try {
    const { mal_id } = req.params;
    const isDeleted = await Anime.deleteOne({ mal_id: mal_id }).exec();
    if (isDeleted.deletedCount > 0) {
      return res.status(200).json({
        message: "Data removed successfully",
      });
    } else {
      return res.status(204).json({
        message: "Data not found",
      });
    }
  } catch (error) {
    console.log(chalk.red("❌ Error removing data"), error);
    return res.status(500).json({
      message: "Error removing data",
    });
  }
};
