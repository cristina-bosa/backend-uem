import mongoose from "mongoose";

const animeSchema = new mongoose.Schema({
  mal_id: Number,
  url: String,
  title: String,
  title_english: String,
  title_japanese: String,
  url_image: String,
  synopsis: String,
  background: String,
  episodes: Number,
  duration: String,
  season: String,
  year: Number,
  favorite: {
    type: Boolean,
    default: false,
  },
});

export default mongoose.model("Anime", animeSchema);
