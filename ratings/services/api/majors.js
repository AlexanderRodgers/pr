import axios from 'axios'
axios.defaults.baseURL = 'http://localhost:8000/api/'

export default {
    getMajors() {
        return axios.get('majors/')
        .then(res => {
            return res.data
        })
    },

    getMajor(id) {
        return axios.get('majors/' + id)
        .then(res => {
            return res.data
        })
    }
}