import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:8000",
});

export const indexDocuments = async () => {
  const res = await API.post("/documents/index");
  return res.data;
};

export const sendMessage = async (question) => {
  const res = await API.post("/chat/", { question });
  return res.data;
};