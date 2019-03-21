import axios from 'axios'

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