import axios from "axios";
import config from "./config";
import { computed, ref } from 'vue'

export const HTTP = axios.create({
    baseURL: config.MOCK,
});

export default{
    async getAnime(page, searchString){
        try{
            if(page === null && searchString === undefined){
                const respons = await HTTP.get('/anime/');
                return respons.data;
            }
            else if(page !== null && searchString === undefined){
                const respons = await HTTP.get('/anime/',{
                    params: {
                        page: page,
                    }
                });
                return respons.data;
            }
            else{
                const respons = await HTTP.get('/anime/',{
                    params: {
                        page: page,
                        string: searchString,
                    }
                });
                return respons.data;
            }
        } catch(e){
            console.log(e + "!!!");
        }
    },
    async getAnimeWithGenres(genersList, page){
        try{
            if(genersList.length > 0){
                const listData = [];
                for(var i = 0; i < genersList.length; i++){
                    listData.push(genersList[i]);
                }
                const url = ref(computed(() => `http://127.0.0.1:8000/api/anime/?page=${page}`));
                console.log(url.value);
                const respons = await axios.post(url.value,{
                    'genres': listData,
                });
                return respons.data;
            }
        } catch(e){
            console.log(e + "!!!");
        }
    },
    async getGenres(){
        try{
            const respons = await HTTP.get('/genre/');
            return respons.data;
        } catch(e){
            console.log(e + "!!!");
        }
    }
}