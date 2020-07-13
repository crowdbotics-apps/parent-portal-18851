import {} from "react-native-dotenv"
const parentOnly = axios.create({
  baseURL:
    "https://app.jackrabbitclass.com/jr3.0/ParentPortal/Login?orgID=540191",
  headers: { Accept: "application/json", "Content-Type": "application/json" }
})
export const apiService = {}
