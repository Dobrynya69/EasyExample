import axios from "axios";
import config from "./config";

export const HTTP = axios.create({
    baseURL: config.MOCK,
});

export default{
    async getAnime(page, searchString){
        try{
            console.log(searchString)
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
    async getGenres(){
        try{
            const respons = await HTTP.get('/genre/');
            return respons.data;
        } catch(e){
            console.log(e + "!!!");
        }
    }
}