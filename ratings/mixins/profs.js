import axios from 'axios'

export default {
   mounted() {
      axios.get('http://localhost:8000/api/professors/')
          .then(res => {
              for (let prof of res.data) {
                  prof['first_last'] = prof.first_name + " " + prof.last_name
                  this.professors.push(prof)
              }
          })
          .catch(e => {
              console.error(e)
          })
  }
}