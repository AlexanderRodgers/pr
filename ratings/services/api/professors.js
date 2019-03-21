import axios from 'axios'
import MajorApi from '~/services/api/majors.js'

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
                // We make another variable so we don't change the response data.
                for (let prof of res.data) {
                    prof['first_last'] = prof.first_name + " " + prof.last_name
                    prof['major_stats'] = MajorApi.getMajor(prof['major'])
                    professors.push(prof)
                }
                console.log(professors)
                return professors
            })
    }
}