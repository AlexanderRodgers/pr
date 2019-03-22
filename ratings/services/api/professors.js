import axios from 'axios'
import MajorApi from '~/services/api/majors.js'
axios.defaults.baseURL = 'http://localhost:8000/api/'

export default {
    getProfs() {
        return axios.get('professors/')
            .then(res => {
                console.log(res)
                return res.data
            })
    },

    getCompiledProfs() {
        let professors = []
        return axios.get('professors/')
            .then(res => {
                for (let prof of res.data) {
                    prof['first_last'] = prof.first_name + " " + prof.last_name
                    professors.push(prof)
                }
                console.log(professors)
                return professors
            })
    },

    getMajor(id) {
        return axios.get('majors/' + id)
            .then(res => {
                console.log('ress', res)
                return res.data
            })
    }
}