import axios from "axios";

const api = axios.create({
    baseURL: "http://127.0.0.1:8000",
});

export async function uploadDataset(file){
    const formData = new FormData(); // FormData = package the data 
    formData.append("file", file); // syntax -> formData.append(fieldName, value);
    const response = await api.post("/upload", formData);
    return response.data;
}
export function downloadDataset(filename) {
    window.open(`http://127.0.0.1:8000/download/${filename}`); //directly download the file in browser 
}

export function downloadReport(filename) {
    window.open(`http://127.0.0.1:8000/download-report/${filename}`);
  }