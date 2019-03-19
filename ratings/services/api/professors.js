import axios from 'axios'

export default {
    getProfessors() {
        let professors = []
        return axios.get('professors/')
            .then(res => {
                for (let prof of res.data) {
                    prof['first_last'] = prof.first_name + " " + prof.last_name
                    professors.push(prof)
                }
                return professors
            })
    }
}