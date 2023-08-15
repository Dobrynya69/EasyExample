import axios from "axios";
import config from "./config";
import { computed, ref } from 'vue'

export const HTTP = axios.create({
    baseURL: config.MOCK,
});

export default{
    async getAnime(page){
        try{
            if(page === undefined){
                page = 1;
            }
            const respons = await HTTP.get('/anime/',{
                params: {
                    page
                }
            });
            return respons.data;
        }
        catch(e){
            console.log(e);
        }
    }
}