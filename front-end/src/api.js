import axios from "axios";
import config from "./config";

export const HTTP = axios.create({
    baseURL: config.MOCK,
});

export default{
    async getAnime(props){
        try{
            if(props === null){
                const respons = await HTTP.get('/anime/');
                return respons.data;
            }
            else{
                const respons = await HTTP.get('/anime/',{
                    params: {
                        page: props.page,
                    }
                });
                return respons.data;
            }
        } catch(e){
            console.log(e + "!!!");
        }
    },
    async searchAnime(searchString){
        const respons = await HTTP.get('/anime/',{
            params: {
                string: searchString,
            }
        });
        return respons.data;
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