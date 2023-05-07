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
    async getAnimeWithGenres(genersList){
        try{
            console.log("sosi")
            const sos = [];
            console.log("sosi2")
            for(var i = 0; i < genersList.length; i++){
                sos.push(genersList[i]);
                console.log("sosi3")
            }   
            console.log("sosi4")
            console.log(sos[0])
            const respons = await axios.post('http://127.0.0.1:8000/api/anime/',{'genres': 'sos'});
            console.log("sosi5")
            console.log(respons.data)
            return respons.data;
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