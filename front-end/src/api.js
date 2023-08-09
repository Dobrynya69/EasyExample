import axios from "axios";
import config from "./config";
import { computed, ref } from 'vue'

export const HTTP = axios.create({
    baseURL: config.MOCK,
});

export default{
    async getAnime(){
        try{
            const respons = await HTTP.get('/anime/');
            return respons.data;
        }
        catch(e){
            console.log(e);
        }
    }
}