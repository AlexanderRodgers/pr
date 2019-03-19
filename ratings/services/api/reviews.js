import axios from 'axios'

export default {
    getReviews() {
        return axios.get('reviews/')
            .then(res => {
                return res.data
            })
    },
}